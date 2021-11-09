import re
class Warehouse():
    def __init__(self):
        self.Equipment = {}
    def add_equip(self,*equip_in):
        for eq in equip_in:
            self.Equipment[eq.inventory_label]=eq
    def __str__(self):
        msg = f'                          Warehouse\n    ' \
              f'Name       |  Location     | Inventory |           Notes       |\n{"-"*70}\n'
        for eq in self.Equipment:
            msg = f'{msg} {self.Equipment[eq]}\n'
        return msg

    def change_location(self,inventory_label,new_location):
        eq = self.find_eg_str(inventory_label)
        msg = f'{"-"*70}\nChange location for {eq.name} label {eq.inventory_label}\nOld Statement\n{eq}'
        eq.location = new_location
        msg = f'{msg}\nNew Statement\n{eq}\n{"-"*70}\n'
        return msg

    def find_eg_str(self,inventory_label):
        return self.Equipment[inventory_label]

class Equipment():
    def __init__(self,name,location,inventory_label):
        self.name = name
        self.location = location
        self.inventory_label = inventory_label
    def __str__(self):
        return f' {self.name:<13}|  {self.location:<13}|{self.inventory_label:<11}|'
    @staticmethod
    def valid_ip(ip_str):
        re_ip=re.compile(r'^\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}',re.IGNORECASE)
        if re_ip.match(ip_str) or str(ip_str).upper() == 'NOT CONNECT' :
            return True
        else:
            return False


class Copier(Equipment):
    def __init__(self, name, location, inventory_label, ip):
        super().__init__(name, location, inventory_label)
        if Equipment.valid_ip(ip):
            self.ip = ip
        else:
            raise ValueError("Ip not valid")

    def __str__(self):
        return f'{super().__str__()}   Ip={self.ip:<17}|'

class Printer(Equipment):
    def __init__(self,name,location,inventory_label,ip):
        super().__init__(name,location,inventory_label)
        if Equipment.valid_ip(ip):
            self.ip = ip
        else:
            raise ValueError("Ip not valid")
    def __str__(self):
        return f'{super().__str__()}   Ip={self.ip:<17}|'

class Scaner(Equipment):
    def __init__(self,name, location, inventory_label,format):
        super().__init__(name, location, inventory_label)
        self.format = format
    def __str__(self):
        return f'{super().__str__()}   Format={self.format:<13}|'

list_eg=[Printer('Samsung P300','warehouse','123456','not connect'),
        Copier('Xerox','Office_2FL','345234','192.168.1.2'),
        Scaner('Canon','Office_2FL','987655','A4'),
        Scaner('Canon','Office_3FL','786567','A4'),
        Printer('Samsung P500','warehouse','234543','not connect')
         ]

warehouse = Warehouse()
warehouse.add_equip(*list_eg)
try:
    warehouse.add_equip(Printer('Samsung P300','Office_3FL','678544','1924.168.1.4'))
except ValueError as err:
    print(err)
print(warehouse)
print(warehouse.change_location('123456','Office_2FL'))

