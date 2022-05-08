import re

expression = "A = B * C + D / E - F"

qr, t = [], []

def quad(symbol):
    global expression
    
    if symbol == "=":
        index = expression.index(symbol)
    
        return [str(len(qr)), symbol, expression[index-2], expression[index+1:index+3]]
        
    
    index = expression.index(symbol)
    
    result = [len(qr), symbol, expression[index-3:index-1], expression[index+1:index+3]]
    
    t.append("T"+str(len(qr))+' = '+ expression[index-3:index+3])
    expression = expression.replace(expression[index-3:index+3], "T"+str(len(qr)))
    print(expression)
    
    return result

qr.append(quad('*'))
  
qr.append(quad('/'))
  
qr.append(quad('+'))
  
qr.append(quad('-'))
  
qr.append(quad('='))
for i in t:
    print(i)
    
print("Quadruple Representation of 3AC :\nPosition   Operator    Operand1    Operand2")
for i in qr:
    print(f"{i[0]} \t {i[1]} \t {i[2]} \t {i[3]}".expandtabs(13))
