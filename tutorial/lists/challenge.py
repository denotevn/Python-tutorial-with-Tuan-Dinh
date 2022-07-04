from enum import unique


numbers = [1,2,3,4,2,5,1,2]
uniques = []
print(numbers)

for x in numbers:
    if x not in uniques:
        uniques.append(x)
print(uniques)