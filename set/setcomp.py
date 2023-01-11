users = {"raj","jay","neha","priya","hr","ranbir","malayalam"}
users1 = set()

# for u in users:
#     if len(u) > 4 and (u.startswith("p") or u.startswith("r")):
#         users1.add(u)
        

# print("user1....",users1)

# {print(u.upper()) for u in users if len(u) > 4}
users1 = {u for u in users if len(u) > 4 and (u.startswith("p") or u.startswith("r"))}
print(users1)