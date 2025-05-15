import operator
from antlr4 import *

# Generated from exprs.g4 by ANTLR 4.11.1
if __name__ is not None and "." in __name__:
    from .exprsParser import exprsParser as exp
else:
    from exprsParser import exprsParser as exp

# This class defines a complete generic visitor ...
class exprsVisitor(ParseTreeVisitor):
    # Visit a parse tree produced by exprsParser#root.
    def visitRoot(self, ctx:exp.RootContext):
        return self.visitChildren(ctx)

class EvalVisitor(exprsVisitor):
    def __init__(self):
        self._symbol_table = {}
    
    def _declare(self, symbol, value = None):
        self._symbol_table[symbol] = value
    
    def _retrieve(self, symbol):
        if symbol not in self._symbol_table:
            raise NameError(f"name {symbol} is not defined")
        return self._symbol_table[symbol]

    def _perform_binary(self, ctx, func):
        left_ctx, _, right_ctx = list(ctx.getChildren())
        left  = self.visit(left_ctx)
        right = self.visit(right_ctx)
        return func(left, right)

    def visitRoot(self, ctx):
        [expr] = list(ctx.getChildren())
        self.visit(expr)
    
    # assignment: SYM ':=' expr
    def visitAssignment(self, ctx: exp.AssignmentContext):
        name  = ctx.SYM().getText()
        value = self.visit(ctx.expr())
        self._declare(name, value)
        return value
    
    # write: 'write' expr
    def visitWrite(self, ctx: exp.WriteContext):
        value = self.visit(ctx.expr())
        print(value)
        return value

    # pow: expr '^' expr
    def visitPow(self, ctx: exp.PowContext):
        return self._perform_binary(ctx, operator.pow)

    # mult: expr '*' expr
    def visitMult(self, ctx):
        return self._perform_binary(ctx, operator.mul)

    # div: expr '/' expr
    def visitDiv(self, ctx):
        [_, _, right] = list(ctx.getChildren())
        if right == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return self._perform_binary(ctx, operator.truediv)

    # sum: expr '+' expr
    def visitSum(self, ctx):
        return self._perform_binary(ctx, operator.add)

    # sub: expr '-' expr
    def visitSub(self, ctx):
        return self._perform_binary(ctx, operator.sub)

    # negative: '-' expr
    def visitNegative(self, ctx: exp.NegativeContext):
        return -(self.visit(ctx.expr()))

    # parenthesis: '(' expr ')'
    def visitParenthesis(self, ctx: exp.ParenthesisContext):
        return self.visit(ctx.expr())

    # number: NUM
    def visitNumber(self, ctx: exp.NumberContext):
        return int(ctx.NUM().getText())

    # symbol: SYM
    def visitSymbol(self, ctx: exp.SymbolContext):
        return self._retrieve(ctx.SYM().getText())
