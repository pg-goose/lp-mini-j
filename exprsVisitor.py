# Generated from exprs.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .exprsParser import exprsParser
else:
    from exprsParser import exprsParser

# This class defines a complete generic visitor for a parse tree produced by exprsParser.

class exprsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by exprsParser#root.
    def visitRoot(self, ctx:exprsParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#assignement.
    def visitAssignement(self, ctx:exprsParser.AssignementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#write.
    def visitWrite(self, ctx:exprsParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#exprStmt.
    def visitExprStmt(self, ctx:exprsParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#div.
    def visitDiv(self, ctx:exprsParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#number.
    def visitNumber(self, ctx:exprsParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#symbol.
    def visitSymbol(self, ctx:exprsParser.SymbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#sub.
    def visitSub(self, ctx:exprsParser.SubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#negative.
    def visitNegative(self, ctx:exprsParser.NegativeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#mult.
    def visitMult(self, ctx:exprsParser.MultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#pow.
    def visitPow(self, ctx:exprsParser.PowContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#sum.
    def visitSum(self, ctx:exprsParser.SumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#parenthesis.
    def visitParenthesis(self, ctx:exprsParser.ParenthesisContext):
        return self.visitChildren(ctx)



del exprsParser