birth_year = input('What is your birth year? ')
print(type(birth_year))
age = 2022 - int(birth_year, base=10) # base = 10 convert string -> integer
print(type(age))
print(age)

price = input('Some float nnumber: ')
diff = 20.14 - float(price)
print(diff)

