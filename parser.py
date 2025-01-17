#RUN SECOND

from lexer import token_types , tokens , descripted_tokens 

class NumberNode:
    def __init__(self,value):
        self.value=value

    def __repr__(self):
        return f"Number({self.value})"
    
    def evaluate(self):
        return self.value
    
class BinOpNode:
    def __init__(self , left , op , right):
        self.left=left
        self.op=op
        self.right=right

    def __repr__(self):
        return f"BinOp ( {self.left} , {self.op} , {self.right} )"
    
    def evaluate(self):
        left_value=self.left.evaluate()
        right_value=self.right.evaluate()

        if self.op=='+':
            return left_value+right_value
        elif self.op=='-':
            return left_value-right_value
        elif self.op=='*':
            return left_value*right_value
        elif self.op=='/':
            return left_value/right_value
        else:
            raise ValueError(f"Unknown Operator : {self.op}")


class Parser:
    def __init__(self , descripted_tokens):
        self.descripted_tokens=descripted_tokens
        self.current_token=None
        self.token_index=-1
        self.advance() #initialize
    
    def advance(self):
        #move to next token
        self.token_index+=1
        if self.token_index < len(self.descripted_tokens) :
            self.current_token=self.descripted_tokens[self.token_index]
        else:
            self.current_token=None
        
    def parse(self):
        #start parsing
        ast=self.expr()
        # result=self.expr()
        if self.current_token is not None:
            raise SyntaxError("Unexpected token at end of Input")
        return ast
    
    def expr(self):
        #parse addition and subtraction
        result=self.term()
        while self.current_token is not None and self.current_token[0] in ('PLUS' , 'MINUS'):
            if self.current_token[0] == 'PLUS':
                self.advance()
                result=BinOpNode(result , '+' , self.term())
                # result+=self.term()
            elif self.current_token[0] == 'MINUS' :
                self.advance()
                result=BinOpNode(result , '-' , self.term())
                # result-=self.term()
        return result
    
    def term(self):
        result=self.factor()
        while self.current_token is not None and self.current_token[0] in ('MULTIPLY' , 'DIVIDE'):
            if self.current_token[0] == 'MULTIPLY':
                self.advance()
                result=BinOpNode(result , '*' , self.factor())
                # result*=self.factor()
            elif self.current_token[0] == 'DIVIDE' :
                self.advance()
                result=BinOpNode(result , '/' , self.factor())
                # result/=self.factor()
        return result

    def factor(self):
        if self.current_token is None:
            raise SyntaxError("Unexpected end of input")
        
        if self.current_token[0] == 'NUMBER':
            value=int(self.current_token[1])
            self.advance()
            return NumberNode(value)
        elif self.current_token[0] == 'LPAREN':
            self.advance()
            result=self.expr()
            if self.current_token is None or self.current_token[0] !='RPAREN':
                raise SyntaxError("Expected Closing Parenthesis")
            self.advance()
            return result
        else:
            raise SyntaxError(f"Unexpected Token: {self.current_token[1]}")



parser=Parser(descripted_tokens)
ast=parser.parse()
print(f"AST : {ast}")
