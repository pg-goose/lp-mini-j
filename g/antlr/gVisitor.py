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


    # Visit a parse tree produced by gParser#suma.
    def visitSuma(self, ctx:gParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gParser#numero.
    def visitNumero(self, ctx:gParser.NumeroContext):
        return self.visitChildren(ctx)



del gParser