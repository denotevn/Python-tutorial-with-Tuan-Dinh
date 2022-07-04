'''
Name: Tuan Dinh
Email: tuandinh@gmail.com
Phone: 11223344
'''

customer = {
    "name":"Tuan Dinh",
    "Email":"tuandinh@gmail.com",
    "Phone":"11223344",
    "age":"25",  
    "is_vertified":"True"
}

print(customer["name"]) # Tuan Dinh
print(customer.get("name"))

#change the data
customer["name"] = "Dinh Ngoc Tuan"
print(customer["name"]) # Dinh Ngoc Tuan

print(customer["Email"]) # tuandinh@gmail.com
print(customer["age"]) # 25
# i so on
