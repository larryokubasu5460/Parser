from .symbol_table import SymbolTable


class ParseError(Exception):
    def __init__(self, message=""):
        self.message=f"ParseError: {message}"

class Parser:
    def __init__(self,tokens:list):
        self.position=0 
        self.tokens=tokens
        self.current=self.tokens[self.position][0]

    def advance(self):
        if self.position < len(self.tokens):
            self.position +=1
            self.current=self.tokens[self.position][0]
        else:
            self.current="EOF"
    
    def peek(self):
        if self.position < len(self.tokens):
            return self.tokens[self.position+1]
        else:
            raise ParseError(f"Reached EOF")

    def parse(self):
        # self.tokens=tokens
        # self.position=0
        # self.current=self.tokens[self.position]
    
        if ((self.current !=  '#') and (self.current != 'int')):
            raise ParseError(f"Mising # or int at position {self.position}.")
        else:
            print("Parsing begins")
            return self.parse_program()

    def parse_puts(self):
        self.advance()
        # print("Parsing puts")
        # print(self.current)
        if self.current=="(":
            self.advance()
            self.advance()
            self.advance()

            # print(self.current)
            # print(self.peek())

   
        else:
            raise ParseError(f"Wrong argument in puts {self.current}")  

    def parse_arithmetics5(self):
        self.advance()
        print("Expression parsed")
        # print("In arithmetic 5", self.current)
        self.advance()
    
    def parse_arithmetics4(self):
        if self.current==";":
            return
        print("Parsing arithmetic 4")
        self.advance()
        # print("In arithmetic 4",self.current)
        if ((self.current=="*") or (self.current=="/")):
            print("Multiplication")
            self.parse_arithmetics5()
            self.parse_arithmetics4()
            
        else:
            return

    def parse_arithmetics3(self):
        if self.current==";":
            return
        print("Parsing arithmetic 3")
        self.advance()
        if ((self.peek()[1]=="NUM") or (self.peek()[1]=="ID")):
            # print("In arithmetic 3 ",self.current)
            self.advance()
            self.parse_arithmetics4()
        else:
            return
             
