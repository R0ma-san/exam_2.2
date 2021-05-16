#Позсчет траны компании на зарплату персонала и самого продуктивного и непродуктивного работника
class ProductivityandSalary():
    
    productivity = {}
    expenses = []
    
    def max_productivity(self):
        x = max(self.productivity, key=self.productivity.get)
        print(f'Самый продуктивный: {x} - {self.productivity[x]} %')
    
    def min_productivity(self):
        y = min(self.productivity, key=self.productivity.get)
        print(f'Самый непродуктивный: {y} - {self.productivity[y]} %')


class Manager(ProductivityandSalary):
    
    
    def __init__(self, name, salary, hours, number):
        self.name = name
        self.salary = salary
        self.hours = hours
        self.number = number
      
    #Подсчет общей зарплаты менеджера
    def calculation_of_total_salary(self):
        self.total_salary = self.salary
        print(f"id: {sel.number}, name: {self.name}, salary:{self.total_salary}")
        super().expenses.append(self.total_salary)

    #Вывод продуктивности менеджера
    def productivity(self):
        pr = self.hours/40*100
        print(f'{self.name} productivity - {pr} %')
        super().productivity[self.name] = pr

class Secretary(ProductivityandSalary):
    
    
    def __init__(self, name, salary, hours, number):
        self.name = name
        self.salary = salary
        self.hours = hours
        self.number = number

    #Подсчет общей зарплаты секретаря
    def calculation_of_total_salary(self):
        self.total_salary = self.salary 
        print(f"id: {sel.number}, name: {self.name}, salary:{self.total_salary}")
        super().expenses.append(self.total_salary)
    
    #Вывод продуктивности секретаря
    def productivity(self):
        pr = self.hours/40*100
        print(f'{self.name} productivity - {pr} %')
        super().productivity[self.name] = pr

class Seller(ProductivityandSalary):
    
    
    def __init__(self, name, salary, sales, hours, number):
        self.name = name
        self.salary = salary
        self.sales = sales
        self.hours = hours
        self.number = number    
    
    #Подсчет общей зарплаты продовца
    def calculation_of_total_salary(self):
        self.total_salary = self.salary + self.sales*50
        print(f"id: {sel.number}, name: {self.name}, salary:{self.total_salary}")
        super().expenses.append(self.total_salary)
    
    #Вывод продуктивности продавца
    def productivity(self):
        pr = self.hours/40*100
        print(f'{self.name} productivity - {pr} %')
        super().productivity[self.name] = pr

class Worker(ProductivityandSalary):
    

    def __init__(self, name, hours, number):
        self.name = name
        self.hours = hours
        self.number = number

    #Подсчет общей зарплаты рабочего    
    def calculation_of_total_salary(self):
        self.total_salary = self.hours*100
        print(f"id: {sel.number}, name: {self.name}, salary:{self.total_salary}")
        super().expenses.append(self.total_salary)
    
    #Вывод продуктивности рабочего
    def productivity(self):
        pr = self.hours/40*100
        print(f'{self.name} productivity - {pr} %')
        super().productivity[self.name] = pr

class ReplacementSecretary(ProductivityandSalary):
    
    
    def __init__(self, name, hours, number):
        self.name = name
        self.hours = hours
        self.number = number
    
    #Подсчет общей зарплаты секретаря на замену
    def calculation_of_total_salary(self):
        self.total_salary = self.hours*100
        print(f"id: {sel.number}, name: {self.name}, salary:{self.total_salary}")
        super().expenses.append(self.total_salary)
    
    #Вывод продуктивности секретаря на замену
    def productivity(self):
        pr = self.hours/40*100
        print(f'{self.name} productivity - {pr} %')
        super().productivity[self.name] = pr

#Создание экземпляров класса
pas = ProductivityandSalary()
m = Manager('Barsbek Kanatkulov', 45000, 18, 1)
sec = Secretary('Alimkul Tilekbaev', 20000, 38, 2)
sel = Seller('Aiperi Shalimbekova', 20000, 20, 38, 3)
wor_1 = Worker('Bakit Rustamov', 25, 4)
wor_2 = Worker('Altinai Shirinbaeva', 40, 5)
rep_sec = ReplacementSecretary('Janar Riskulov', 33, 6) 

#Подсчет зарплаты каждого рабочего
print("Зарплаты сотрудников фабрики:")
m.calculation_of_total_salary()
sec.calculation_of_total_salary()
sel.calculation_of_total_salary()
wor_1.calculation_of_total_salary()
wor_2.calculation_of_total_salary()
rep_sec.calculation_of_total_salary()
print(' ')

#Вывод продуктивности каждого рабочего
print("Продуктивность сотрудников фабрики:")
m.productivity()
sec.productivity()
sel.productivity()
wor_1.productivity()
wor_2.productivity()
rep_sec.productivity()
print(' ')

#Вывод затрат и самого продукивного и непродуктивного рабочего
print(f'Общие затраты на зарплату: {sum(pas.expenses)}')
pas.max_productivity()
pas.min_productivity()