def number_base(numb, base):
    numb = numb.upper()
    chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = 0
    for i in numb:
        for ind, v in enumerate(chars):
            if i == v and ind >= base:
                return -1
    if base == 10:
        return int(numb)
    elif base == 10:
        return -1
    elif base < 10:
        chars = chars[0:base]
        numb = numb[::-1]
        for el, v in enumerate(numb):
            for i in chars:
                if v == i:
                    result += int(v)*(base**el)
        return result
    elif base > 10:
        numb = numb[::-1]
        for el, v in enumerate(numb):
            for p, i in enumerate(chars):
                if v == i:
                    result += p*(base**el)
        return result

print(number_base("1A", 11))

"""
def checkio(str_number, radix):
    try:
        return int(str_number, radix)
    except ValueError:
            return -1

print(checkio("z", 36))
"""
