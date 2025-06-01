import sys
from antlr4 import CommonTokenStream, InputStream

from g.antlr.gLexer import gLexer
from g.antlr.gParser import gParser
from g.core.evaluator import GEvaluator


def repl():
    """
    A simple REPL (Read-Eval-Print Loop) for the G interpreter.
    """
    visitor = GEvaluator()
    while True:
        try:
            # Read input from the user
            user_input = input("> ")
            if user_input.strip() == "":
                continue
            if user_input.lower() in ["exit", "quit"]:
                print("bye :(")
                sys.exit(0)
                break
            lexer = gLexer(InputStream(user_input))
            token_stream = CommonTokenStream(lexer)
            parser = gParser(token_stream)
            parser.removeErrorListeners()

            tree = parser.root()
            N = parser.getNumberOfSyntaxErrors()
            if N > 0:
                print(f'{N} syntax errors found')
                continue
            result = visitor.visit(tree)
            if result is not None:
                print(result)
        except KeyboardInterrupt:
            print("\nbye :(")
            sys.exit(0)
        except Exception as e:
            print(f"Error: {e}")
            continue