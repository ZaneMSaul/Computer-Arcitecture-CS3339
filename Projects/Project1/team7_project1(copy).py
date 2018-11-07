import sys
import os

opcodeStr = []  # <type 'list'>: ['Invalid Instruction', 'ADDI', 'SW', 'Invalid Instruction', 'LW', 'BLTZ', 'SLL',...]
validStr= [] #<type 'list'>: ['N', 'Y', 'Y', 'N', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'Y',...]
instrSpaced = [] # <type 'list'>: ['0 01000 00000 00001 00000 00000 001010', '1 01000 00000 00001 00000 00000 001010',...]
arg1 = [] # <type 'list'>: [0, 0, 0, 0, 0, 1, 1, 10, 10, 0, 3, 4, 152, 4, 10, 1, 0, 112, 0] 
arg2 = [] # <type 'list'>: [0, 1, 1, 0, 1, 0, 10, 3, 4, 5, 0, 5, 0, 5, 6, 1, 1, 0, 0] 
arg3 = [] # <type 'list'>: [0, 10, 264, 0, 264, 48, 2, 172, 216, 260, 8, 6, 0, 6, 172, -1, 264, 0, 0] 
arg1Str = [] # <type 'list'>: ['', '\tR1', '\tR1', '', '\tR1', '\tR1', '\tR10', '\tR3', '\tR4', .....] 
arg2Str = [] # <type 'list'>: ['', ', R0', ', 264', '', ', 264', ', #48', ', R1', ', 172', ', 216', ...]' 
arg3Str = [] # <type 'list'>: ['', ', #10', '(R0)', '', '(R0)', '', ', #2', '(R10)', '(R10)', '(R0)',...] 
mem = [] # <type 'list'>: [-1, -2, -3, 1, 2, 3, 0, 0, 5, -5, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0] 
binMem = [] # <type 'list'>: ['11111111111111111111111111111111', '11111111111111111111111111111110', ...] 
valid = [] 
opcode = []

if __name__ == "__main__":    # execute only if run as a script    main()

class TestMe:
    #def __init__(self):
    def run(self): 
        global opcodeStr 
        global validStr 
        global arg1 
        global arg2 
        global arg3 
        global arg1Str 
        global arg2Str 
        global arg3Str 
        global mem 
        global binMem 
        global valid 
        global opcode

for i in range(len(sys.argv)): 
    if (sys.argv[i] == '-i' and i < (len(sys.argv) - 1)): 
        inputFileName = sys.argv[i + 1] 
    print inputFileName 
    elif (sys.argv[i] == '-o' and i < (len(sys.argv) - 1)): 
        outputFileName = sys.argv[i + 1]


