import random

for i in range(3):
    print(random.random()) # random values 0 -> 1
print("Randome 10 -> 20")

for i in range(5):
    print(random.randint(10,20))

members = ['Tuan', 'Ngoc', 'Manh', 'Thanh']
leader = random.choice(members) # chon ngau nhien q nguoi lam leader tu members
print(leader)