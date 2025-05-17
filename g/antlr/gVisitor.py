# Generated from ./g/antlr/g.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .gParser import gParser
else:
    from gParser import gParser

# This class defines a complete generic visitor for a parse tree produced by gParser.

class gVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gParser#root.
    def visitRoot(self, ctx:gParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#help.
    def visitHelp(self, ctx:gParser.HelpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#assignment.
    def visitAssignment(self, ctx:gParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#exprStmt.
    def visitExprStmt(self, ctx:gParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#unaryexpr.
    def visitUnaryexpr(self, ctx:gParser.UnaryexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#binaryexpr.
    def visitBinaryexpr(self, ctx:gParser.BinaryexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#operand.
    def visitOperand(self, ctx:gParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#vector.
    def visitVector(self, ctx:gParser.VectorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#scalar.
    def visitScalar(self, ctx:gParser.ScalarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#unaryOp.
    def visitUnaryOp(self, ctx:gParser.UnaryOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#binaryOp.
    def visitBinaryOp(self, ctx:gParser.BinaryOpContext):
        return self.visitChildren(ctx)



del gParser