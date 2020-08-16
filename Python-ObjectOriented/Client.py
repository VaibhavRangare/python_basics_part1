from Employee import Employee, Manager

employee = Employee("Manager","India")
print(f'Employee Country is: {employee.country}')
print(f'Employee Country is: {employee.type}')

manager = Manager("John",43,"Male")
print(f'Manager Name is: {manager.name}')
print(f'Manager age is: {manager.age}')
print(f'{manager.name} is: {manager.type}')
print(f"{manager.name}'s country is: {manager.country}")
