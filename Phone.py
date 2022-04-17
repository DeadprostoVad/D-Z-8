"""
Создать класс Phone, у которого будут следующие атрибуты:
Определить атрибуты:
- brand - бренд
- model - модель
- issue_year - год выпуска
Определить методы:
- инициализатор __init__
- receive_call, который принимает имя звонящего и выводит на экран: Звонит {name}
- get_info, который будет возвращать кортеж (brand, model, issue_year)
- метод __str__, который выводит на экран информацию об устройстве:
Бренд: {}
Модель: {}
Год выпуска: {}
"""
class Phone:
    brand: str
    model: str
    issue_year: str

    def __init__(self, brand, model, issue_year):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    def __str__(self):
        self.get_info()
        return ""

    def get_info(self):
        print(f"Бренд - {self.brand} \n"
              f"Модель - {self.model} \n"
              f"Год выпуска - {self.issue_year}")
        return ""

    def receive_call(self, name):
        self.name = name
        print(f"Звонит {self.name}")
        return " "

class Phones:
    def __init(self, l ):
        self.phones = l
    def __getitem__(self, item):
        return self.l[item]
l =  (Phone("Poco", "M3_Pro_5G", 2021), Phone('Honor', '8X', 2018), Phone('Xiaomi', 'Redmi_Note_8_Pro', 2020), Phone('Huawei', 'Y5', 2015))

str(l[2])