# E->TE'
# E'->+TE'|e
# T->FT'
# T'->*FT'|e
# F->(E)|id      
 
    def parse_arithmetics2(self):
        if self.current==";":
            return
        # print("Parsing arithmetics 2")
        self.advance()
        if((self.current=="+") or (self.current=="-")):
            # print("In arithmetic 2 ",self.current)
            self.advance()
            self.parse_arithmetics3()
            self.parse_arithmetics2()
            print(self.current)
            print(self.peek())
        else:
            return

    def parse_arithmetics1(self):
        if ((self.peek()[1]=="ID") or (self.peek()[1]=="NUM")):
            # print("Parsing arithmetic 1")
            self.advance() #number
            # print("In arithmetic 1", self.current)
            self.parse_arithmetics3()
            self.parse_arithmetics2()
        else:
            return
 
    def parse_arithmetics(self):
        # self.advance()
        print("Parsing arithmetics...")
        # print(self.current)
        SymbolTable.add_symbol(self.current)
        self.advance() #=
        # print("Symbol",self.current)
        self.parse_arithmetics1()
        # self.inside_while()
         

    def inside_while(self):
        print("Parsing while")
        # print(self.current)
        if (self.current)=="puts":
            self.parse_puts()
            self.advance()

        if self.peek()[1]=="ASSIGN":
            # print(self.current)
            # print("Parsing arithmetic")
            self.parse_arithmetics()
            self.advance()

        if self.peek()[1]=="(IN|DE)CREMENT":
            self.advance()
            self.advance()
            self.advance()
            print("Out of while")
            
            # print(self.current)
        if self.current!="}":
            print("Not done with while")
            # print(self.current)
            self.inside_while()
        else:
            return
       
    
    def parse_statements(self):
        self.advance()
        # print(self.current)
                    
        # if statement list is while
        if self.current=='while':
            print("Parsing arguments of while")
            self.advance()
            if self.current=="(":
                if self.peek()[1]== "ID" :
                   
                    self.advance()
                    
                    if self.peek()[1]=="RELATIONAL OP":
                    
                        self.advance()
                        if ((self.peek()[1]=='ID')or(self.peek()[1]=="NUM")):
        
                            self.advance()
                            self.advance()
                            self.advance()
                            if self.current=="{":
                                # parse inside while
                                self.advance()
                                self.inside_while()
                                self.advance()
                            else:
                                raise ParseError(f"Unexpected argument in while loop {self.current}")
                        else:
                            raise ParseError(f"Unexpected argument in while loop {self.current}")
                    else:
                        raise ParseError(f"Unexpected argument in while loop {self.current}")
                elif self.peek()[0] in ['int','float']:
                    self.advance()
                    if self.peek()[1]=="ID":
                        self.advance()
                    if self.peek()[1]=="RELATIONAL OP":
                        self.advance()
                        if ((self.peek()[1]=='ID') or (self.peek()[1] == "NUM")):
                            self.advance()
                            self.advance()
                            if self.current=="{":
                                # parse inside while
                                self.advance()
                                self.inside_while()
                                self.advance()

                        
        elif self.current=="puts":
            self.parse_puts()
        else:
            print("body is empty")
                
    
    def parse_exit(self):
        print("Before exit", self.current)
        if self.current=='return':
            if self.peek()[1]=="NUM":
                self.advance()
                self.advance()
                self.advance()
                if self.current=="}":
                    print("Parse complete with exit keyword")
            else:
                self.advance()
                self.advance()
                print("Parsing complete")
        else:
            print("Parsing complete with no exit keyword")
            

    def parse_assignment(self):
        print("Variable", self.current)
        if self.peek()[1]=='ASSIGN':
            # declaration with assignment
            name=self.current
            self.advance()
            self.advance()
            value=self.current
            SymbolTable.add_symbol(name,value)
            print("Parsed assignment succesffuly")
            self.advance()
            if self.peek()[0] in ['int','float']:
                self.advance()
                self.advance()
                self.parse_assignment()
            else:
                self.parse_statements()
        else:
            # declaration with no assignment
            self.name=self.current
            SymbolTable.add_symbol(self.name)
            print("Parsed assignment without declaration")
            self.advance()
            if self.peek()[0] in ['int','float']:
                self.advance()
                self.advance()
                self.parse_assignment()
            else:
                self.parse_statements()
            


    def main_body2(self):
        print("Parse variables and statement list")
        # print("Current token", self.current)
        self.advance()
        if ((self.current == 'int') or (self.current=='float') and (self.peek()[1]=="ID")): 
            if ((self.current=='int') or (self.current=='float')):
                # call assignment function  
                self.advance()
                self.parse_assignment()
                self.parse_exit()
            print("Done parsing body")
        

    
    def include(self):
        while True:
            if (self.current== '#'):
                self.advance()
                if self.current=='include':
                    print("Matched Include")
                    self.advance()
                    if self.current =='<':
                        print("Matched <")
                        self.advance()
                        if self.tokens[self.position][1]=='HEADERFILE':
                            print("Matched header")
                            self.advance()
                            if self.current==">":
                                print("Matched closing >")
                                self.advance()
                                continue
                            else:
                                raise ParseError(f"Wrong header file details at {self.position}")
                        raise ParseError(f"Missing closing > at {self.position}")
                    raise ParseError(f"Missing headerfile at {self.position}")
                raise ParseError(f"Missing include at {self.position}")
            else:
                print("Done parsing header")  
                break               
        
    
    def main_body(self):
        print("Starting to parse body")
        if (self.current=="int") and (self.peek()[0]=='main'):
            while self.tokens[self.position][1] == 'KEYWORD':
                self.advance()
            if self.current=="(":
                self.advance()
                self.advance()
                if self.current == "{":
                    print("Parsing Inside parenthesis") 
                    self.main_body2() 
        else:
            raise ParseError(f"Missing main function at position {self.position}")          


    def parse_program(self):
        self.include()
        self.main_body()