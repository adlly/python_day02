def method1():
    print(num)

def method2():
    method1()

def method3():
    try:
        method2()
    except:
        print("异常")

method3()