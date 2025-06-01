from g.core.binary_operatos import BINARYOPS_NO_LIFT, BINARYOPS_SWITCH
from g.core.error import GError, GSyntaxError, GValueError
from g.core.result import Result
from g.core.unary_operators import UNARYOPS_SWITCH
from .symbol_table import SymbolTable

from g.antlr.gParser import gParser as gp
from g.antlr.gVisitor import gVisitor


class BaseMixin:
    """
    Base mixin for evaluators, providing common functionality.
    - defining and resolving symbols,
    - performing binary operations
    - applying functions
    """
    def __init__(self):
        self._symbol_table = SymbolTable()

    def _define(self, name: str, value = None):
        self._symbol_table.define(name, value)

    def _resolve(self, name: str):
        return self._symbol_table.resolve(name)

    def _perform(self, op, left, right):
        func = BINARYOPS_SWITCH.get(op)
        if func is None:
            raise GSyntaxError(f"unknown operator {op}")
        no_broadcast = op in BINARYOPS_NO_LIFT
        return BaseMixin._apply(func, left, right, no_broadcast)

    @staticmethod # static to indicate it does not mutate an instance
    def _apply(func, l, r, no_broadcast=False):
        # both lists?
        if no_broadcast:
            return func(l, r)
    
        # https://en.wikipedia.org/wiki/Applicative_functor
        if isinstance(l, list) or isinstance(r, list):
            # turn non-lists into “constant” lists
            if not isinstance(l, list): l = [l] * len(r)
            if not isinstance(r, list): r = [r] * len(l)
            if len(l) != len(r): raise GValueError("lists of different length")
            # recurse element-wise
            return [ BaseMixin._apply(func, l, r, no_broadcast) for l,r in zip(l, r) ]
        # both scalars
        return func(l, r)

class BaseEvaluator(BaseMixin, gVisitor):
    """
    Base evaluator for G, implements the visitor pattern.
    """
    def visitRoot(self, ctx: gp.RootContext):
        result = []
        for child in ctx.stmt():
            # visit the child and aggregate the result
            try:
                r = self.visit(child)
            except GError as e:
                r = e
            if r is not None:
                result.append(Result(r))
        return result if len(result) >= 1 else None

    def aggregateResult(self, aggregate, nextResult):
        if nextResult is None:
            return aggregate
        return nextResult

    def visitHelp(self, _: gp.HelpContext):
        # traverse the class tree and print it's names
        for cls in type(self).__mro__:
            print(cls.__name__)

    def visitAssgexpr(self, ctx: gp.AssgexprContext):
        """Assignment expression."""
        name  = ctx.ID().getText()
        value = self.visit(ctx.expr() or ctx.compose())
        self._define(name, value)
        return None

    def visitExprstmt(self, ctx: gp.ExprstmtContext):
        return self.visit(ctx.expr())

class ExprMixin(BaseMixin):
    def visitCompose(self, ctx: gp.ComposeContext):
        """function composition expressions."""
        f = self.visit(ctx.expr())
        if ctx.compose() is None:
            if callable(f):
                return f
            raise GSyntaxError("cannot compose non-callable expressions")
        # compose next
        g = self.visit(ctx.compose())
        if callable(f) and callable(g):
            return lambda x: f(g(x))
        raise GSyntaxError("cannot compose non-callable expressions")
    
    def visitApplyexpr(self, ctx: gp.ApplyexprContext):
        """function application expression."""
        f = self._resolve(ctx.ID().getText())
        if callable(f):
            return f(self.visit(ctx.expr()))
        raise GSyntaxError(f"cannot apply non-callable expression: {ctx.ID().getText()}")

    def visitBinaryexpr(self, ctx: gp.BinaryexprContext):
        """Binary expressions with optional flip operator."""
        left = self.visit(ctx.operand())
        bin_ctx  = ctx.binaryOp()
        flip_ctx = ctx.flipOp()
    
        # no operator -> just the single operand
        if not (bin_ctx or flip_ctx):
            return left
        # figure out which BinaryOpContext actually applies
        op_ctx = bin_ctx or flip_ctx.binaryOp()
        op = op_ctx.getText()
        # compute the right side
        right = self.visit(ctx.expr())

        if callable(right):
            return lambda x: self._perform(op, left, right(x))

        # if it was a “flip”, swap args
        a, b = (right, left) if flip_ctx else (left, right)
        return self._perform(op, a, b)

    def visitUnaryexpr(self, ctx: gp.UnaryexprContext):
        """Unary expressions with optional unary operator."""
        op = ctx.unaryOp().getText()
        expr_ctx = ctx.expr()
        value = self.visit(expr_ctx) if expr_ctx else None

        # built-in unary operator
        if op in UNARYOPS_SWITCH:
            func = UNARYOPS_SWITCH[op]
            # no operand, return as first-class function
            if value is None:
                return func
            return func(value)

        # custom visitor for this operator?
        func = self.visit(ctx.unaryOp())
        if callable(func):
            if value is None:
                return func
            return func(value)
        raise GSyntaxError(f"unknown operator {op}")

class OperandMixin(BaseMixin):
    """Operand mixin includes methods for visiting operands."""
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
        # TODO expand for nested vectors?

    def visitScalar(self, ctx: gp.ScalarContext):
        value = None
        if ctx.INT():
            value = int(ctx.INT().getText())
        if ctx.NEGATIVE():
            value = -value
        return value

class UnaryMixin(BaseMixin):
    """Unary mixin includes methods for visiting unary expressions."""
    def fold(self, func, iter):
        # TODO should I put fold here?
        if not isinstance(iter, list):
            iter = [iter]
        if len(iter) == 0:
            return 0
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
        """binaryOp ':' -> retorna funció x -> op(x, x)."""
        op = ctx.binaryOp().getText()
        if op is None or op not in BINARYOPS_SWITCH:
            raise GSyntaxError(f"unknown binary operator ‘{op}’")
        return lambda x, op=op: self._perform(op, x, x)


class GEvaluator(BaseEvaluator, ExprMixin, OperandMixin, UnaryMixin):
    """
    Evaluator for G
    """
    def __init__(self):
        super().__init__()