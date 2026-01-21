no = int(input("entre the number :"))
count = 0

while no > 0 :
    count += 1
    no //= 10

print("count of digits :", count)