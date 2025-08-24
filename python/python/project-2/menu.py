while(1):
    print("press 1 for area of circle")
    print("press 2 for area of rectangle")
    print("press 3 for area of triangle")
    print("press 4 for exit")
    choice = int(input("enter your choice: "))
    if (choice == 1):
        r = float(input("enter radius of circle: "))
        area = 3.14 * r * r
        print("area of circle is: ", area)
    elif (choice == 2):
        l = float(input("enter length of rectangle: "))
        b = float(input("enter breadth of rectangle: "))
        area = l * b
        print("area of rectangle is: ", area)
    elif (choice == 3):
        b = float(input("enter base of triangle: "))
        h = float(input("enter height of triangle: "))
        area = 1/2 * b * h
        print("area of triangle is: ", area)
    else:
        print("exiting...")
        break