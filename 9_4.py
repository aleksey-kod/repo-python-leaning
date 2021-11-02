class Car:
    def __init__(self,speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Поехали')
    def stop(self):
        print(f'Остановились')
    def turn(self,direction):
        print(f'{self.name} Повернули на {direction}')
    def show_speed(self):
        return f'{self.name} Текущая скорость {self.speed}'

class TownCar(Car):
    def show_speed(self):
        msg=super().show_speed()
        if self.speed > 60:
            msg=f'{msg} !! Превышение лимита в 60 !!'
        return msg
class SportCar(Car):
    """"""


class WorkCar(Car):
    def show_speed(self):
        msg=super().show_speed()
        if self.speed > 40:
            msg=f'{msg} !! Превышение лимита в 40 !!'
        return msg

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police=True)


police_one=PoliceCar(100,'red','Копы')
police_one.turn('Налево')
print(police_one.show_speed())
work_one=WorkCar(70,'blue','Дальнобойщик')
print(work_one.show_speed())
town_one=TownCar(90,'black','Такси')
print(town_one.show_speed())

