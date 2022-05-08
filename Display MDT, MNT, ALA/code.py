sample_asm = open('Sample.asm Exp 4.txt', 'r')

MDT, MNT, ALA = [], {}, {}
index_MDT, index_MNT, index_ALA, flag = 0, 0, 0, 0

# Pass 1
for line in sample_asm:
    word = line.split()
    if word[0] == 'MACRO':
        MNT[word[1]] = index_MNT
        index_MNT += 1
        
        ALA[word[2]] = index_ALA
        index_ALA += 1
        
        flag = 1
    
    if word[0] == 'ENDM':
        MDT.append([str(index_MDT), word])
        index_MDT += 1
        flag = 0
    
    if flag:
        if word[0] != 'MACRO':
            MDT.append([str(index_MDT), word])
            index_MDT += 1

print("Contents of Macro-Definition Table are :\nIndex \t Macro-Definition")
for i in MDT:
    print(f"{i[0]} \t {' '.join(i[1])}".expandtabs(8))
    
print("\n\nContents of Macro-Name Table are :\nIndex \t Macro-Name")
for key in MNT:
    print(f"{MNT[key]} \t {key}".expandtabs(8))

print("\n\nContents of Argument List Array are :\nIndex \t Parameter")
for key in ALA:
    print(f"{ALA[key]} \t {key}".expandtabs(8))
