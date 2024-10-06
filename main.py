numbers = list(map(int, input("Введите числа через пробел: ").split())) # создание нового списка с квадратами чисел
squares = [number**2 for number in numbers] # цикл for с условием
print(squares) # вывод результата