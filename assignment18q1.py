n = int(input("Enter number of elements: "))
lst = []

for i in range(n):
    lst.append(int(input()))

total = sum(lst)
print("Addition:", total)
