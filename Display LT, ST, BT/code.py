sample_asm = [["JOHN", "START", ""],
              ["", "USING", "*,15"],
              ['', "LOAD", "1,FIVE"],
              ['', "ADD", "1,FOUR"],
              ['', "STORE", "1,TEMP"],
              ["FIVE", "DC", "F'5'"],
              ["FOUR", "DC", "F'4'"],
              ['TEMP', 'DS', "1'F'"],
              ['', 'END', '']]

pseudo_opcode = ['START', 'USING', 'DC', 'DS', 'END']

MOT, POT, ST, LT = [], [], [], []

location_counter = 0

# Pass 1
for i in sample_asm:
    if i[1] not in ['START', 'USING']:
        location_counter += 4
    i.append(location_counter)
        
    # Determining Mnemonic Opcode Table
    if i[1] not in pseudo_opcode:
        mnuemonic = i[1]
        length = '10'
        instrn_format = '001'
        
        MOT.append([mnuemonic, length, instrn_format])
    
    # Determining Psedo Opcode Table
    else:
        pseudo = i[1]
        routine_address = '-'*3
        
        POT.append([pseudo, routine_address])
    
    # Determining Symbol Table
    if i[0] != '':
        symbol = i[0]
        location = i[3]
        length = 1 if i[2]=='' else 4
        relocation = 'R'
        
        ST.append([symbol, location, length, relocation])
    
    
    if "'" in i[2]:
        ltr = i[2]
        location = i[3]
        length = 4
        relocation = 'R'
        
        LT.append([ltr, location, length, relocation])

// print("Contents of Mnemonic Opcode Table are : \nMnemonic  Length  Instruction Format")
// for i in MOT:
//    print(f"{i[0]} \t\t {i[1]} \t\t {i[2]}".expandtabs(4))
    
    
// print("\nContents of Psedo Opcode Table are : \nPseudo-Opcode  Routine Address")
// for i in POT:
//    print(f"{i[0]} \t\t {i[1]}".expandtabs(8))
    
    
print("\nContents of Symbol Table are : \nSymbol \t\t Location \t Length \tRelocation".expandtabs(2))
for i in ST:
    print(f"{i[0]} \t\t {i[1]} \t\t {i[2]} \t\t {i[3]}".expandtabs(5))
    
    
print("\nContents of Literal Table are : \nLiteral \t Value \t\t Length \t Relocation".expandtabs(2))
for i in LT:
    print(f"{i[0]} \t\t {i[1]} \t\t {i[2]} \t\t {i[3]}".expandtabs(4))


BT = []

reg_op = sample_asm[1][2]
using_r, register = int(reg_op[2:]), 1
# Pass 2
for i in range(using_r+1):
    availability = 'Y' if i==using_r else 'N'
    value = '-' if availability=='N' else  0
    
    BT.append([i, availability, value])
    

print('The contents of Base Table are : \nRegister  Availability  Value')
for i in BT:
    print(f"{i[0]} \t\t {i[1]} \t\t {i[2]}".expandtabs(6))
