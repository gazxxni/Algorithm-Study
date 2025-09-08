n = int(input()) 

result = 0
a = 1  

while n > 0:

    if n % 2 == 1:
        result += a
        
    a *= 3
    n //= 2

print(result)
