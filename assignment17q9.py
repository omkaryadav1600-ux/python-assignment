def CountDigits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

print(CountDigits(5187934))
