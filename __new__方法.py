class Person(object):


    #使用其类创建对象，并返回对象给 __init__
    def __new__(cls, *args, **kwargs):
        print("__new__")
        return object.__new__(cls)


    #监听类的实例化完成，给对象赋值
    def __init__(self):
        print("__init__")

        self.name="xiaoming"

    #监听对象的值的变化
    def __str__(self):
        return self.name


    #监听对象的销毁
    def __del__(self):
        print("bye")


xiaoming = Person()
xiaoming.name
