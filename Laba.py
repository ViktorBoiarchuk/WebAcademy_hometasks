def laba_description():
    laba_name = input("Enter laba: ")
    group = input("Enter your group: ")
    name = input("Enter your name:  ")
    all_laba_data = [len(group), len(name), len(laba_name)]
    table_length = max(all_laba_data)
    return table_length, laba_name, group, name


def laba_print():
    table_length, laba_name, group, name = laba_description()
    print("{0}{1}{0}".format('*', '*'*table_length))
    for elem in [laba_name, group, name]:
        print("{0}{1}{0}{2}".format('*', elem, (table_length - len(elem)) * '*'))
    print("{0}{1}{0}".format('*', '*'*table_length))

laba_print()
