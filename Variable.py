name = 'Vaibhav'            # String
age = 10                    # integer
book_price = 10.5           # float
is_readable = False         # bool
# is_readable = false       # compilation error

print(name)                 # Vaibhav
print(age)                  # 10
print(float(age))           # 10.0
print(book_price)           # 10.5
print(int(book_price))      # 10
print(is_readable)          # False
print(bool(0))              # False
print(bool(1))              # True
print(str(10))              # 10
# print(name+','+ age+','+ book_prie) # can only concatenate str (not "int") to str

print(type(name))           # <class 'str'>
print(type(is_readable))    # <class 'bool'>
