def pepLineLength(filename):
    file1=open(filename)
    text=file1.readlines()
    file1.close()
    longLines=0
    for i in range(text):
        if len(text[i])>79:
            print("line " + str(i) + " too long: "+str(len(text[i])
            longLines=longLines+1                                      
    print(str(longLines)+" lines are too long")