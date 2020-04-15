# try:
#     open("hm.txt","r")
#     print(num)
# except (FileNotFoundError,NameError):
    # print("异常了")



#e用来存储异常信息描述
# try:
#     open("hm.txt","r")
#     print(num)
# except (FileNotFoundError,NameError) as e:
#     print(e)


#捕获所有异常:Exception 它是所有异常的父类


try:
    open("hm.txt","r")
except Exception as e:
    print("捕获异常",e)