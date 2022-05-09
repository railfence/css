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

print(sample_asm)
