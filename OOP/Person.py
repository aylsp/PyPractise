# coding:utf-8

class Person(object):
    CATEGORY = 'Person'
    DESC = 'I am a person'

    def __init__(self, country):
        # print 'call the method __init__'
        self.country = country

    # def __new__(cls, *args, **kwargs):
    #     print 'call the method __new__'

    def say_hello(self):
        print 'hello ' + self.DESC + '\n'

    @classmethod
    def say_hello_V1(cls):
        print 'hello ' + cls.DESC + '\n'

    @staticmethod
    def say_hello_V2():
        print 'hello ' + '\n'
