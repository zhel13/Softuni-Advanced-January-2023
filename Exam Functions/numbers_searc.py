def numbers_searching(*args):
    result = []
    set_result = set(args)
    min_num = min(set_result)
    max_num = max(set_result)
    for i in range(min_num, max_num + 1):
        if i not in set_result:
            result.append(i)
    duplicates = set([x for x in args if args.count(x) > 1])
    checking_duplicates = list(duplicates)
    result.append(sorted(checking_duplicates))
    return result


print(numbers_searching(1, 2, 4, 2, 5, 4))
print(numbers_searching(5, 5, 9, 10, 7, 8, 7, 9))
print(numbers_searching(50, 50, 47, 47, 48, 45, 49, 44, 47, 45, 44, 44, 48, 44, 48))
