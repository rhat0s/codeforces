n,k = input().split()
a = input().split(" ",int(n))
a.sort(key=int, reverse=True)
count = 0
for num in a:
    if(int(num) >= int(a[int(k)-1]) and int(num) != 0):
            count+=1
print(count)
