from lexer import *
from parser import *


def doTest(name, txt, shouldFail=False,printOutput=False):
    lx = Lexer()
    lx.input(txt)
    res = Parser(list(lx.tokens()))
    output = str(res.parse())
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

doTest("Invalid Typo Blank Program",
       """
       HA
       KTHXBYE
       """,
       shouldFail=True)

print("\n USER INPUT \n")

doTest("Input Variable",
       """
        HAI
        GIMMEH x
        KTHXBYE
       """)

doTest("Invalid Input Yarn",
       """
        HAI
        GIMMEH "x yarn"
        KTHXBYE
       """,shouldFail=True)

doTest("Invalid Input Numbr",
       """
        HAI
        GIMMEH 69
        KTHXBYE
       """,shouldFail=True)

doTest("Invalid Input Numbar",
       """
        HAI
        GIMMEH 1.23
        KTHXBYE
       """,shouldFail=True)

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

doTest("Assignment Variable",
       """
        HAI
        VARIABLE R VARIABLE
        I HAS A VAR ITZ VAR
        KTHXBYE
       """)

doTest("Assignment Expression",
       """
        HAI
        VARIABLE R SUM OF 10 AN 20
        I HAS A VAR ITZ DIFF OF 100 AN 50
        KTHXBYE
       """)

print("\n OPERATIONS: Arithmetic \n")

doTest("Sum Numbr",
       """
        HAI
        SUM OF 1 AN 2
        KTHXBYE
       """)

doTest("Sum Numbar",
       """
        HAI
        SUM OF 1.2 AN 2.1
        KTHXBYE
       """)

doTest("DIFF Numbr",
       """
        HAI
        DIFF OF 1 AN 2
        KTHXBYE
       """)

doTest("DIFF Numbar",
       """
        HAI
        DIFF OF 1.2 AN 2.1
        KTHXBYE
       """)

doTest("PRODUKT Numbr",
       """
        HAI
        PRODUKT OF 1 AN 2
        KTHXBYE
       """)

doTest("PRODUKT Numbar",
       """
        HAI
        PRODUKT OF 1.2 AN 2.1
        KTHXBYE
       """)

doTest("QUOSHUNT Numbr",
       """
        HAI
        QUOSHUNT OF 1 AN 2
        KTHXBYE
       """)

doTest("QUOSHUNT Numbar",
       """
        HAI
        QUOSHUNT OF 1.2 AN 2.1
        KTHXBYE
       """)

doTest("MOD Numbr",
       """
        HAI
        MOD OF 1 AN 2
        KTHXBYE
       """)

doTest("MOD Numbar",
       """
        HAI
        MOD OF 1.2 AN 2.1
        KTHXBYE
       """)

print("\n SWITCH \n")

doTest("Switch All",
       """
        HAI
        WTF? BTW uses value in IT
        OMG "<value literal>"
            VISIBLE "OMG"
        OMG 10
            VISIBLE "OMG"
        OMGWTF
            VISIBLE "OMGWTF"
        OIC
        KTHXBYE
       """)

doTest("Switch 1 omg",
       """
        HAI
        WTF? BTW uses value in IT
        OMG "<value literal>"
            VISIBLE "OMG"
        OIC
        KTHXBYE
       """)