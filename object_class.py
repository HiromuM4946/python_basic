class Person(object):

    # コンストラクタ
    def __init__(self, name: str):
        self.name = name
    
    def say_something(self):
        self.run(10)
        print('I am {}. hello'.format(self.name))

    def run(self, num):
        print('run' * num)
    
    # デストラクタ
    def __del__(self):
        print('good bye')

# if __name__ == '__main__':
#     person = Person('Mike')
#     person.say_something()

#     print('############')

class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='model S', enable_auto_run=False, passwd='123'):
        # オーバーライド
        super().__init__(model)
        self._enable_auto_run = enable_auto_run
        self.passwd = passwd

    # プロパティを使って、値の書き換えをできなくする
    @property
    def enable_auto_run(self):
        return self._enable_auto_run
    
    # setterで値の書き換えができるようにする
    # psswdなどといった条件を使って、書き換えできるようにする
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '456':
            self._enable_auto_run = is_enable
        else:
            raise ValueError

    def run(self):
        print('super fast')
    def auto_run(self):
        print('auto run')

# tesla_car = TeslaCar('Model S', passwd='456')
# tesla_car.enable_auto_run = True
# print(tesla_car.enable_auto_run)

class Person_v2(object):
    def __init__(self, age=1):
        self.age = age
    def drive(self):
        if self.age >= 18:
            print('ok')
        else:
            raise Exception('No drive')

class Baby(Person_v2):
    def __init__(self, age=1):
        if age < 18:
            super().__init__(age)
        else:
            raise ValueError

class Adult(Person_v2):
    def __init__(self, age=18):
        if age >= 18:
            super().__init__(age)
        else:
            raise ValueError

baby = Baby()
adult = Adult()

class Car_v2(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')
    def ride(self, person):
        person.drive()

car_v2 = Car_v2()
# car_v2.ride(baby)
# car_v2.ride(adult)


# クラスメソッドとスタティックメソッド
class Person_v3(object):

    kind = 'human'

    def __init__(self):
        self.x = 100
    
    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

    @staticmethod
    def about(year):
        print('about human {}'.format(year))

# print(Person_v3.kind)
# print(Person_v3.what_is_your_kind())

# Person_v3.about(1999)


# 特殊メソッド
class Word(object):
    def __init__(self, text: str):
        self.text = text

    def __str__(self):
        return 'Word!!!!'

    def __len__(self):
        return len(self.text)
    
    def __add__(self, word):
        return self.text.lower() + word.text.lower()

# w = Word('test')
# w2 = Word('#############')

# print(w + w2)