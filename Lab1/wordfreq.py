import operator #for sorted on line 53
import random #for random on line 37

frequencies= {} #create dictonary
stopWordsDict={}#create dictonary


#creats list from the lines and separate each word from each other
def tokenize(lines): 

    words = [] #creats empty list
    for line in lines:
        start = 0
        while start < len(line):
            blank= " "
            if start+1 < len(line) and charCheck(line[start])==charCheck(line[start+1]): #if the character and the next character ar of the same type  for example letter and letter or number and number
                start=start+1
                
            else:
                line=line[:start+1]+blank+line[start+1:] #adds a blank space bettween the two characters who are of a diffrent type ex letter and nummber
                start=start+2 #adds 2 becouse we just added a blankspace and whants to move to teh character after the space
                
        line = line.lower()
        line= line.split()       
        words.extend(line) #add the line of separated words to the list 
    return words

#checks if the character is letter, number, space or somthing else (used in tokenize())
def charCheck(char): 
    if char.isalpha():
        return "alpha"
    elif char.isdigit():
        return "digit"  
    elif char.isspace():
        return "space"
    else: 
        return random.random()



#takes away the words that are equal in documents from  stopWords and words
def countWords(words,stopWords):
    frequencies= {}  
    for i in range (len(words)):
        if words[i] not in stopWords:
            frequencies[words[i]]= frequencies.get(words[i],0)+1
    return frequencies


#prints the (n) most used words from frequencies 
def printTopMost(frequencies,n): 
    i=0
    frequencies=dict(sorted(frequencies.items(), key=lambda x: x[1], reverse=True)) #sorts the dictonary from big to small
    for word,freq in frequencies.items():
        if i>=n:
            break
        i=i+1
        print(word.ljust(23),freq)
    return (frequencies) #sorted
