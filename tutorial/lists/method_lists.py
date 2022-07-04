numbers = [5,2,2,2,2,4]
print(numbers.index(2)) # 1 - return index of 2 tim thay dau tien
print(50 in numbers) # False
numbers.append(20)
print(numbers) # [5,2,2,2,2,4, 20]
numbers.insert(0,21) # add element with index and values
print(numbers)
print(numbers.count(2)) # 4 so values == 2 trong mang
numbers.clear()
print(numbers) # []