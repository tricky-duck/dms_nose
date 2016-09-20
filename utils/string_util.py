# -*- coding: utf-8 -*-
import random
import string


def random_string(prefix, max_len, spec=False):
    spec_symbols = r'[|]~<!--@/*$%^&#*/()?>,.*/\№_={":' + r"';`}"
    symbols = string.ascii_letters + string.digits
    if spec:
        symbols += spec_symbols
    if max_len > len(prefix):
        random_len = max_len - len(prefix)
    elif max_len == 0:
        return prefix
    else:
        random_len = 0
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(1, random_len + 1))])


def random_string_fixed_len(prefix, str_len):
    symbols = string.ascii_letters + string.digits
    if str_len > len(prefix):
        random_len = str_len - len(prefix)
    elif str_len == 0:
        return ""
    else:
        random_len = 0
    return prefix + "".join([random.choice(symbols) for i in range(random_len)])


# умножает строку на рандомное число в заданном диапазоне
def random_string_mult(s, max_len):
    return s*(random.randrange(1, max_len + 1))