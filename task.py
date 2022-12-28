users = ["a","raj","ram","naman","lol","madam"]
palindrome = []

for i in users:
    if i == i[::-1]:
        palindrome.append(i)

        
palindrometuple = tuple(palindrome)
print(palindrometuple)        

