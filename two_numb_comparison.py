def numb_comparison():
    x = int(input('Enter x: '))
    y = int(input('Enter y: '))
    if x > y:
        return "Bigger"
    elif x < y:
        return "Smaller"
    else:
        return "These numbers are equal"

print(numb_comparison())
