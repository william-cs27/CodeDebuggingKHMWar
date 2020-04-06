


for i in range(int(input())): 
        word = str(input())
        word.upper() 
        vowels = ['A','E','I','O','U']
        count=0
        for j in range(1,len(word)) :  #length() to len() and ":" is placed to make the synatx of for loop correct
            
            if (word[j] in vowels) : 
                count=count+1               #incrementing in classic method
                if (word[j] in vowels) and (word[j+1] in vowels):
                    if word[j-1] in vowels:
                        count=count-1
                
                    
            
                #else:
                    #count=count+1 
        print (count) 