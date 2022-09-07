from datetime import datetime
from pprint import pprint

# 1. Создайте словарь: {"city": "Москва", "temperature": "20"}
dic = {"city": "Москва", "temperature": "20"}

# 2. Выведите на экран значение ключа city
print(dic["city"])

# 3. Уменьшите значение "temperature" на 5
dic["temperature"] = int(dic["temperature"]) - 5
print(dic["temperature"])

# 4. Выведите на экран весь словарь
print(dic)

#----------------------------------------------------------------

# 1. Проверьте, есть ли в словаре ключ country
print(dic.get("country"))

# 2. Выведите значение по-умолчанию "Россия" для ключа country
dic["country"] = "Russia"

# 3 Добавьте в словарь элемент date со значением "27.05.2019"
date_str =  datetime(2019,5,27)
date_conv = date_str.strftime("%d.%m.%Y")
dic["date"] = date_conv
print(dic)

# 4. Выведите на экран длину словаря
print(len(dic))