# function 3
# range


# list = list(range(5))
# list = list(range(1,6))
# list = list(range(1,20,2))
list = list(range(5,0,-1))
print(list)

import time

print("counter:")
for i in range(5):
    print(5 - i, end="\r")
    # print(i,end="\n" )
    time.sleep(1)
print("he finished")