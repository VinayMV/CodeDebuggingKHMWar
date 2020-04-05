def function(bookscoresarray,no_ofdays,signupdays,noofbooksperday,libbooksarray)
    a=bookscores
    li=[] 
    for i in range(len(a)): 
        li.append([a[i],i]) 
    li.sort() 
    b = [] 
    for x in reversed(li): 
        b.append(x[1]) 

    n=no_ofdays
    p=signupdays
    q=n-p
    k=noofbooksperday

    r=[]
    e=0
    c=libbooks

    d=[]
    for i in b:
        if i in c:
            d.append(i);


    for i in range (0,q):
        for j in range(0,k):
            if(e!=q):
                r.append(d[e])
                e+=1

    print(r)
