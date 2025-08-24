import random
'''
1 for snake
-1 for water 
0 for gun

rules

snake win against water
gun win against snake
water win against gun
'''

computer=random.choice([-1,0,1])
youstr=input("enter your choice : ")
youdicts={"s":1,"w":-1,"g":0}
revdict={1:"snake",-1:"water",0:"gun"}
you=youdicts[youstr]
print("you enter : ",revdict[you])
print("computer enter : ",revdict[computer])
if(computer==you):
    print("its a draw")
else:
    # if(computer==1 and you==-1):  (computer- you)=>2
    #     print("computer won")    
    # elif(computer==1 and you==0): (computer- you)=>1
    #     print("you won")         
    # elif(computer==-1 and you==1):(computer- you)=>-2
    #     print("you won")         
    # elif(computer==-1 and you==0):(computer- you)=>-1
    #     print("computer won")    
    # elif(computer==0 and you==1): (computer- you)=>-1
    #     print("computer won")     
    # elif(computer==0 and you==-1):(computer- you)=>1
    #     print("you won")
    # else:
    #     print("something went wrong")
    if((computer-you)==-1 or (computer-you==2)):
        print("computer won ")
    else:
        print("you won")