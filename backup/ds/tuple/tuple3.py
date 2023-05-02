users =((1,"raj"),(2,"ram"),(3,"ravi"))

for i in users:
    for j in i:
        print(j)
        

students = ([1,"parth"],[2,"jay"],[3,"prit"])

students[0][1]="PARTH"

for i in students:
    print(i)
    
employees =[(101,"rahul",1234.50),(102,"raj",1234.50),(103,"ram",1234.50)]

cities = ("ahmedbad","surat","baroda","rajkot","mumbai","pune","delhi")
print(cities)
cityList = list(cities)
cityList.extend(["chennai","kolkata"])
print(cityList)

cities = tuple(cityList)
print(cities)
    