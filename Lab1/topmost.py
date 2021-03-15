from wordfreq import * #imports the functions from wordfreq.py
import sys
import urllib.request



#exampel inputs
#python3 topmost.py eng_stopwords.txt examples/article1.txt 20
#python3 topmost.py eng_stopwords.txt https://en.wikipedia.org/wiki/Whale_shark 20
#python3 topmost.py examples/article3.txt  examples/article2.txt 10                          #what words article 2 use but not in article 3
#...

def main(stopWords,file,n):



    #reading
    file1 = open(stopWords,encoding="utf-8")
    stopWords=file1.read()
    file1.close()
    stopWords=stopWords.strip("\n")

    #checks if file is a URL or not 
    if file.startswith("http://") or file.startswith("https://")  :
        response = urllib.request.urlopen(file)
        contentList = response.read().decode("utf8").splitlines()
    else:
        file2 = open(file,encoding="utf-8")
        contentList=file2.readlines()
        file2.close()  
            
        
    #claculate and prints   
    (printTopMost(countWords(tokenize(contentList),stopWords),n))

main(sys.argv[1],sys.argv[2],int(sys.argv[3]))