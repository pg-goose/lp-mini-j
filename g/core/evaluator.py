from .symbol_table import SymbolTable

from g.antlr.gParser import gParser as gp
from g.antlr.gVisitor import gVisitor

# switch for arithmetic operations
ARITHM_SWITCH = {
    '+': lambda x,y: x + y,
    '-': lambda x,y: x - y,
    '*': lambda x,y: x * y,
    '/': lambda x,y: x // y,
    '|': lambda x,y: x % y,
    '^': lambda x,y: x ** y
}

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
                return [func(x,y) for x,y in zip(l,r)]
            # one list only
            if isinstance(l, list):
                return [func(x,r) for x in l]
            if isinstance(r, list):
                return [func(l,y) for y in r]
            # both scalars
            return func(l,r)
        # check if operand exists in symbol table
        if op not in ARITHM_SWITCH:
            raise RuntimeError(f"Unknown operator: {op}")
        return apply(ARITHM_SWITCH[op], left, right)

class BaseEvaluator(BaseMixin, gVisitor):
    # visitRoot already defined in gVisitor

    def aggregateResult(self, aggregate, nextResult):
        # override this because all terminal nodes return None
        return nextResult or aggregate

    def visitExprStmt(self, ctx: gp.ExprStmtContext):
        return self.visit(ctx.expr())

    def visitExpr(self, ctx: gp.ExprContext):
        # the expression can be an single operand or a operand with some operator
        # if it is a single operand, we can just return the value
        left = ctx.operand()
        if ctx.binaryop():
            operator = ctx.binaryop().getText()
            right = ctx.expr()
            return self._perform(operator, left, right)
        return self.visit(left)
    
    def visitHelp(self, ctx: gp.HelpContext):
        # traverse the class tree and print it's name
        for cls in type(self).__mro__:
            print(cls.__name__)
        
    def visitAssignment(self, ctx: gp.AssignmentContext):
        name  = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self._define(name, value)
        return None

    def visitOperand(self, ctx):
        # the operand can be a scalar, a vector, a symbol or parenthesis
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

    def visitScalar(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())
        # TODO expand for other types

class ArithmeticMixin(BaseMixin):
    def visitSUM(self, ctx: gp.SUMContext):
        print("not implemented yet")

class GEvaluator(BaseEvaluator):
    """
    Evaluator for the g language.
    """
    def __init__(self):
        super().__init__()