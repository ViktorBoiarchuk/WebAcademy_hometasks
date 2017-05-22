def nested_list_showing():
    m = int(input("Enter m list parameter: "))
    n = int(input("Enter n list parameter: "))
    list_parameters = "{} * {}".format(m, n)
    print(list_parameters)
    resulted_list = [[list(range(i+1, n+1+i))] for i in range(m)]
    # for i in range(m):
    #     resulted_list.append([list(range(i+1, n+1+i))])
    return resulted_list

print(nested_list_showing())
