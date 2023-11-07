#["amit","raj1","neha111","parth"]
def isSpace(n):
    for i in n:
        if " " in i:
            return True
    
    return False
    


data = ["ram sita","lakshaman"," love kush","amit"]

x = list(filter(lambda x : isSpace(x),data))
print(x)    