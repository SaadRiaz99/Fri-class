import pymysql
myq = pymysql.connect(host="localhost", user="root", password="24022007@")

mtcur = myq.cursor()

mtcur.execute("show databases")
for i in mtcur:
    print(i)
print("abe bhai run ho gia")