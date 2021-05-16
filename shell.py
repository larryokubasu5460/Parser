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
        print("Mini Tree\n",repr(P.tree))
    
    except KeyboardInterrupt:
        exit()


