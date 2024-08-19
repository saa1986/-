# Задача "Распаковка":
# 1.Функция с параметрами по умолчанию:
# Создайте функцию print_params(a = 1, b = 'строка', c = True), которая принимает три параметра со значениями по умолчанию (например сейчас это: 1, 'строка', True).
# Функция должна выводить эти параметры.
# Вызовите функцию print_params с разным количеством аргументов, включая вызов без аргументов.
# Проверьте, работают ли вызовы print_params(b = 25) print_params(c = [1,2,3])
# 2.Распаковка параметров:
# Создайте список values_list с тремя элементами разных типов.
# Создайте словарь values_dict с тремя ключами, соответствующими параметрам функции print_params, и значениями разных типов.
# Передайте values_list и values_dict в функцию print_params, используя распаковку параметров (* для списка и ** для словаря).
# 3.Распаковка + отдельные параметры:
# Создайте список values_list_2 с двумя элементами разных типов
# Проверьте, работает ли print_params(*values_list_2, 42)
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

print_params()  # 1 строка True
print_params(b=25)  # 1 25 True
print_params(c=[1, 2, 3])  # 1 строка [1, 2, 3]
print_params('Taksi', 2, 0)  # Taksi 2 0
values_list = [1, True, 'van']
values_dict = {'a': 'Urban + Python','b': True,'c': 1986,}
print_params(*values_list)  # 1 True van
print_params(**values_dict)  # Urban + Python True 1986
values_list_2 = [190824, ' Python + Urban']
print_params(*values_list_2, 38)  # 190824 Python + Urban 38