# POPL ANTLR Project Main Program
# Malek Necibi, Tasha Ogoti, Romelo Seals, Andy Soloviov, Akhil Mulakala


"""import sys
from antlr4 import *
from lexer_file import Lex
from parser_file import Pars


def main(argv):
    if len(sys.argv) > 1:
        input = FileStream(sys.argv[1])
    else:
        input = InputStream(sys.stdin.readline())

    lexer = Lex(input)
    tokens = CommonTokenStream(lexer)
    parser = Pars(tokens)
    tree = parser.prog()
    print(tree.toStringTree(recog = parser))

if __name__ == "__main__":
    main(sys.argv)
"""


import sys
from antlr4 import *
# import antlr4
from ExprLexer import ExprLexer
from ExprParser import ExprParser


def main(argv):
    input_stream = FileStream(argv[1])
    lexer = ExprLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.startRule()


if __name__ == '__main__':
    main(sys.argv)
