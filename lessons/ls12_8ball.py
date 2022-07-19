"""The answers to unknowns! An8ball game."""

from random import randint


def main() -> None:
    """Entrypoint into our game!"""
    is_playing: bool = True
    while is_playing:
        input("Ask a yes/no question: ")
        random_value: int = randint(0, 3)
        print(response(random_value))
        is_playing = input("Continue? yes/no: ") == "yes"
    print("Have a great day!")


def response(n: int) -> str:
    """Given a number, return a response of the 8ball."""
    if n == 0:
        return "Definitely, yes!"
    else:
        if n == 1:
            return "Ask again lateral."
        else:
            return "It will never happened."


# Python Idiom for a runnable Python module
if __name__ == "__main__":
    main()
else:
    print(__name__)
