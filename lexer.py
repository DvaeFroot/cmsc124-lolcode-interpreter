#Forked from https://gist.github.com/eliben/5797351
import re
import sys


class Token(object):
    def __init__(self, type, val, pos):
        self.type = type
        self.val = val
        self.pos = pos

    def __str__(self):
        return '%s(%s) at %s' % (self.type, self.val, self.pos)


class LexerError(Exception):
    def __init__(self, pos):
        self.pos = pos


class Lexer(object):
    def __init__(self, rules, skip_whitespace=True):
        idx = 1
        regex_parts = []
        self.group_type = {}

        for regex, type in rules:
            #Define the name of the group
            groupname = 'GROUP%s' % idx
            #Define Capture Groupname and the corresponding regex
            regex_parts.append('(?P<%s>%s)' % (groupname, regex))
            #Define the type of the groupname
            self.group_type[groupname] = type
            idx += 1

        #This is where all the rules get compiled separated by '|'. This is the only regex that will be used for checking Lexemes
        self.regex = re.compile('|'.join(regex_parts))

        #For white space checking
        self.skip_whitespace = skip_whitespace
        self.re_ws_skip = re.compile('\S')

    def input(self, buf):
        self.buf = buf
        self.pos = 0

    def token(self):
        if self.pos >= len(self.buf):
            return None

        #This one can just be omitted. It's only used if we try to skip whitespaces
        if self.skip_whitespace:
            #Get the first space from starting position
            m = self.re_ws_skip.search(self.buf, self.pos)

            if m == None:
                #No match means end of file
                return None
            
            #Get new starting position for regex searching
            self.pos = m.start()

        #Do regex match. This is the only codeblock needed
        m = self.regex.match(self.buf, self.pos)
        if m:
            #Get the group that was matched
            groupname = m.lastgroup
            #Get the type of the token using the groupname
            tok_type = self.group_type[groupname]
            #Get the current token using the groupname. The actual token is in m.group(groupname). 
            #The Token class is just a struct to store information about the current token.
            tok = Token(tok_type, m.group(groupname), self.pos)
            #Update the position
            if str(m.group(groupname)) == "BTW":
                newline = re.compile(r"\n")
                m = newline.search(self.buf, self.pos)

                if m:
                    #Get new starting position for regex searching
                    self.pos = m.start()
            elif str(m.group(groupname)) == "OBTW":
                newline = re.compile(r"TLDR")
                m = newline.search(self.buf, self.pos)

                if m:
                    #Get new starting position for regex searching
                    self.pos = m.start()
            else:
                self.pos = m.end()
            return tok

        # if we're here, no rule matched
        # We can replace this one or outright remove it
        raise LexerError(self.pos)

    def tokens(self):
        #Get all tokens
        while 1:
            tok = self.token()
            if tok is None:
                break
            yield tok


if __name__ == '__main__':
    rules = [
        # litereal
        (r'\"[^\"]*\"',                                   'String Literal'),
        (r'\bTROOF|NOOB|NUMBR|NUMBAR|YARN|TYPE\b',    'Type Literal'),
        (r'\bWIN|FAIL\b',                             'Boolean Literal'),
        (r'\b-?\d+.\d+\b',                            'Float Literal'),
        (r'\b0|-?[1-9][0-9]*\b',                      'Integer Literal'),
        # keywords
        (r'\bIF\sU\sSAY\sSO\b',                       'Function Closing Keyword'),
        (r'\bIM\sOUTTA\sYR\b',                        'Loop Closing Keyword'),
        (r'\bQUOSHUNT\sOF\b',                         'Division Operator'),
        (r'\bPRODUKT\sOF\b',                          'Multiplication Operator'),
        (r'\bBOTH\sSAEM\b',                           'Equality Operator'),
        (r'\bEITHER\sOF\b',                           'Or Operator'),
        (r'\bHOW\sIZ\sI\b',                           'Function Declaration'),
        (r'\bIM\sIN\sYR\b',                           'Loop Start Keyword'),
        (r'\bIS\sNOW\sA\b',                           'IS NOW A'),
        (r'\bSMALLR\sOF\b',                           'Return Minimum Keyword'),
        (r'\bBIGGR\sOF\b',                            'Return Maximum Keyword'),
        (r'\bI\sHAS\sA\b',                            'Variable Declaration'),
        (r'\bBOTH\sOF\b',                             'And Operator'),
        (r'\bDIFF\sOF\b',                             'Subtraction Operator'),
        (r'\bDIFFRINT\b',                             'Not Equal Operator'),
        (r'\bO\sRLY\?\b',                             'If conditional'),
        (r'\bALL\sOF\b',                              'Infinite Arity And Operator'),
        (r'\bANY\sOF\b',                              'Infinite Arity Or Operator'),
        (r'\bKTHXBYE\b',                              'Code End Delimiter'),
        (r'\bMOD\sOF\b',                              'Modulo Operator'),
        (r'\bNO\sWAI\b',                              'Else Keyword'),
        (r'\bSUM\sOF\b',                              'Summation Keyword'),
        (r'\bVISIBLE\b',                              'Output Keyword'),
        (r'\bWON\sOF\b',                              'XOR Operator'),
        (r'\bYA\sRLY\b',                              'Truth Codeblock keyword'),
        (r'\bGIMMEH\b',                               'Read Keyword'),
        (r'\bNERFIN\b',                               'Decrement Keyword'),
        (r'\bOMGWTF\b',                               'Break Default Keyword'),
        (r'\bSMOOSH\b',                               'Concatenation Keyword'),
        (r'\bFOUND\b',                                'Return Keyword'),
        (r'\bI\sIZ\b',                                'Function Call'),
        (r'\bMEBBE\b',                                'Else If Keyword'),
        (r'\bUPPIN\b',                                'Increment Keyword'),
        (r'\bWTF\?\b',                                'Switch Case Keyword'),
        (r'\bGTFO\b',                                 'Return Keyword with no value'),
        (r'\bMAEK\b',                                 'Typecast Keyword'),
        (r'\bMKAY\b',                                 'MKAY Keyword'),
        (r'\bOBTW\b',                                 'Multiline Comment Start Delimiter'),
        (r'\bTLDR\b',                                 'Multiline Comment End Delimiter'),
        (r'\bWILE\b',                                 'While Keyword'),
        (r'\bBTW\b',                                  'Comment Delimiter'),
        (r'\bHAI\b',                                  'Code Delimiter'),
        (r'\bITZ\b',                                  'Variable Assignment'),
        (r'\bNOT\b',                                  'Not Operator'),
        (r'\bOIC\b',                                  'End of control statement'),
        (r'\bOMG\b',                                  'Case Keyword'),
        (r'\bTIL\b',                                  'Until Keyword'),
        (r'\bAN\b',                                   'Argument Separator'),
        (r'\bYR\b',                                   'YR Keyword'),
        (r'\bA\b',                                    'A Keyword'),
        (r'\bR\b',                                    'Value Assignment Operator'),
        #  identifier
        (r'\b[a-z][a-z0-9_]+\b',                      'Variable Identifier'),
    ]

    lx = Lexer(rules, skip_whitespace=True)
    lx.input("""HAI 1.2
BTW this is how we declare variables
I HAS A food
I HAS A bird
BTW this is how we assign variables
food R 1
bird R 5
BTW this is how initialize variables
I HAS A biz ITZ "OMG!"
VISIBLE food
VISIBLE biz
VISIBLE bird
"HAI"
"KTHXBYE"
KTHXBYE""")

    try:
        for tok in lx.tokens():
            print(tok)
    except LexerError as err:
        print('LexerError at position %s' % err.pos)
