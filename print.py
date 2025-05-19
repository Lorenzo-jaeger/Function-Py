# function 1
# Print

product = "iphone"
units = 200

print("the product", product, "has", units, "units in stock.", sep="/")

import time

print("counter:")
for i in range(5):
    print(5 - i, end="\r")
    time.sleep(1)
print("he finished")
