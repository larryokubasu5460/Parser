from tokenizer import tokenizer
from mini_parser import Parser

while(True):
    try:
        f_p=input(">>Enter file name: ")
        inp=open(f_p)
        file=inp.read()
        # print(file)

        tokens=tokenizer(file)
        print("Tokens: ", tokens)
        P=Parser(tokens)
        P.parse()
    
    except KeyboardInterrupt:
        exit()






























    # print(P.current)
    # P.advance()
    # print(P.current)
    # P.advance()
    # print(P.current)
    # print("Peek", P.peek())
    # P.advance()
    # print(P.current)