for i in range(int(input())): #int() has been added
        word = input()
        word = word.upper() # indendation chaged from here
        vowels = ['A','E','I','O','U']
        count = 0 #== has been changed to =
        for j in range(1,len(word)) :#colon has been added and funtion has been changed
                if word[j] in vowels:#sqaure brackets removed 
                        if j == 0: 
                                count = count+1 #++ not supported
                        elif word[j+1] in vowels: #sqaure brackets removed 
                                count = count #break has been removed
                        else:
                                count = count+1 #++ not supported
        print (count)
