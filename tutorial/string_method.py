course = 'Python for Beginners'
print(len(course)) # return length of string
print(course.upper()) # to upper the string

print(course.lower())

#find use to find index of character or substring of string
# if don't find the character function return -1
print(course.find('P')) # 0
print(course.find('0')) # -1
print(course.find('Beginners')) # se lay chi so phan tu dau tien cua chuoi

# Reaplace string
print(course.replace('Beginners', 'Absolute Beginners')) # Python for beginners
# in
print('python' in course) # False
print('Python' in course) # True
#title
print(course.title()) # Python For Beginners