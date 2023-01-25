def avg(*nos):
    avg =0
    sum =0
    for i in nos:
        #rint(i)
        sum = sum + i
        #print(avg)
    avg = sum // len(nos)   
        
    return avg;    

average = avg(15,15,20,45,8)
print(average)
    
        