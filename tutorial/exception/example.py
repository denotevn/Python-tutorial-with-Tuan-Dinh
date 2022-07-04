random_list = ['a', 1, 2]

for num in random_list:
    try:
        print(f"The number is {num}")
        r = 1/int(num)
        break
    except Exception as e:
        print(f"Oops! {e.__class__} occurred. ")
        print("Next entry.")
        print()
print("The reciprocal of", num, "is", r)