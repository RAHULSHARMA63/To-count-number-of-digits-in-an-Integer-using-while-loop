num = 4672
count = 0

while num != 0:
    num //= 10
    count += 1

print("Number of digits: " + str(count))