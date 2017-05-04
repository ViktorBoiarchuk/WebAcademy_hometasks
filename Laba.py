def laba_description():
    laba_name = input("Enter laba: ")
    group = input("Enter your group: ")
    name = input("Enter your name:  ")
    all_laba_data = [len(group), len(name), len(laba_name)]
    for i in all_laba_data:
        if i == max(all_laba_data):
            table_length = i
            return table_length, laba_name, group, name


def laba_print():
    table_length, laba_name, group, name = laba_description()
    print("{0}{1}{0}".format('*', '*'*table_length))
    for dumpy_i in [laba_name, group, name]:
        print("{0}{1}{0}".format('*', dumpy_i), (table_length-len(dumpy_i))*'*', sep='')
    print("{0}{1}{0}".format('*', '*'*table_length))

laba_print()
