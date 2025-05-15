import sys
from antlr4 import CommonTokenStream, InputStream

from g.antlr.gLexer import gLexer
from g.antlr.gParser import gParser
from g.core.evaluator import EvaluatorVisitor


def repl():
    """
    A simple REPL (Read-Eval-Print Loop) for the G interpreter.
    """
    visitor = EvaluatorVisitor()
    while True:
        try:
            # Read input from the user
            user_input = input("> ")
            if user_input.lower() in ["exit", "quit"]:
                print("bye :(")
                sys.exit(0)
                break
            # Create a lexer and parser for the input
            input_stream = InputStream(input('? '))
            lexer = gLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = gParser(token_stream)
            tree = parser.root()
            result = visitor.visit(tree)
            print(result)
        except KeyboardInterrupt:
            print("\nbye :(")
            sys.exit(0)
        except Exception as e:
            print(f"Error: {e}")
            continue