import time
for i in range(10, 0, -1):
    j = 1
    str = ""
    for j in range(j,i,1):
        str = "*"*j
    print(i,str)

    time.sleep(1)

print("BLAST OFF")