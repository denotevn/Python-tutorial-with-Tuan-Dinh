'''
i = 1
while i < 5:
    print("*" * i)
    i = i + 1
print("Done")
'''

# Easy game
secret_num = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    num_predict = input("Your Guess: ")
    num_predict = int(num_predict, base=10)
    guess_count += 1
    if num_predict == secret_num:
        print("You win !! Amazing !")
        break
    if guess_count == guess_limit:
        print("Your failed!")