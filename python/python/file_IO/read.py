# f = open("D:\\python\\file_IO\\file.txt")
#"r" use when  u want to read file but its not necessery to write r becoz r is already given while opening file 
#read function
    # data=f.read()
    # print(data)

#readline function
# data = f.readline()
# while(data !=""):
#     print(data)
#     data=f.readline()
# f.close()

#read file with "with" statement
with open("D:\\python\\file_IO\\file.txt") as f:
    print(f.read())