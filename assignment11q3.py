no = int(input("enter the number :"))
sum = 0


while no > 0:
    sum += no % 10
    no //= 10

print("sum od digits:", sum)