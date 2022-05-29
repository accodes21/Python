
import time
n = int(input("Enter number of terms:"))
f = 0
s = 1
sum = 0

if n == 1:
    print(f)
else:
    print(f)
    print(s)
    for i in range(2,n):
        sum = f+s
        f = s
        s = sum
        time.sleep(0.5)
        print(sum)
    