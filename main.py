from antlr4 import InputStream, CommonTokenStream
from exprsLexer import exprsLexer as ExprsLexer
from exprsParser import exprsParser as ExprsParser
from visitors import EvalVisitor

def repl():
    visitor = EvalVisitor()
    while True:
        try:
            line = input('? ')
            if not line.strip():
                continue
            stream = InputStream(line + '\n')
            lexer  = ExprsLexer(stream)
            tokens = CommonTokenStream(lexer)
            parser = ExprsParser(tokens)
            tree   = parser.root()
            visitor.visit(tree)
        except NameError as ne:
            print(ne)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    repl()
