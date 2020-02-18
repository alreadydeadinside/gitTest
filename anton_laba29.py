def gcb (k1, k2):
    if k2 != 0:
        if k1 > k2:
            return gcb(k2, k1 % k2)
        elif k1 < k2:
            return gcb(k1, k2 % k1)
    return k1


k1 = int(input("Enter your first nubmer: "))
k2 = int(input("Enter your second nubmer: "))

print("Your greatest common factor:", gcb(k1, k2))
