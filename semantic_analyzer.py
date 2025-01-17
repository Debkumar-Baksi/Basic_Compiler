#RUN THIRD

from parser import ast , NumberNode , BinOpNode , Parser

class SemanticAnalyzer:
    def __init__(self):
        self.errors=[]
    
    def analyze(self,node):
        self.visit(node)
        if self.errors:
            for error in self.errors:
                print(f"Semantic Error: {error}")
            return False
        return True
    
    def visit(self,node):
        method_name=f"visit_{type(node).__name__}"
        visitor=getattr(self, method_name , self.generic_visit)
        return visitor(node)
    
    def generic_visit(self,node):
        raise Exception(f"No visit method for {type(node).__name__}")
    
    def visit_NumberNode(self,node):
        pass

    def visit_BinOpNode(self,node):
        self.visit(node.left)
        self.visit(node.right)


analyzer=SemanticAnalyzer()
result=ast.evaluate()
if analyzer.analyze(ast):
    print("Semantic Analysis Passed")
    print(f"Result: {result}")
else:
    print("Semantic Analysis Failed")
