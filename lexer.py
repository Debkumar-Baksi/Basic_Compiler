
#RUN FIRST

token_types=[
    ['NUMBER','0123456789'],
    ['PLUS','+'],
    ['MINUS','-'],
    ['MULTIPLY','*'],
    ['DIVIDE','/'],
    ['LPAREN','('],
    ['RPAREN',')'],
    ['WHITESPACE',' \t\n']
]
# print(token_types[0][1])

def lexer(input_string):
    descripted_tokens=[]
    tokens=[]
    position = 0
    input_length=len(input_string)

    while position < input_length:
        char=input_string[position]

        #whitespaces
        if char in token_types[7][1]:
            position+=1
            continue

        #number
        if char in token_types[0][1]:
            value=''
            while position < input_length and input_string[position] in token_types[0][1]:
                value+=input_string[position]
                position+=1
            descripted_tokens.append(('NUMBER',value))
            tokens.append(value)
            continue

        #other
        token_found=False
        for token_type , token_chars in token_types[1:7]:
            if char == token_chars:
                descripted_tokens.append((token_type,char))
                tokens.append(char)
                position +=1
                token_found=True
                break

        #noToken
        if not token_found:
            raise SyntaxError(f"Unexpected Character: {char}")
        
    return descripted_tokens,tokens



#file input
def read_input(file_input):
    with open (file_input , 'r') as file:
        content = file.read()
    return content

input_file="input.txt"
input_text=read_input(input_file)



descripted_tokens , tokens =lexer(input_text)
# for token in tokens:
print(descripted_tokens)
print(tokens)

