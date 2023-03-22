from collections import deque

number_of_pizza = deque([int(s) for s in input().split(", ")])
pizza_makers = deque([int(s) for s in input().split(", ")])
MAX_NUM_PIZZA = 10
pizza_counter = 0

while number_of_pizza and pizza_makers:
    if number_of_pizza[0] > MAX_NUM_PIZZA or number_of_pizza[0] <= 0:
        number_of_pizza.popleft()
        continue
    else:
        if number_of_pizza[0] <= pizza_makers[-1]:
            pizza_counter += number_of_pizza[0]
            number_of_pizza.popleft()
            pizza_makers.pop()

        else:
            number_of_pizza[0] -= pizza_makers[-1]
            pizza_counter += pizza_makers[-1]
            pizza_makers.pop()

if number_of_pizza:
    print(f"Not all orders are completed.\nOrders left: {', '.join([str(r) for r in number_of_pizza])}")

else:
    print(f"All orders are successfully completed!\nTotal pizzas made: {pizza_counter}\n"
          f"Employees: {', '.join([str(e) for e in pizza_makers])}")
