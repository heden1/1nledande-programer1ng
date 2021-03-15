def translate(expr,src,dst):
    
    #create list from file 
    file1=open("translation.txt")
    text=file1.readlines()
    file1.close()
    list1=[]
    totalList=[]
    for line in text:
        line=line.strip("\n")
        if line.split(":")==['']:
            totalList.append(list1)
            list1=[]
        else:
            list1.append(line.split(": "))
    totalList.append(list1)
    
    #find expr word in list
    find=False
    for word in range(len(totalList)):
        for expression in (totalList[word]):
            if str(expression[1])==expr: #could also use "and expression[0]==src" but not needed
                find=True
                break
        if find:
            break
        
    
    #get the translation
    if find:
        for trans in totalList[word]:
            if trans[0]==dst:
                return trans[1]
            
    return None
    
print(translate("jordgubb", "swe", "fre"))