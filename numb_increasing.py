def numb_increase():    # if there are unless two equal numbers, all numbers will decrease on decreasing numb
    x = int(input('Enter x: '))
    y = int(input('Enter y: '))
    z = int(input('Enter z: '))
    numbers = [x, y, z]
    for i in numbers:
        count = numbers.count(i)
        if count >= 2:
            increasing = int(input('Enter the numb: '))
            numbers = [el + increasing for el in numbers]
            return numbers
        else:
            return 'There is no equal numbers'

print(numb_increase())
