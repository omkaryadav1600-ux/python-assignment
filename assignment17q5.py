def CheckPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = 5
if CheckPrime(num):
    print("It is Prime Number")
else:
    print("It is Not Prime Number")
