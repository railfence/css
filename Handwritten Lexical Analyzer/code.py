import keyword
import re

operators = [':', '&', '|', '!', ';', '+', '-', '=', '%', '==', '!=']

program_keyword = set()
program_operator = set()
identifier = set()
#invalid_identifier = set()

program = open('Lexical Code.txt', 'r')

for line in program:
    token_list = re.split(' ', line)
    
    if token_list[0] == '#':
        pass
    
    else:
        for token in token_list:
            if token=='\n':
                pass
            
            elif token in keyword.kwlist:
                program_keyword.add(token)
                
            elif token in operators:
                program_operator.add(token)
                
            elif token.isalpha():
                identifier.add(token)
            
            

print("--Program to design lexical analyzer--")

print("\nKeywords in the program are :")
print(*program_keyword, sep=', ')

print("\nValid Identifiers in the program are :")
print(*identifier, sep=', ')

print("\nOpertors in the program are :")
print(*program_operator, sep=', ')
