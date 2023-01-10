#list [] allow duplicate stores in index manner as well mutable...
#tuple () allow duplicate stores in index manner and not mutable...
#dictionary {} allow duplicate calues but not key stores in key value manner and mutable...
#set {}  not allow duplicate stores and mutable... set is unordered collection of unique elements

email = {"raj","jay","raj","neha","shruti","amit"}
print(email)

email.add("raja")
email.add("jaya")
print(email)

email.remove("jaya")
print(email)

email.update(["meet","meeta","priya"])
print(email)

#removedelem =email.pop()
#print(removedelem)

email.discard("abc")
print(email)

#set   --> remove -->  print --> discard --> update --> add --> pop





