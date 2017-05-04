def triangle_print():
    numb = int(input("Enter numb: "))
    for i, v in enumerate(range(numb, 0, -1)):
        print('*' * v, '.' * i, sep='')


triangle_print()
