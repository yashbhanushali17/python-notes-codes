def gentable(n):
    table=""
    for i in range(1,11):
        table+=f"{n} X {i} = {n*i}\n"
    with open(f"D:\\python\\file_IO\\tables/table_{n}","w") as f:
        f.write(table)

for i in range(1,25):
    gentable(i)