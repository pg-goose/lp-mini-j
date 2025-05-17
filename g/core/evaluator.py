from g.core.binary_operatos import BINARYOPS_NO_LIFT, BINARYOPS_SWITCH
from g.core.unary_operators import UNARYOPS_SWITCH
from .symbol_table import SymbolTable

from g.antlr.gParser import gParser as gp
from g.antlr.gVisitor import gVisitor


class BaseMixin:
    def __init__(self):
        self._symbol_table = SymbolTable()

    def _define(self, name: str, value = None):
        self._symbol_table.define(name, value)

    def _resolve(self, name: str):
        return self._symbol_table.resolve(name)

    def _perform(self, op, left, right):
        func = BINARYOPS_SWITCH.get(op)
        if func is None:
            raise RuntimeError(f"Unknown operator: {op}")
        no_broadcast = op in BINARYOPS_NO_LIFT
        return BaseMixin._apply(func, left, right, no_broadcast)

    @staticmethod # static to indicate it does not mutate an instance
    def _apply(func, l, r, no_broadcast=False):
        # both lists?
        if no_broadcast:
            return func(l, r)
    
        # https://en.wikipedia.org/wiki/Applicative_functor
        if isinstance(left, list) or isinstance(right, list):
            # turn non-lists into “constant” lists
            if not isinstance(left, list):
                left = [left] * len(right)
            if not isinstance(right, list):
                right = [right] * len(left)
            if len(left) != len(right):
                raise ValueError("lists of different length")
            # recurse element-wise
            return [ BaseMixin._apply(func, l, r) for l,r in zip(left, right) ]
        # both scalars
        return func(l, r)

class BaseEvaluator(BaseMixin, gVisitor):
    # visitRoot already defined in gVisitor

    def aggregateResult(self, aggregate, nextResult):
        # override this because all terminal nodes return None
        if nextResult is None:
            return aggregate
        return nextResult

    def visitHelp(self, ctx: gp.HelpContext):
        # traverse the class tree and print it's name
        for cls in type(self).__mro__:
            print(cls.__name__)

    def visitExprStmt(self, ctx: gp.ExprStmtContext):
        return self.visit(ctx.expr())
    
    def visitAssignment(self, ctx: gp.AssignmentContext):
        name  = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self._define(name, value)
        return None

class ExprMixin(BaseMixin):
    def visitBinaryexpr(self, ctx: gp.BinaryexprContext):
        """operand (binaryOp expr)?"""
        # if there is no binary operator, just return the left operand
        left = self.visit(ctx.operand())
        if not ctx.binaryOp():
            return left
        right = self.visit(ctx.expr())
        op = ctx.binaryOp().getText()
        return self._perform(op, left, right)
    
    def visitUnaryexpr(self, ctx: gp.UnaryexprContext):
        """unaryOp operand"""
        op = ctx.unaryOp().getText()
        value = self.visit(ctx.operand())

        # simple unary operator
        if op in UNARYOPS_SWITCH:
            return UNARYOPS_SWITCH[op](value)
        
        # may have a visitor method
        func = self.visit(ctx.unaryOp())
        if func is not None:
            return func(value)
        raise RuntimeError(f"Unknown operator: {op}")

class OperandMixin(BaseMixin):
    def visitUnit(self, ctx):
        # the unit can be a scalar, a vector, a symbol or parenthesis
        if ctx.scalar():
            return self.visit(ctx.scalar())
        if ctx.vector():
            return self.visit(ctx.vector())
        if ctx.ID(): # if symbol, resolve it
            name = ctx.ID().getText()
            return self._resolve(name)
        # if parenthesis, visit the expression inside
        return self.visit(ctx.expr())

    def visitVector(self, ctx):
        # the vector can be a list of scalars or a list of vectors
        # if it is a list of scalars, we can just return the list
        if isinstance(ctx.scalar(), list):
            return [self.visit(scalar) for scalar in ctx.scalar()]
        # TODO expand for nested vectors

    def visitScalar(self, ctx: gp.ScalarContext):
        value = None
        if ctx.INT():
            value = int(ctx.INT().getText())
        # TODO expand for other types
        return value

class UnaryMixin(BaseMixin):
    def fold(self, func, iter):
        # TODO should I put fold here? not the best organizational choice
        if not isinstance(iter, list):
            iter = [iter]
        acc = iter[0]
        for item in iter[1:]:
            acc = func(acc, item)
        return acc

    def visitFold(self, ctx: gp.FoldContext):
        """binaryOp '/'"""
        op = ctx.binaryOp().getText()
        func = BINARYOPS_SWITCH[op]
        # we return the partially applied fold
        return lambda iter: self.fold(func, iter)
    
    def visitMakeunary(self, ctx: gp.MakeunaryContext):
        """binaryOp ':' ⇒ retorna funció x ↦ op(x, x)."""
        op = ctx.binaryOp().getText()
        if op is None or op not in BINARYOPS_SWITCH:
            raise RuntimeError(f"Unknown binary operator ‘{op}’")
        return lambda x: self._perform(op, x, x)



class GEvaluator(BaseEvaluator, ExprMixin, OperandMixin, UnaryMixin):
    """
    Evaluator for the g language.
    """
    def __init__(self):
        super().__init__()