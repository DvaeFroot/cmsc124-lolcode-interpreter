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
        else:
            #This one can just be omitted. It's only used if we try to skip whitespaces
            if self.skip_whitespace:
                #Get the first space from starting position
                m = self.re_ws_skip.search(self.buf, self.pos)

                if m:
                    #Get new starting position for regex searching
                    self.pos = m.start()
                else:
                    #No match means end of file
                    return None

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
        #Get all tokens
        while 1:
            tok = self.token()
            if tok is None:
                break
            yield tok


if __name__ == '__main__':
    rules = [
        # litereal
        (r'\".*\"',                                 'YARN'),
        (r'\bTROOF|NOOB|NUMBR|NUMBAR|YARN|TYPE',    'TYPE'),
        (r'\bWIN|FAIL',                             'TROOF'),
        (r'\b-?\d+.\d+',                            'NUMBAR'),
        (r'\b0|-?[1-9][0-9]*\b',                    'NUMBR'),
        # keywords
        (r'\bIF\sU\sSAY\sSO',                       'IF U SAY SO'),
        (r'\bIM\sOUTTA\sYR',                        'IM OUTTA YR'),
        (r'\bQUOSHUNT\sOF',                         'QUOSHUNT OF'),
        (r'\bPRODUKT\sOF',                          'PRODUKT OF'),
        (r'\bBOTH\sSAEM',                           'BOTH SAEM'),
        (r'\bEITHER\sOF',                           'EITHER OF'),
        (r'\bHOW\sIZ\sI',                           'HOW IZ I'),
        (r'\bIM\sIN\sYR',                           'IM IN YR'),
        (r'\bIS\sNOW\sA',                           'IS NOW A'),
        (r'\bSMALLR\sOF',                           'SMALLR OF'),
        (r'\bBIGGR\sOF',                            'BIGGR OF'),
        (r'\bI\sHAS\sA',                            'I HAS A'),
        (r'\bBOTH\sOF',                             'BOTH OF'),
        (r'\bDIFF\sOF',                             'DIFF OF'),
        (r'\bDIFFRINT',                             'DIFFRINT'),
        (r'\bO\sRLY\?',                             'O RLY?'),
        (r'\bALL\sOF',                              'ALL OF'),
        (r'\bANY\sOF',                              'ANY OF'),
        (r'\bKTHXBYE',                              'KTHXBYE'),
        (r'\bMOD\sOF',                              'MOD OF'),
        (r'\bNO\sWAI',                              'NO WAI'),
        (r'\bSUM\sOF',                              'SUM OF'),
        (r'\bVISIBLE',                              'VISIBLE'),
        (r'\bWON\sOF',                              'WON OF'),
        (r'\bYA\sRLY',                              'YA RLY'),
        (r'\bGIMMEH',                               'GIMMEH'),
        (r'\bNERFIN',                               'NERFIN'),
        (r'\bOMGWTF',                               'OMGWTF'),
        (r'\bSMOOSH',                               'SMOOSH'),
        (r'\bFOUND',                                'FOUND'),
        (r'\bI\sIZ',                                'I IZ'),
        (r'\bMEBBE',                                'MEBBE'),
        (r'\bUPPIN',                                'UPPIN'),
        (r'\bWTF\?',                                'WTF?'),
        (r'\bGTFO',                                 'GTFO'),
        (r'\bMAEK',                                 'MAEK'),
        (r'\bMKAY',                                 'MKAY'),
        (r'\bOBTW',                                 'OBTW'),
        (r'\bTLDR',                                 'TLDR'),
        (r'\bWILE',                                 'WILE'),
        (r'\bBTW',                                  'BTW'),
        (r'\bHAI',                                  'HAI'),
        (r'\bITZ',                                  'ITZ'),
        (r'\bNOT',                                  'NOT'),
        (r'\bOIC',                                  'OIC'),
        (r'\bOMG',                                  'OMG'),
        (r'\bTIL',                                  'TIL'),
        (r'\bAN',                                   'AN'),
        (r'\bYR',                                   'YR'),
        (r'\bA',                                    'A'),
        (r'\bR',                                    'R'),
        #  identifier
        (r'\b[a-z][a-z0-9_]+',                      'IDENTIFIER'),
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
VISIBLE 1bird
"HAI"
"KTHXBYE"
KTHXBYE""")

    try:
        for tok in lx.tokens():
            print(tok)
    except LexerError as err:
        print('LexerError at position %s' % err.pos)
