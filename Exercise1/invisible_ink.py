import sys
import binaryconv as bc

#encode functions
def txt2bin(txt):
    bin = []
    for c in txt:
        bin.append(bc.padzero(bc.dec2bin(ord(c)),8))
    return "".join(bin)

def bin2invisible(bin):
    inv = []
    for b in bin:
        if b=='0':
            inv.append(' ')
        else:
            inv.append('\t')
    return "".join(inv)

def txt2invisible(txt):
    return bin2invisible(txt2bin(txt))





#decode functions
def invisible2bin(inv): #create binnary numbers from "space" (=0) and other characthers like "\t" (=1)
    bin = []
    for d in inv:
        if d==' ':
            bin.append('0')
        else:
            bin.append('1')
    return "".join(bin)

def bin2txt(bin):
    txt=[]
    for e in range (0,len(bin),8): #divides the binary numbers to groups of 8
        txt.append(chr(bc.bin2dec(bin[e:e+8])))
    return "".join(txt)

def invisible2txt(inv):
    return bin2txt(invisible2bin(inv))




# main function
def main():

    if sys.argv[1]=="decode": #decode
        #opens and reads file and takes away the \n (newline)
        file = open(sys.argv[2])
        line = file.read().replace("\n", " ")
        file.close()
        
        print(invisible2txt(line))#prints the secret message
        
    elif sys.argv[1]=="encode": #encode the file <sys.argv[2]>
        file = open(sys.argv[2])
        line = file.read().replace("\n", " ")
        file.close()

        if len(sys.argv)== 4: #Check if length of sys.argv input is 4 then takes sys.argv[3] as a output file to print the decoded message
            file2 = open(sys.argv[3],"w")#checks for file named the same as sys.argv[3] if not crates a new file. Then writes over the text with new text
            file2.write(txt2invisible(line))
            file2.close()
            print("Printed in file",sys.argv[3])

        else:
            print(txt2invisible(line))
            


    else:
        print("Wrong input. Input: python invisible_ink.py <encode or decode> <my-file-name> ")

main()


