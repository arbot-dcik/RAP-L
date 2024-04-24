# UTF-8
# Personalize your RAP

######################################### LEXER #########################################

LETTER = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd',
          'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm',
          'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D',
          'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M',
          '_']

NUMBER = ['0', '1', '2', '3', '4',
          '5', '6', '7', '8', '9']

OPERATOR = ['(', ')', '=', '+', '-', '*', '/', ',']

TOKEN_NEXTLINE = 'nextline'
TOKEN_NUMBER = 'number'
TOKEN_STRING = 'string'
TOKEN_NAME = 'name'
TOKEN_OPERATOR = 'operator'
TOKEN_END = 'end'

ERROR_BASEERROR_ID = -1
ERROR_SYNTAXERR_ID = 1
#ERROR_SYNTAXERR_ID = 1
#ERROR_SYNTAXERR_ID = 1
#ERROR_SYNTAXERR_ID = 1
#ERROR_SYNTAXERR_ID = 1

END_CHAR = '!'

######################################### PASER #########################################

######################################### SAFE #########################################

NORMAL_ID = 0

ERROR_NAME_TO_ID = {'baseErr':ERROR_BASEERROR_ID,'SyntaxErr':ERROR_SYNTAXERR_ID}

DEFAULT_ENM = 'err'

DEFAULT_EMG = 'err'

######################################### OTHER #########################################
