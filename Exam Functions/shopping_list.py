def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."

    basket = set()
    products = []
    for product, data in kwargs.items():
        price = data[0] * data[1]

        if len(basket) == 5:
            break
        if budget >= price:
            basket.add(product)
            products.append(f"You bought {product} for {price:.2f} leva.")
            budget -= price

    return "\n".join(products)


# print(shopping_list(100,
#                     microwave=(70, 2),
#                     skirts=(15, 4),
#                     coffee=(1.50, 10),
#                     ))
# print(shopping_list(20,
#                     jeans=(19.99, 1),
#                     ))
print(shopping_list(104,
                    cola=(1.20, 2),
                    candies=(0.25, 15),
                    bread=(1.80, 1),
                    pie=(10.50, 5),
                    tomatoes=(4.20, 1),
                    milk=(2.50, 2),
                    juice=(2, 3),
                    eggs=(3, 1),
                    ))
