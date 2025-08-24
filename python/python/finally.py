def final():
    try:
        a=int(input("enter number"))
        print(a)
        return
    except Exception as e:
        print(e)
        return
        # print("finally use in function and it will run no matter if function terminated in try or catch with return statement!!!")
    finally:
        print("finally use in function and it will run no matter if function terminated in try or catch with return statement!!!")
final()
#while if u will use only print statement it will give error