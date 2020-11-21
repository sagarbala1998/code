def maxdist(s):
    n=len(s)
    if n<2: return n
    
    distinct=set(s)  
    distinct_len=len(distinct)
    
    mi=n+1
 
    a={}
    st=0; itr=1
    a[s[st]]=1
    while itr<n:
 
        if s[itr] in a: a[s[itr]]+=1
 
        else: a[s[itr]]=1
 
        if len(a)==distinct_len:
 
            while st<itr and a[s[st]]>1:
                a[s[st]]-=1
                st+=1
            if mi>itr+1-st: mi=itr+1-st
        itr+=1
 
    print(mi)
 
    
s=str(input())
maxdist(s)