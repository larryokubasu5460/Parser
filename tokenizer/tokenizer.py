import re

# keywordsRegex = "^int$|^double$|^float$|^while$|^include$|^main$|^for$|^if$|^return$|^scanf$|^printf$|^%d$"
# headerfileRegex = "^[A-Za-z\.]+"
# numbersRegex = "^[+-]*\d+\.?\d*$"
# arithmeticOp = "[\+\-\/\*\++\--]"
# relationalOpRegex = "<|<=|>=|>|!=|==|!"
# assignmentOp = "^=$"
# newlineChar="^\n$"
# specialsymbols="\#|\(|\)|\{|\}|\:|\;|\,|\%|\"|\&|\[|\]"
# identifierRegex = "^[a-zA-Z_][a-zA-Z0-9]*$"

def tokenizer(string:str):
    token_rexes=[
        (re.compile(r"^for|^include|^while|^main|^for|^if^|^return|^int|^double|^puts|^printf|^%d"),"KEYWORD"),
        (re.compile(r"^\+\+|^\-\-"),"(IN|DE)CREMENT"),
        (re.compile(r"^[0-9]+\.?[0-9]*"),"NUM"),
        (re.compile(r"^[A-Za-z]+\.[A-Za-z]+"),"HEADERFILE"),
        (re.compile(r"^[A-Za-z_][A-Za-z0-9_]*"),"ID"),
       
        (re.compile(r"^\n"),"NEWLINE"),
        (re.compile(r"^[+*/-]"),"ARITHMETIC OP"),
        (re.compile(r"^<=|^>=|^<|^>|^\!\=|^\=\=|^\+\="),"RELATIONAL OP"),
        (re.compile(r"^="),"ASSIGN"),
        (re.compile(r"^[\(\)\;\,\"\"\.\#\&\%\{\}]"),"SPECIAL SYMBOL"),
        (re.compile(r"[-+]?\d+"),"D"),
  
      

    ]
    tokens=[]
# tk=RegexpTokenizer("[\w\.\w.*]+|\d+\.?\d*|<=|>=|>|!=|!|\++|--|<|==|[^ ]|[A-Za-z\[\d+|\w\]]+")
# input_tokens=tk.tokenize(file)
# print(input_tokens)
    while len(string):
        string=string.lstrip()
        matched=False
        for token_rex,token_type in token_rexes:
            mo=token_rex.match(string)
            if mo:
                matched=True
                token=(mo.group(0),token_type)
                tokens.append(token)
                string=token_rex.sub('',string)
                string=string.lstrip()
                break  #break out of the inner loop
        if not matched:
            raise Exception("Invalid string")
    return tokens

