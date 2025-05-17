# Generated from ./g/antlr/g.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,15,63,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,4,0,18,8,0,11,0,12,0,19,1,0,1,0,1,1,1,1,1,1,1,1,1,
        1,3,1,29,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,38,8,2,3,2,40,8,2,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,49,8,3,1,4,1,4,4,4,53,8,4,11,4,12,
        4,54,1,5,1,5,1,6,1,6,1,7,1,7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,1,1,
        0,5,10,63,0,17,1,0,0,0,2,28,1,0,0,0,4,39,1,0,0,0,6,48,1,0,0,0,8,
        50,1,0,0,0,10,56,1,0,0,0,12,58,1,0,0,0,14,60,1,0,0,0,16,18,3,2,1,
        0,17,16,1,0,0,0,18,19,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,21,
        1,0,0,0,21,22,5,0,0,1,22,1,1,0,0,0,23,29,5,1,0,0,24,25,5,13,0,0,
        25,26,5,11,0,0,26,29,3,4,2,0,27,29,3,4,2,0,28,23,1,0,0,0,28,24,1,
        0,0,0,28,27,1,0,0,0,29,3,1,0,0,0,30,31,3,12,6,0,31,32,3,4,2,0,32,
        40,1,0,0,0,33,37,3,6,3,0,34,35,3,14,7,0,35,36,3,4,2,0,36,38,1,0,
        0,0,37,34,1,0,0,0,37,38,1,0,0,0,38,40,1,0,0,0,39,30,1,0,0,0,39,33,
        1,0,0,0,40,5,1,0,0,0,41,49,3,8,4,0,42,49,3,10,5,0,43,49,5,13,0,0,
        44,45,5,2,0,0,45,46,3,4,2,0,46,47,5,3,0,0,47,49,1,0,0,0,48,41,1,
        0,0,0,48,42,1,0,0,0,48,43,1,0,0,0,48,44,1,0,0,0,49,7,1,0,0,0,50,
        52,3,10,5,0,51,53,3,10,5,0,52,51,1,0,0,0,53,54,1,0,0,0,54,52,1,0,
        0,0,54,55,1,0,0,0,55,9,1,0,0,0,56,57,5,12,0,0,57,11,1,0,0,0,58,59,
        5,4,0,0,59,13,1,0,0,0,60,61,7,0,0,0,61,15,1,0,0,0,6,19,28,37,39,
        48,54
    ]

class gParser ( Parser ):

    grammarFileName = "g.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'help'", "'('", "')'", "'_'", "'+'", 
                     "'-'", "'*'", "'/'", "'|'", "'^'", "'=:'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "ASSIGN", "INT", 
                      "ID", "WS", "COMMENT" ]

    RULE_root = 0
    RULE_stmt = 1
    RULE_expr = 2
    RULE_operand = 3
    RULE_vector = 4
    RULE_scalar = 5
    RULE_unaryOp = 6
    RULE_binaryOp = 7

    ruleNames =  [ "root", "stmt", "expr", "operand", "vector", "scalar", 
                   "unaryOp", "binaryOp" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    ASSIGN=11
    INT=12
    ID=13
    WS=14
    COMMENT=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(gParser.EOF, 0)

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gParser.StmtContext)
            else:
                return self.getTypedRuleContext(gParser.StmtContext,i)


        def getRuleIndex(self):
            return gParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = gParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.stmt()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 12310) != 0)):
                    break

            self.state = 21
            self.match(gParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gParser.RULE_stmt

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class HelpContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitHelp" ):
                return visitor.visitHelp(self)
            else:
                return visitor.visitChildren(self)


    class ExprStmtContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(gParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStmt" ):
                return visitor.visitExprStmt(self)
            else:
                return visitor.visitChildren(self)


    class AssignmentContext(StmtContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.StmtContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(gParser.ID, 0)
        def ASSIGN(self):
            return self.getToken(gParser.ASSIGN, 0)
        def expr(self):
            return self.getTypedRuleContext(gParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)



    def stmt(self):

        localctx = gParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 28
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = gParser.HelpContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.match(gParser.T__0)
                pass

            elif la_ == 2:
                localctx = gParser.AssignmentContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.match(gParser.ID)
                self.state = 25
                self.match(gParser.ASSIGN)
                self.state = 26
                self.expr()
                pass

            elif la_ == 3:
                localctx = gParser.ExprStmtContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 27
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class UnaryexprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def unaryOp(self):
            return self.getTypedRuleContext(gParser.UnaryOpContext,0)

        def expr(self):
            return self.getTypedRuleContext(gParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryexpr" ):
                return visitor.visitUnaryexpr(self)
            else:
                return visitor.visitChildren(self)


    class BinaryexprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a gParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def operand(self):
            return self.getTypedRuleContext(gParser.OperandContext,0)

        def binaryOp(self):
            return self.getTypedRuleContext(gParser.BinaryOpContext,0)

        def expr(self):
            return self.getTypedRuleContext(gParser.ExprContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryexpr" ):
                return visitor.visitBinaryexpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self):

        localctx = gParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                localctx = gParser.UnaryexprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.unaryOp()
                self.state = 31
                self.expr()
                pass
            elif token in [2, 12, 13]:
                localctx = gParser.BinaryexprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.operand()
                self.state = 37
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2016) != 0):
                    self.state = 34
                    self.binaryOp()
                    self.state = 35
                    self.expr()


                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vector(self):
            return self.getTypedRuleContext(gParser.VectorContext,0)


        def scalar(self):
            return self.getTypedRuleContext(gParser.ScalarContext,0)


        def ID(self):
            return self.getToken(gParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(gParser.ExprContext,0)


        def getRuleIndex(self):
            return gParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = gParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_operand)
        try:
            self.state = 48
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.vector()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.scalar()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                self.match(gParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 44
                self.match(gParser.T__1)
                self.state = 45
                self.expr()
                self.state = 46
                self.match(gParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VectorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gParser.ScalarContext)
            else:
                return self.getTypedRuleContext(gParser.ScalarContext,i)


        def getRuleIndex(self):
            return gParser.RULE_vector

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVector" ):
                return visitor.visitVector(self)
            else:
                return visitor.visitChildren(self)




    def vector(self):

        localctx = gParser.VectorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vector)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.scalar()
            self.state = 52 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 51
                    self.scalar()

                else:
                    raise NoViableAltException(self)
                self.state = 54 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScalarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(gParser.INT, 0)

        def getRuleIndex(self):
            return gParser.RULE_scalar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScalar" ):
                return visitor.visitScalar(self)
            else:
                return visitor.visitChildren(self)




    def scalar(self):

        localctx = gParser.ScalarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_scalar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(gParser.INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gParser.RULE_unaryOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryOp" ):
                return visitor.visitUnaryOp(self)
            else:
                return visitor.visitChildren(self)




    def unaryOp(self):

        localctx = gParser.UnaryOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_unaryOp)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(gParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinaryOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gParser.RULE_binaryOp

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryOp" ):
                return visitor.visitBinaryOp(self)
            else:
                return visitor.visitChildren(self)




    def binaryOp(self):

        localctx = gParser.BinaryOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_binaryOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2016) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





