lst = [1, 2, 3, 4, 5]
if len(lst) > 1:
    lst[0], lst[-1] = lst[-1], lst[0]
print(lst)