price = 1000000
is_good_credit = True

print("*" * 45)
if is_good_credit:
    down_payment = 0.1*price
    print(f"Down Payment: ${down_payment}")
else:
    down_payment = 0.2 * price
    print(f"Down Payment: ${down_payment}")