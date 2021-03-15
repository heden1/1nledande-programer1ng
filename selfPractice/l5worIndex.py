def word_index(text):
    dict ={}
    if len(text)==0:
        return dict
    text=text.split(' ')
    for i in range(len(text)):
        list1=[i]
        if text[i] in dict:
            list1=dict.get(text[i])
            list1.append(i)
            
        dict[text[i]]= dict.get(text[i],list1)        
    return(dict)
            
        
        
        

        
    
    





print(word_index('the spider indexes the spider web') )
print(word_index('')) 
#{'the': [0,3],'spider': [1,4], 'indexes': [2], 'web': [5]}