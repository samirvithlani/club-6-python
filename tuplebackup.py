# list dynamic array --> [] --> list specfic add last data add ,, specfic data remove, last remove....
#@data manupulation -->
#tuple --> immutable--> no modification --> no add, no remove, no update ()

userData = ("amit","raj","parth","jay","amit")
print(userData)

cnt = userData.count("amit")
print(userData[0])
#userData[0] = "amita" #error..
print(cnt)

ind = userData.index("parth")
print(ind)


tup1 = (1,2)
tup2 = (3,4)

#tup1[0] = 11
#tup1= tup1 + ["amit","raj"]
print(tup1)