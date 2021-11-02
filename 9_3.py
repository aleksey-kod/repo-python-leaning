class Worker:
    def __init__(self,name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}
class Position(Worker):
    def get_full_name(self):
        return self.name+' '+self.surname

    def get_total_income(self):
        return self._income.get("wage")+self._income.get("bonus")

bibl=Position('Иван','Иванович','Библиотекарь',50000,10000)
print(bibl.get_full_name())
print(bibl.get_total_income())
сook=Position('Петр','Сергеевич','Повар',45000,20000)
print(сook.get_full_name())
print(сook.get_total_income())
