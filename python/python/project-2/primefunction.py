def prime():
    print("enter the number that u want to check if it is prime or not")
    n = int(input("enter number : "))
    if n<= 1:
        print("not prime") 
    else:
        for i in range(2,n):
            if n % i == 0:
                print("number is not prime")
                break
            else:
                print(n, "is prime")
                break
while(1):
    prime()