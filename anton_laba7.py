import random
num = 20
arr = [0]*num
even = 0
odd = 0
negative = 0
positive = 0


for i in range(num):
    arr[i] = int(random.randrange(-100, 100))
for i in arr:
    if int(i) % 2 ==0:
        even += 1
    else:
        odd += 1
for i in arr:
    if int(i) >= 0:
        positive += 1
    else:
        negative += 1
print("Array:", arr)
print("Even numbers: %.d, and odd numbers: %.d" % (even, odd)) # Even - четные, Odd - не четные
print("Positive numbers: %.d, and Negative numbers: %.d" % (positive, negative)) # Positive - положительные, Negative - отрицательные
