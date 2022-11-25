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

doTest("Invalid Typo Blank Program",
       """
       HAI
IM IN YR umum UPPIN YR udud TIL BOTH SAEM udud AN 1
  VISIBLE hai
  VISIBLE hai
  VISIBLE hai
  VISIBLE hai
  VISIBLE hai
IM OUTTA YR umum
    KTHXBYE
       """, printOutput=False)

print("\n COMMENTS \n")

doTest("Multiline Comment",
       """
        HAI
        OBTW what way?
        TLDR I HAS A var2
        I HAS A var3
        KTHXBYE""")

doTest("Multiline Comment",
       """
        HAI
        OBTW what way?
        TLDR I HAS A var2
        I HAS A var3
        OBTW this
            Way
        TLDR
        KTHXBYE""")

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

doTest("BIGGR Numbr",
       """
        HAI
        MOD OF 1 AN 2
        KTHXBYE
       """)

doTest("BIGGR Numbar",
       """
        HAI
        BIGGR OF 1.2 AN 2.1
        KTHXBYE
       """)

doTest("SMALLR Numbr",
       """
        HAI
        SMALLR OF 1 AN 2
        KTHXBYE
       """)

doTest("SMALLR Numbar",
       """
        HAI
        SMALLR OF 1.2 AN 2.1
        KTHXBYE
       """)

doTest("Chain Arithmetic 1",
       """
        HAI
        SUM OF QUOSHUNT OF PRODUKT OF 3 AN 4 AN 2 AN 1
        KTHXBYE
       """)

doTest("Chain Arithmetic 2",
       """
        HAI
        SUM OF SUM OF SUM OF 3 AN 4 AN 2 AN 1
        KTHXBYE
       """)

print("\n Operations: Comparison \n")

doTest("Comparison",
       """
        HAI
        BOTH SAEM x AN y
        DIFFRINT x AN y
        KTHXBYE
       """)

doTest("Relational Comparison",
       """
        HAI
        BOTH SAEM x AN BIGGR OF x AN y BTW x >= y
        BOTH SAEM x AN SMALLR OF x AN y BTW x <= y
        DIFFRINT x AN SMALLR OF x AN y BTW x > y
        DIFFRINT x AN BIGGR OF x AN y BTW x < y
        KTHXBYE
       """)

print("\n SWITCH \n")

doTest("Switch OMG",
       """
        HAI
        WTF?
            OMG "A"
                VISIBLE "ABCD"
                GTFO
            OMG "E"
                VISIBLE "EFGH"
                GTFO
        OIC
        KTHXBYE
       """)

doTest("Switch OMG and OMGWTF",
       """
        HAI
        WTF?
            OMG "A"
                VISIBLE "ABCD"
                GTFO
            OMG "E"
                VISIBLE "EFGH"
                GTFO
            OMGWTF
                VISIBLE "IJKL"
        OIC
        KTHXBYE
       """,printOutput=False)

doTest("Switch 1 omg",
       """
        HAI
        WTF? BTW uses value in IT
        OMG "<value literal>"
            VISIBLE "OMG"
        OIC
        KTHXBYE
       """, printOutput=False)
