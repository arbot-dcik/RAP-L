#
# var string = "Hello World!"
# var number = 100
# print(string,number)
# ===========================
# Hello World!
# 100

from define import *
def lexer(text):
    text += END_CHAR
    tokens = []
    t_len = len(text) - 1
    current_char = ''
    index = -1

    while index < t_len:
        index += 1
        current_char = text[index]
        
        if current_char in '\n':
            tokens.append({'type':TOKEN_NEXTLINE,'value':current_char})
        elif current_char in ' ':
            pass
        elif current_char in '"' + "'":
            value = ''
            index += 1
            current_char = text[index]
            while current_char not in '"' + "'":
                value += current_char
                if index + 1 > t_len:
                    break
                index += 1
                current_char = text[index]
            tokens.append({'type':TOKEN_STRING,'value':value})
                
        elif current_char in LETTER:
            value = ''
            while current_char in LETTER + NUMBER and current_char != '\n':
                value += current_char
                if index + 1 > t_len:
                    break
                index += 1
                current_char = text[index]
            index -= 1
            tokens.append({'type':TOKEN_NAME,'value':value})
            
        elif current_char in NUMBER:
            value = ''
            dot = False
            while current_char in NUMBER + ['.'] and current_char != '\n':
                if index + 1 > t_len:
                    index += 2
                    break
                if dot and current_char == '.':
                    return [],ERROR_SYNTAXERR_ID #####ERROR RETURN
                if current_char == '.':
                    dot = True
                value += current_char
                index += 1
                current_char = text[index]
            index -= 1 #字符撤回
            tokens.append({'type':TOKEN_NUMBER,value:value})
            
        elif current_char in OPERATOR and current_char != '\n':
            tokens.append({'type':TOKEN_OPERATOR,'value':current_char})
        elif current_char in [END_CHAR] and index == t_len:
            tokens.append({'type':TOKEN_END,'value':current_char})
        else:
            print('ERROR')
    
    return tokens,0

if __name__ == '__main__':
    t,c = lexer("1.1.")
    for i in t:
        print(i)
