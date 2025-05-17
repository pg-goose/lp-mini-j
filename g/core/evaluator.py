from g.core.binary_operatos import BINARYOPS_SWITCH
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
        """
        Apply op between left and right depening on the type
        All ops are elementwise, so:
          - scalar ∘ scalar  => scalar
          - scalar ∘ list    => [scalar ∘ e for e in list]
          - list ∘ scalar    => [e ∘ scalar for e in list]
          - list ∘ list      => zip-wise [e1 ∘ e2 …]
        """
        # helper function, applies f to a and b
        def apply(func, l, r):
            # both lists?
            if isinstance(l, list) and isinstance(r, list):
                if len(l) != len(r):
                    raise ValueError("lists of different length")
                return [func(x,y) for x,y in zip(l,r)]
            # one list only
            if isinstance(l, list):
                return [func(x,r) for x in l]
            if isinstance(r, list):
                return [func(l,y) for y in r]
            # both scalars
            return func(l,r)
        # check if operand exists in symbol table
        if op not in BINARYOPS_SWITCH:
            raise RuntimeError(f"Unknown operator: {op}")
        return apply(BINARYOPS_SWITCH[op], left, right)

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
        "Expression that consists in `expression operator expression`"
        left = self.visit(ctx.operand())
        if not ctx.binaryOp():
            # if there is no binary operator, just return the left operand
            return left
        right = self.visit(ctx.expr())
        op = ctx.binaryOp().getText()
        return self._perform(op, left, right)

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
    
    def visitUnaryexpr(self, ctx: gp.UnaryexprContext):
        "Expression that consists in `operator expression`"
        # if there is no unary operator, just return the operand
        if not ctx.unaryOp():
            return self.visit(ctx.operand())
        # if there is a unary operator, apply it to the operand
        op = ctx.unaryOp().getText()
        value = self.visit(ctx.operand())
        if op in UNARYOPS_SWITCH:
            value = UNARYOPS_SWITCH[op](value)
        else:
            raise RuntimeError(f"Unknown operator: {op}")
        return value

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
            

class GEvaluator(BaseEvaluator, ExprMixin, OperandMixin):
    """
    Evaluator for the g language.
    """
    def __init__(self):
        super().__init__()