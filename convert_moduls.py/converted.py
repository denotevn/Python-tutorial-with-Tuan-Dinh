def lbs_to_kg(weigth):
    return weigth * 0.45

def kg_to_lbs(weight):
    return weight/0.45

def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if max < number:
            max = number
    return max


