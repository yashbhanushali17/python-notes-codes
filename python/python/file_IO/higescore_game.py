# import random
# def game():
#     print("you are playing game : ")
#     score =random.randint(1,100)
#     with open("D:\\python\\file_IO\\hiscore.txt") as f:
#         hiscore=f.read()
#         if(hiscore!=""):
#             hiscore=int(hiscore)
#         else:
#             hiscore=0
#     print("your score is :",hiscore)
#     if(score>hiscore):
#         with open("D:\\python\\file_IO\\hiscore.txt","w") as f:
#             f.write(str(score))
#     return score
# game()
import random   
def game():
    print("you are playing a game : ")
    score=random.randint(1,100)
    with open("D:\\python\\file_IO\\hiscore.txt") as f: 
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    print("your score is : ",hiscore)
    with open("D:\\python\\file_IO\\hiscore.txt","w") as f: 
        if(score>hiscore):
            f.write(str(score))
    return score
game()
 