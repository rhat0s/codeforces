# A. Team

n = int(input())
count = 0

for x in range(n):
    p = input().split(" ")
    tempcount = 0
    if int(p[0]) + int(p[1]) + int(p[2]) >= 2:
        count+=1
print(count)

