"""A demosntration of class/objects."""


class Pizza:
    """A simple model of Pizza."""
    size: str = "medium"
    extra_cheese: bool = False
    toppings: int = 0

def main() -> None:
    """Entrypoint of program."""
    a_pizza: Pizza = Pizza()
    a_pizza.size = "large"
    a_pizza.toppings = 3
    a_pizza.extra_cheese = True
    print("Price: " + str(price_calculator(a_pizza)))
    print("Size: " + a_pizza.size)
    print("Toppings: " + str(a_pizza.toppings))

def price_calculator(a_pizza: Pizza) -> float:
    pizza_price: float = 0.0
    if Pizza.size == "medium":
        pizza_price += 9
    elif Pizza.size == "large":
        pizza_price += 11
    elif Pizza.size == "small":
        pizza_price += 7
    if Pizza.extra_cheese:
        pizza_price += 1
    else:
        pizza_price = pizza_price
    pizza_price += (0.75 * Pizza.toppings)
    return pizza_price
    

if __name__ == "__main__":
    main()
