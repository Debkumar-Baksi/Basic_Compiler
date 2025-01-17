#RUN FOURTH

from parser import ast

class Three_Address_Code_Generator :
    def __init__(self):
        self.temp_counter=0
        self.code=[]

    def generate(self,node):
        self.visit(node)
        return self.code
    
    def visit(self,node):
        method_name=f"visit_{type(node).__name__}"
        visitor = getattr(self , method_name , self.generic_visit)
        return visitor(node)
    
    def generic_visit(self,node):
        raise Exception(f"No visit method for {type(node).__name__}")
    
    def visit_NumberNode(self,node):
        return node.value
    
    def visit_BinOpNode(self,node):
        left_value=self.visit(node.left)
        right_value=self.visit(node.right)

        temp_var=self.new_temp()
        self.code.append(f"{temp_var} = {left_value} {node.op} {right_value}")
        
        return temp_var

    def new_temp(self):
        self.temp_counter+=1
        return f"t{self.temp_counter}"
    


tac_generator=Three_Address_Code_Generator()
tac_code=tac_generator.generate(ast)
for instruction in tac_code:
    print(instruction)