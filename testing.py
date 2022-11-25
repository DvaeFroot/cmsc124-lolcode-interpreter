from lexer import *
from parser import *

def doTest(name,shouldPass,txt,):
    lx = Lexer()
    lx.input(txt)
    res = Parser(list(lx.tokens()))
    hasError = 'Error LOL' in str(res.parse())
    if not shouldPass:
        hasError = not hasError
    print(name, "failed" if hasError else "passed")
    

doTest("Blank Program",
       True,
       """
       HAI
       KTHXBYE
       """)

doTest("Typo Blank Program",
       False,
       """
       HA
       KTHXBYE
       """)