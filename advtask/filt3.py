def containsAlphaAndDigit(n):
    # has_alpha = any(char.isalpha() for char in n)
    # has_digit = any(char.isdigit() for char in n)
    # return has_alpha and has_digit
    has_alpha = False
    has_digit = False
    
    for char in n:
        if char.isalpha():
            has_alpha = True
            break
    
    for char in n:
        if char.isdigit():
            has_digit = True
            break
    
    return has_alpha and has_digit    
                
    
    

data = ["ram sita", "lakshaman", " love kush", "amit", "raj1", "neha111", "parth", "123"]
filtered_data = list(filter(containsAlphaAndDigit, data))
print(filtered_data)
