def CheckNumber(num):
    if num > 0 :
        print("Possitive Number")
    elif num < 0 :
        print("Nagatve Number") 
    else :
        print("Zero")

n = int(input("Enter the number :"))
CheckNumber(n)