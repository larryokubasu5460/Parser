
# class CodeGenerator:
#     def __init__(self):
#         self.data=None

# {'x': '0', 'z': 0, 'm': ['m', '=', '90', '*', '87'], 'y': ['y', '=', '90', '+', '8'], 'while': ['(', 'x', '<', '10'], 'puts': ['(', 'x', ')'], 'x++': ['x', '++']}
def CodeGenerator(object):
    # loop over dictionary
    for key,value in object.items():
        # print(key,len(str(value)))
        if (len(str(value))>1 and len(str(value))<3) and ('=' not in value):
            print(("ASSIGN", str(key), str(value)))
        if len(str(value))>3:
            for x in value:
                if '=' in value:
                    print(("ADD", str(key), str(value[2:])))
                    break
        if key=='while':
            print(("Label", "L1"))
            for x in value:
                if '<' in value:
                    print(("Lt","t1",str(value[:-2]),str(value[:-1])))
                    break
            print(("NOT","t2","t1"))
            print(("IF", "t2","L2"))
            print(("GOTO","L1"))
            print(("Label","L2"))

        
        
            
        


