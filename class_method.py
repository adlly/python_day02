class Person(object):
    __country="china"


    #定义类方法,对私有类属性取值赋值使用
    #修饰器
    @classmethod
    def get_country(cls):
        return cls.__country

    @classmethod
    def set_country(cls,name):
        cls.__country=name

    #定义静态类方法，一般不用

    @staticmethod
    def get_what():
        return ("哈哈哈哈")




print(Person.get_country())

Person.set_country("india")

print(Person.get_country())

print(Person.get_what())