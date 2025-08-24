import random
n=random.randint(1,100)
a=-1
guess=1
while(a!=n):
    a=int(input("enter number : "))
    if(a>n):
        print("enter smaller !!!")
        guess+=1
    elif(a<n):
        print("enter higher !!!")
        guess+=1
print("you guessed", n ,"in", guess ,"guesses")