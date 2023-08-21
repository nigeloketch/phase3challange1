
def twoNumbers (a, b, c):

    positive_count = 0
    
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1
    
    return positive_count == 2

print(twoNumbers(2, 4, -3))  
print(twoNumbers(-4, 6, 8))  
print(twoNumbers(4, -6, 9))  
print(twoNumbers(-4, 6, 0))  
print(twoNumbers(4, 6, 10))  
print(twoNumbers(-14, -3, -4))  

