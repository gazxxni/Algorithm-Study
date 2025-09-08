import sys
input = sys.stdin.readline

n = int(input().strip())
dic = {1: 1}

for i in range(2, n + 1):
    n_dic = {i: 0 for i in range(1, 21)}
    
    for year, cnt in dic.items():
        age = i - year

        if year % 2 == 1:
            death_age = 3
        else:
            death_age = 4

        n_dic[i] += cnt

        if age < death_age:
            n_dic[year] += cnt

    dic = n_dic

print(sum(dic.values()))
