import sys
input = sys.stdin.readline

a = list(input().rstrip())
r = 10 ** 9 + 7
data = [1] * n

for i in range(1, n):
	data[i] = (data[i - 1] * 2) % r
	
ans = 0

for i in range(n):
	if a[i] == 'O':
    	ans = (ans + data[i]) % r
		
print(ans)




# a = input()
# cnt = 0

# while True:

#     if not 'O' in a:
#         break


#     for i in range(len(a)):
#         if a[i] == 'O':
#             a[i] = 'X'
#             cnt += 1

#             for j in range(i):
#                 if a[j] == 'O':
#                     a[j] = 'X'
                    
                


    
    