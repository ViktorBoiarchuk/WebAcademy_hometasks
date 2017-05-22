def count_symb():
    string = input("Enter a string: ")
    symb = input("Enter a symbol: ")
    count = 0
    for letter in string:
        if symb == letter:
            count += 1
    return count

print(count_symb())