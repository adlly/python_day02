#单例模式，这个类创建出的对象只有一个（占用一份内存地址）
#合理的使用内存（避免内存浪费）

# num = None
# if not num:
#     print("ceshi")


class Person(object):
    __instance = None

    __is_First = True

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
            print("创建对象")
        return cls.__instance

    def __init__(self,name,age):
        if self.__is_First:
            self.name=name
            self.age=age
            print(self.name,self.age)
            self.__is_First=False





xiaoming = Person("xiaoming",20)
xiaohong = Person("xiaohong",21)
xiaopang = Person("xiaopang",22)
print(xiaoming,xiaohong,xiaopang)
print(xiaoming.name,xiaohong.name,xiaopang.name)

