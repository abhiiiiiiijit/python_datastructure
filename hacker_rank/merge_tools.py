def merge_the_tools(string, k):
    # your code goes her
    lst = []
    for i in range(0,len(string),k):
        lst.append(string[i:i+k])
        
    for e in lst:
        set_e = set(e)

        print(''.join(set_e))
        

    
    
