def lecture_number():
    try:
        module_number = int(input('module number: '))
        lecture_part = int(input('part: '))
    except ValueError as error:
        print('Wrong input, {}! Try again'.format(error))
        lecture_number()
    print('module_name: {}.{}'.format(module_number, lecture_part))
    res = module_number*2 + (lecture_part-2)
    return 'Lecture number: {}'.format(res)

print(lecture_number())
