import sys
from antlr4 import FileStream, CommonTokenStream
from g.antlr.gLexer import gLexer
from g.antlr.gParser import gParser
from g.core.evaluator import GEvaluator
from g.repl import repl

def main():
    if len(sys.argv) < 2:
        repl()
        return
    j_file = sys.argv[1]

    if not j_file.endswith(".j"):
        print("Warn: file must have .j extension")
    
    visitor = GEvaluator()

    inputStream = FileStream(j_file, encoding='utf-8')
    lexer = gLexer(inputStream)
    lexer.removeErrorListeners()

    token_stream = CommonTokenStream(lexer)
    parser = gParser(token_stream)
    parser.removeErrorListeners()

    tree = parser.root()
    N = parser.getNumberOfSyntaxErrors()
    if N > 0:
        print(f'{N} syntax errors found')
        return 1
    result = visitor.visit(tree)
    for r in result:
        if r is not None:
            print(r)
    return 0

if __name__ == "__main__":
    main()