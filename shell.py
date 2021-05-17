from tokenizer import tokenizer
from mini_parser import Parser,SymbolTable
from icg import CodeGenerator as cg

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
        # print("Mini Tree\n",repr(P.tree))
        # print("SymbolTable\n",SymbolTable.symbols)
        print("code generator")
        cg(SymbolTable.symbols)
    
    except KeyboardInterrupt:
        exit()


