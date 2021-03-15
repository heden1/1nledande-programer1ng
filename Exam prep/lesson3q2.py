def encrypt(text):
    text=text.split()
    dict1={}
    i=0
    encryption=[]
    
    for word in text:
        if word not in dict1.values():
            dict1[i]=word
            i=i+1
            
    # list out keys and values separately
        key_list = list(dict1.keys())
        val_list = list(dict1.values())
# print key with val 100
        position = val_list.index(word)
        encryption.append(key_list[position])
        #cryption.append(dict1[word])
    print(dict1)
    print(encryption)
        
        



encrypt("the tree was used to make the tree blocks")
#should return the pair:([0,1,2,3,4,5,0,1,6],{0: "the", 1: "tree", 2:"was",3:"used", ...})
#You can assume that all words in the sentence areseparated by space
#,which makes it possible to separate them by usingsplit().