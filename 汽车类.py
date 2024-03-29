# 1. 小米汽车刚发布，小强准备去购买一辆车：
# 请为汽车设计类
# 汽车的一些属性
# 汽车的一些方法
class TestCar:
    def __init__(self):
        self.name = '小米汽车'
        self.color = '黑色'
        self.price = 10000
        self.num = 5

    def buy(self):
        self.num = self.num - 1
        print(f'{self.name}卖出了{self.num}辆')

    def sell(self):
        self.num = self.num - 1
        print(f'{self.name}卖出了{self.num}辆')
    def show(self):
        print(self.name, self.color, self.price)

# 请为用户设计类
# 用户属性
class TestUser:
    def __init__(self):
        self.name = '小强'
        self.age = 18
        self.sex = '男'
        self.money = 10000
# 用户方法
    def buy(self, car):
        if self.money >= car.price:
            self.money = self.money - car.price
            car.buy()
            print(f'{self.name}购买了{car.name}')
        else:
            print(f'{self.name}没有足够的钱购买{car.name}')

    def sell(self, car):
        if car.num > 0:
            self.money = self.money + car.price
            car.sell()
            print(f'{self.name}买了一辆{car.name}')
        else:
            print(f'{self.name}没有{car.name}可以卖')

    def show(self):
        print(self.name, self.age, self.sex, self.money)


car = TestCar()
user = TestUser()
user.buy(car)
user.sell(car)
user.show()
car.show()

