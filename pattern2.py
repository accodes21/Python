
import time
for x in range(0,6):
    n=1
    for y in range(0,x+1):
        print(n, end="")
        n+=1
        time.sleep(0.02)
    print("\r")
    
for x in range(5,0,-1):
    for y in range(1,x+1):
        print(y, end="")
        time.sleep(0.02)
    print("\r")