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

class EvaluatorVisitor(gVisitor):
    def __init__(self):
        super().__init__()
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
    
    # visitRoot already defined in gVisitor

    def visitAssignment(self, ctx: gp.AssignmentContext):
        """
        Visit an assignment statement.
        """
        name  = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self._define(name, value)
        return value

    def visitExprStmt(self, ctx: gp.ExprStmtContext):
        """
        Visit an expression statement.
        """
        return self.visit(ctx.expr())

    def visitExpr(self, ctx: gp.ExprContext):
        # the expression can be an single operand or a operand with some operator
        # if it is a single operand, we can just return the value
        left = ctx.operand()
        if ctx.binaryop():
            operator = ctx.binaryop().getText()
            right = ctx.expr()
            return self._perform(operator, left, right)
        

