#Forked from https://gist.github.com/eliben/5797351
import re
import sys


class Token(object):
    """ A simple Token structure.
        Contains the token type, value and position.
    """

    def __init__(self, type, val, pos):
        self.type = type
        self.val = val
        self.pos = pos

    def __str__(self):
        return '%s(%s) at %s' % (self.type, self.val, self.pos)


class LexerError(Exception):
    """ Lexer error exception.
        pos:
            Position in the input line where the error occurred.
    """

    def __init__(self, pos):
        self.pos = pos


class Lexer(object):
    """ A simple regex-based lexer/tokenizer.
        See below for an example of usage.
    """

    def __init__(self, rules, skip_whitespace=True):
        """ Create a lexer.
            rules:
                A list of rules. Each rule is a `regex, type`
                pair, where `regex` is the regular expression used
                to recognize the token and `type` is the type
                of the token to return when it's recognized.
            skip_whitespace:
                If True, whitespace (\s+) will be skipped and not
                reported by the lexer. Otherwise, you have to
                specify your rules for whitespace, or it will be
                flagged as an error.
        """
        # All the regexes are concatenated into a single one
        # with named groups. Since the group names must be valid
        # Python identifiers, but the token types used by the
        # user are arbitrary strings, we auto-generate the group
        # names and map them to token types.
        #
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
        """ Initialize the lexer with a buffer as input.
        """
        self.buf = buf
        self.pos = 0

    def token(self):
        """ Return the next token (a Token object) found in the
            input buffer. None is returned if the end of the
            buffer was reached.
            In case of a lexing error (the current chunk of the
            buffer matches no rule), a LexerError is raised with
            the position of the error.
        """
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

            #Do regex search. This is the only codeblock needed
            m = self.regex.match(self.buf, self.pos)
            if m:
                #Get the group that was matched
                groupname = m.lastgroup
                #Get the type of the token using the groupname
                tok_type = self.group_type[groupname]
                #Get the current token using the groupname. The actual token is in m.group(groupname)
                tok = Token(tok_type, m.group(groupname), self.pos)
                #Update the position
                self.pos = m.end()
                return tok

            # if we're here, no rule matched
            # We can replace this one or outright remove it
            raise LexerError(self.pos)

    def tokens(self):
        """ Returns an iterator to the tokens found in the buffer.
        """
        #Get all tokens
        while 1:
            tok = self.token()
            if tok is None:
                break
            yield tok


if __name__ == '__main__':
    rules = [
        # litereal
        ('\".*\"',             'YARN'),
        ('TROOF|NOOB|NUMBR|NUMBAR|YARN|TYPE', 'TYPE'),
        ('WIN|FAIL',           'TROOF'),
        ('-?\d+.\d+',          'NUMBAR'),
        ('0|-?[1-9][0-9]*',    'NUMBR'),
        # keywords
        ('IF\sU\sSAY\sSO', 'IF U SAY SO'),
        ('IM\sOUTTA\sYR', 'IM OUTTA YR'),
        ('QUOSHUNT\sOF', 'QUOSHUNT OF'),
        ('PRODUKT\sOF', 'PRODUKT OF'),
        ('BOTH\sSAEM', 'BOTH SAEM'),
        ('EITHER\sOF', 'EITHER OF'),
        ('HOW\sIZ\sI', 'HOW IZ I'),
        ('IM\sIN\sYR', 'IM IN YR'),
        ('IS\sNOW\sA', 'IS NOW A'),
        ('SMALLR\sOF', 'SMALLR OF'),
        ('BIGGR\sOF', 'BIGGR OF'),
        ('I\sHAS\sA', 'I HAS A'),
        ('BOTH\sOF', 'BOTH OF'),
        ('DIFF\sOF', 'DIFF OF'),
        ('DIFFRINT', 'DIFFRINT'),
        ('O\sRLY\?', 'O RLY?'),
        ('ALL\sOF', 'ALL OF'),
        ('ANY\sOF', 'ANY OF'),
        ('KTHXBYE', 'KTHXBYE'),
        ('MOD\sOF', 'MOD OF'),
        ('NO\sWAI', 'NO WAI'),
        ('SUM\sOF', 'SUM OF'),
        ('VISIBLE', 'VISIBLE'),
        ('WON\sOF', 'WON OF'),
        ('YA\sRLY', 'YA RLY'),
        ('GIMMEH', 'GIMMEH'),
        ('NERFIN', 'NERFIN'),
        ('OMGWTF', 'OMGWTF'),
        ('SMOOSH', 'SMOOSH'),
        ('FOUND', 'FOUND'),
        ('I\sIZ', 'I IZ'),
        ('MEBBE', 'MEBBE'),
        ('UPPIN', 'UPPIN'),
        ('WTF\?', 'WTF?'),
        ('GTFO', 'GTFO'),
        ('MAEK', 'MAEK'),
        ('MKAY', 'MKAY'),
        ('OBTW', 'OBTW'),
        ('TLDR', 'TLDR'),
        ('WILE', 'WILE'),
        ('BTW', 'BTW'),
        ('HAI', 'HAI'),
        ('ITZ', 'ITZ'),
        ('NOT', 'NOT'),
        ('OIC', 'OIC'),
        ('OMG', 'OMG'),
        ('TIL', 'TIL'),
        ('AN', 'AN'),
        ('YR', 'YR'),
        ('A', 'A'),
        ('R', 'R'),
        #  identifier
        ('[a-z][a-z0-9_]+',    'IDENTIFIER'),

    ]

    lx = Lexer(rules, skip_whitespace=True)
    lx.input("""
    HAI 1.2
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
    KTHXBYE
    """)

    try:
        for tok in lx.tokens():
            print(tok)
    except LexerError as err:
        print('LexerError at position %s' % err.pos)
