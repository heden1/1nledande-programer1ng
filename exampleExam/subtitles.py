def loadSubRip(filename):
    
    #create list from file 
    file1=open(filename)
    text=file1.readlines()
    file1.close()

    script=[]
    total=""
    for line in text:
        if ":" in line and line.startswith("0"):
            #print(line)
            line=line.strip("\n")
            line=line.split("-->")
            time=tuple(line)
        elif line[0].isalpha():
            line=line.strip("\n")
            script.append(line)
        elif line =='\n' :
            total=total+ "\n" +str(time) + str(script)
            script=[]
            #print (total)
    tupl=(total,str(time) , str(script))
    print(tupl)        
    return (total+ "\n"+str(time) + str(script))


#print(loadSubRip("subtitles.txt"))

def loadSubRip2(filename):
    
    #create list from file 
    file1=open(filename)
    text=file1.readlines()
    file1.close()

    
    i=0
    subtitles=[]
    
    while i<len(text):
        #print (text[i].split())
        i=i+1
        fields=text[i].split()
        i=i+1
        rows=[]
        while i<len(text) and text[i]!="\n":
            rows.append(text[i].strip("\n"))
            i=i+1
        i=i+1
        subtitles.append((fields[0],fields[2],rows))
    return subtitles


print(loadSubRip2("subtitles.txt"))