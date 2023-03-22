def list_manipulator(num_list, *args):
    commands = args[0]
    direction = args[1]
    item = args[2:]

    if commands == "remove":
        if direction == "end":
            if item:
                for i in range(args[2]):
                    num_list.pop()
            else:
                num_list.pop()
        elif direction == "beginning":
            if item:
                for i in range(args[2]):
                    num_list.pop(0)
            else:
                num_list.pop(0)
    elif commands == "add":
        if direction == "end":
            num_list.extend(x for x in item)
        else:
            for x in range(1, len(item)+1):
                num_list.insert(0, item[-x])

    return num_list


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))

