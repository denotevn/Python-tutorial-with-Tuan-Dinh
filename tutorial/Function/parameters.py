def greet_user(name):
    print(f"Hi! My name's {name}")


print("Start !")
greet_user("Tuan")
greet_user("Ngoc")
print("Finish")

def greet_user(first_name, last_name):
    print(f"Hi! My name's {first_name} {last_name}")


print("Start !")
greet_user(first_name="Tuan",last_name="Dinh" )
greet_user(last_name="Ngoc", first_name="Khanh")
print("Finish")