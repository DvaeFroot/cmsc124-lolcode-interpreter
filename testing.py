from lexer import *
from parser import *


def doTest(name, txt, shouldFail=False,printOutput=False):
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
    
    if printOutput:
        print(output)


doTest("Blank Program",
       """
       HAI
       WTF?
       OMG 1 VISIBLE hai
       OMG 2 VISIBLE hai
       OMG 3 VISIBLE hai
       OMG 4 VISIBLE hai
       OMG 5 VISIBLE hai
       OMG 6 VISIBLE hai
    KTHXBYE
       """)

doTest("Invalid Typo Blank Program",
       """
       HA
       KTHXBYE
       """,
       shouldFail=True)

print("\n USER OUTPUT \n")

doTest("Print Yarn",
       """
        HAI
        VISIBLE "YARN"
        KTHXBYE
       """)

doTest("Print Numbr",
       """
        HAI
        VISIBLE 1
        KTHXBYE
       """)

doTest("Print Numbar",
       """
        HAI
        VISIBLE 1.0
        KTHXBYE
       """)

doTest("Print Variable",
       """
        HAI
        VISIBLE VARIABLE
        KTHXBYE
       """)

doTest("Print Expresion",
       """
        HAI
        VISIBLE SUM OF 2 AN 4
        KTHXBYE
       """)

print("\n VARIABLES \n")

doTest("I HAS A",
       """
        HAI
        I HAS A thing
        KTHXBYE
       """)

doTest("ITZ literal Yarn",
       """
        HAI
        I HAS A thing2 ITZ "some"
        KTHXBYE
       """)

doTest("ITZ literal Numbr",
       """
        HAI
        I HAS A thing2 ITZ 2
        KTHXBYE
       """)

doTest("ITZ literal Numbar",
       """
        HAI
        I HAS A thing2 ITZ 2.0
        KTHXBYE
       """)

doTest("ITZ literal Troof",
       """
        HAI
        I HAS A thing2 ITZ WIN
        I HAS A thing3 ITZ FAIL
        KTHXBYE
       """)

doTest("ITZ Expression",
       """
        HAI
        I HAS A thing2 ITZ SUM OF 5 AN 4
        KTHXBYE
       """)

print("\n OPERATIONS \n")

doTest("Assignment Numbr",
       """
        HAI
        VARIABLE R 1
        I HAS A VAR ITZ 10
        KTHXBYE
       """)

doTest("Assignment Numbar",
       """
        HAI
        VARIABLE R 1.0
        I HAS A VAR ITZ 10.0
        KTHXBYE
       """)

doTest("Assignment Yarn",
       """
        HAI
        VARIABLE R "variable"
        I HAS A VAR ITZ "this is a yarn"
        KTHXBYE
       """)

doTest("Assignment Troof",
       """
        HAI
        VARIABLE R WIN
        I HAS A VAR ITZ FAIL
        KTHXBYE
       """)

doTest("Invalid Assignment Variable",
       """
        HAI
        VARIABLE R VARIABLE
        I HAS A VAR ITZ VAR
        KTHXBYE
       """,
       shouldFail=True)
