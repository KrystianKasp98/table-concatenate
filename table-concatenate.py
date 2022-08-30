def concatenate_args_list(*args):
    required_len = len(args)
    r_list = []
    items = []
    for index, item in enumerate(args):
        for numb_index, numb in enumerate(item):
            if index == 0:
                items.append([])
            try:
                items[numb_index].append(numb)
            except:
                break

    for item in items:
        if not required_len == len(item):
            break
        else:
            r_list.append(sum_args_val(item))

    return r_list


def sum_args_val(l_numb):
    res = 0
    for numb in l_numb:
        if not isinstance(numb, int) and not isinstance(numb, float):
            res = None
            break
        else:
            res += numb
    return res


print(concatenate_args_list([33, 12, 99, 12, 88, 9, 12], [None, "", 23, "none", 552, False, 22, 66, 77], [11, 22, 33, 44, 55, 66, 33, 12, 99, 12, 88, 9]))
