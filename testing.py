from lexer import *
from parser import *


def doTest(name, txt, shouldFail=False):
    lx = Lexer()
    lx.input(txt)
    res = Parser(list(lx.tokens()))
    output = str(res.parse())
    print(output)
    hasError = 'Error LOL' in output
    if hasError == (not shouldFail):
        print("FAILED:", name)
    else:
        print("PASSED:", name)


doTest("Blank Program",
       """
       HAI
       WTF?
       OMG 1 VISIBLE hai GTFO
       OMG 2 VISIBLE hai GTFO
       OMG 3 VISIBLE hai GTFO
       OIC
    KTHXBYE
       """)

#  doTest("Typo Blank Program",
#         """
#         HA
#         KTHXBYE
#         """,
#         shouldFail=True)
