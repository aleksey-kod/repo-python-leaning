class Stationery:
    def __init__(self,title="Название"):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Pen (Stationery):
    def draw(self):
        print(f'Сейчас пишет шариковая {self.title}')
class Pencil(Stationery):
    def draw(self):
        print(f'Сейчас пишем тонким {self.title}')
class Handle(Stationery):
    def draw(self):
        print(f'Сейчас пишет толстый {self.title}')

pen = Pen('ручка')
pencil = Pencil('карандашом')
handle = Handle('маркер')
pen.draw()
pencil.draw()
handle.draw()
