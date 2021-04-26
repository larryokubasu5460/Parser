from tokenizer import tokenizer
from mini_parser import mini_parser

while(True):
    try:
        f_p=input(">>Enter file name: ")
        inp=open(f_p)
        file=inp.read()
        # print(file)

        tokens=tokenizer(file)
        print("Tokens: ", tokens)

    except KeyboardInterrupt:
        exit()