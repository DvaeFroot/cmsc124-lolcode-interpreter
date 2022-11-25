from lexer import *
from parser import *


def doTest(name, txt, shouldFail=False,printOutput=False):
    lx = Lexer()
    lx.input(txt)
    res = Parser(list(lx.tokens()))
    output = str(res.parse())
    #  print(output)
    hasError = 'Error LOL' in output
    if hasError == (not shouldFail):
        print("FAILED:", name)
    else:
        print("PASSED:", name)

    if printOutput:
        print(output)


#  doTest("Blank Program",
#         """
#         HAI
#         WTF?
#         OMG 1 VISIBLE hai GTFO
#         OMG 2 VISIBLE hai GTFO
#         OMG 3 VISIBLE hai GTFO
#         OIC
#      KTHXBYE
#         """)

#  doTest("Invalid Typo Blank Program",
#         """
#         HA
#         KTHXBYE
#         """,
#         shouldFail=True)
#
#  doTest("Assignment Numbr",
#         """
#          HAI
#          VARIABLE R 1
#          I HAS A VAR ITZ 10
#          KTHXBYE
#         """)
#
#  doTest("Assignment Numbar",
#         """
#          HAI
#          VARIABLE R 1.0
#          I HAS A VAR ITZ 10.0
#          KTHXBYE
#         """)

doTest("Assignment Yarn",
       """
        HAI
        VARIABLE R "variable"
        I HAS A VAR ITZ "this is a yarn"
        KTHXBYE
       """)

#  doTest("Invalid Assignment Variable",
#         """
#          HAI
#          VARIABLE R VARIABLE
#          I HAS A VAR ITZ VAR
#          KTHXBYE
#         """,
#         shouldFail=True)
