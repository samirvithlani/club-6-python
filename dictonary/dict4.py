class1 = ["a","b","c"]
class2 = ["d","e","f"]

school = {"c1":class1,"c2":class2}
#class2 new student to be added..
#class2 = school.get("c2")
#class2.append("g")
school.get("c2").append("g")
school.get("c1").pop()



for i,j in school.items():
    #i c1 j class1
    
    #list
    for stu in j:
        #stu a
        #stu b
        #stu c
        print(stu,end=" ")
    
    print()    

    