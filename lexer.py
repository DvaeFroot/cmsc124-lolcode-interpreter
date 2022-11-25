#Forked from https://gist.github.com/eliben/5797351
import re
from token_types import *
from parser import Parser


class Token(object):
    def __init__(self, type, val, pos):
        self.type = type
        self.val = val
        self.pos = pos

    def __str__(self):
        return '%s: %s' % (self.type, self.val)


class LexerError(Exception):
    def __init__(self, pos):
        self.pos = pos


class Lexer(object):
    def __init__(self, skip_whitespace=True):
        rules = [
            # literal
            (r'(?<=\")[^\"]*(?=\")',                      TT_STRING),
            (r'\bTROOF|NOOB|NUMBR|NUMBAR|YARN|TYPE\b',    TT_TYPE),
            (r'\bWIN|FAIL\b',                             TT_BOOLEAN),
            (r'\b-?\d+.\d+\b',                            TT_FLOAT),
            (r'\b0|-?[1-9][0-9]*\b',                      TT_INTEGER),

            # keywords
            #START
            (r'\bHOW\sIZ\sI\b',                           TT_FUNC_STRT),
            (r'\bIM\sIN\sYR\b',                           TT_LOOP_STRT),
            (r'\bHAI\b',                                  TT_CODE_STRT),

            #END
            (r'\bIF\sU\sSAY\sSO\b',                       TT_FUNC_END),
            (r'\bIM\sOUTTA\sYR\b',                        TT_LOOP_END),
            (r'\bKTHXBYE\b',                              TT_CODE_END),

            #OPERATOR
            (r'\bI\sHAS\sA\b',                            TT_VAR_DEC),
            (r'\bIS\sNOW\sA\b',                           TT_TYPECAST_1),
            (r'\bMAEK\b',                                 TT_TYPECAST_2),

            #Arithmetic
            (r'\bQUOSHUNT\sOF\b',                         TT_DIV_OP),
            (r'\bPRODUKT\sOF\b',                          TT_MUL_OP),
            (r'\bEITHER\sOF\b',                           TT_OR_OP),
            (r'\bDIFF\sOF\b',                             TT_SUB),
            (r'\bMOD\sOF\b',                              TT_MOD),
            (r'\bSUM\sOF\b',                              TT_SUMMATION),
            (r'\bNERFIN\b',                               TT_DEC),
            (r'\bUPPIN\b',                                TT_INC),

            #RELATIONAL
            (r'\bBOTH\sSAEM\b',                           TT_EQU_OP),
            (r'\bDIFFRINT\b',                             TT_NEQU),
            (r'\bBOTH\sOF\b',                             TT_AND),
            (r'\bALL\sOF\b',                              TT_AND_INF),
            (r'\bANY\sOF\b',                              TT_OR_INF),
            (r'\bNO\sWAI\b',                              TT_ELSE),
            (r'\bWON\sOF\b',                              TT_XOR),
            (r'\bNOT\b',                                  TT_NOT),

            #CONTROL
            (r'\bO\sRLY\?',                               TT_IF),
            (r'\bYA\sRLY\b',                              TT_TRUTH),
            (r'\bOMGWTF\b',                               TT_BREAK),
            (r'\bMEBBE\b',                                TT_ELIF),
            (r'\bWTF\?',                                  TT_SWITCH),
            (r'\bGTFO\b',                                 TT_CASEBREAK),
            (r'\bWILE\b',                                 TT_WHILE),
            (r'\bOIC\b',                                  TT_CONTROL_END),
            (r'\bOMG\b',                                  TT_CASE),
            (r'\bTIL\b',                                  TT_UNTIL),

            (r'\bI\sIZ\b',                                TT_FUNCALL),
            (r'\bFOUND\b',                                TT_RETURN),

            #OPERATION
            (r'\bVISIBLE\b',                              TT_OUTPUT),
            (r'\bGIMMEH\b',                               TT_READ),
            (r'\bSMOOSH\b',                               TT_CONCAT),
            (r'\bITZ\b',                                  TT_VAR_ASSIGN),
            (r'\bSMALLR\sOF\b',                           TT_MIN),
            (r'\bBIGGR\sOF\b',                            TT_MAX),
            (r'\bR\b',                                    TT_VAR_VAL_ASSIGN),

            #OTHERS
            (r'\bOBTW\b',                                 TT_COMMENT_MULTI_STRT),
            (r'\bTLDR\b',                                 TT_COMMENT_MULTI_END),
            (r'\bBTW\b',                                  TT_COMMENT_STRT),
            (r'\bMKAY\b',                                 TT_MKAY),
            (r'\bAN\b',                                   TT_ARG_SEP),
            (r'\bYR\b',                                   TT_YR),
            (r'\bA\b',                                    TT_A),
            (r'\"',                                       TT_STRING),

            #identifier
            (r'\b[a-zA-Z]\w*\b',                          'Identifier'),
        ]

        regex_parts = []
        self.group_type = {}

        for index, (regex, classification) in enumerate(rules):
            #Define the name of the group
            groupname = 'GROUP%s' % index
            #Define Capture Groupname and the corresponding regex
            regex_parts.append('(?P<%s>%s)' % (groupname, regex))
            #Define the type of the groupname
            self.group_type[groupname] = classification

        #This is where all the rules get compiled separated by '|'. This is the only regex that will be used for checking Lexemes
        self.regex = re.compile('|'.join(regex_parts))

        #For white space checking
        self.skip_whitespace = skip_whitespace
        self.regex_whitespace = re.compile('[^\s,]')


    def input(self, buf):
        self.buf = buf
        self.pos = 0


    def token(self):
        if self.pos >= len(self.buf):
            return None

        #This one can just be omitted. It's only used if we try to skip whitespaces
        if self.skip_whitespace:
            #Get the first space from starting position
            m = self.regex_whitespace.search(self.buf, self.pos)

            if m == None:
                #No match means end of file
                return None

            #Get new starting position for regex searching
            self.pos = m.start()

        #Do regex match. check for comments and skip them.
        m = self.regex.match(self.buf, self.pos)
        if m:
            groupname = m.lastgroup
            if str(m.group(groupname)) == "BTW":
                #Get the group that was matched
                groupname = m.lastgroup
                #Get the type of the token using the groupname
                tok_type = self.group_type[groupname]
                #Get the current token using the groupname. The actual token is in m.group(groupname). 
                #The Token class is just a struct to store information about the current token.
                tok = Token(tok_type, m.group(groupname), self.pos)
                #Update the position
                self.pos = m.end()

                newline = re.compile(r"\n")
                m = newline.search(self.buf, self.pos)

                if m:
                    #Get new starting position for regex searching
                    self.pos = m.start()
                else:
                    self.pos = len(self.buf)
                return tok
            elif str(m.group(groupname)) == "OBTW":
                #Get the group that was matched
                groupname = m.lastgroup
                #Get the type of the token using the groupname
                tok_type = self.group_type[groupname]
                #Get the current token using the groupname. The actual token is in m.group(groupname). 
                #The Token class is just a struct to store information about the current token.
                tok = Token(tok_type, m.group(groupname), self.pos)
                # print(tok)
                #Update the position
                self.pos = m.end()

                newline = re.compile(r"TLDR")
                m = newline.search(self.buf, self.pos)

                if m:
                    #Get new starting position for regex searching
                    self.pos = m.start()
                else:
                    self.pos = len(self.buf)

                return tok

            #Get the first space from starting position
            m = self.regex_whitespace.search(self.buf, self.pos)

            if m == None:
                #No match means end of file
                tok = Token(TT_EOF, )
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
            self.pos = m.end()
            return tok

        # if we're here, no rule matched
        # We can replace this one or outright remove it
        raise LexerError(self.pos)

    def tokens(self):
        #generator to get all tokens
        while 1:
            tok = self.token()
            if tok is None:
                break
            yield tok


if __name__ == '__main__':
    lx = Lexer()
    txt = """HAI
        BOTH OF PRODUKT OF 1 AN 2 AN 4
        BOTH OF PRODUKT OF 1 AN 2 AN 4
        BOTH OF PRODUKT OF 1 AN 2 AN 4
        BOTH OF PRODUKT OF 1 AN 2 AN 4
    KTHXBYE"""
    lx.input(txt)

    #  try:
    #      for tok in lx.tokens():
    #          print(tok)
    #  except LexerError as err:
    #      print('LexerError at position %s' % err.pos)

    res = Parser(list(lx.tokens()))
    print(res.parse())


