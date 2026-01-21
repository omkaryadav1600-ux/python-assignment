no = int(input("enter the number:"))
temp = no 
rev = 0

while no > 0:
    rev = rev * 10 + no % 10
    no //= 10

    if temp == rev:
        print("palindrome")
    else:
        print("Not Palindrome")    
  