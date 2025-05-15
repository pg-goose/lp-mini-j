from .symbol_table import SymbolTable

from g.antlr.gParser import gParser as gp
from g.antlr import gVisitor

class EvaluatorVisitor(gVisitor):
    def __init__(self):
        super().__init__()
        self._symbol_table = SymbolTable()

    def _define(self, name: str, value = None):
        self._symbol_table.define(name, value)

    def _resolve(self, name: str):
        return self._symbol_table.resolve(name)
    
    def _perform_binary(self, ctx: gp.ExprContext, func: callable):
        [left_ctx, _, right_ctx] = list(ctx.getChildren())
        left  = self.visit(left_ctx)
        right = self.visit(right_ctx)
        return func(left, right)
    
    def _perform_unary(self, ctx: gp.ExprContext, func: callable):
        [_, right_ctx] = list(ctx.getChildren())
        right = self.visit(right_ctx)
        return func(right)
    
    # visitRoot already defined in gVisitor