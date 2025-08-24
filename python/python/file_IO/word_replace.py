word="horse"
with open("D:\\python\\file_IO\\donkey.txt") as f:
    content=f.read()
    con=content.replace(word,"donkey")
with open("D:\\python\\file_IO\\donkey.txt","w") as f:
    f.write(con)