"""An example of a while loop statement"""

iterations: int = int(input("How many times?"))
i: int = 0

while i < iterations:
    print("In repeat block")
    print("i is " + str(i))
    i = i + 1


print("After repeat block! i is " + str(i))
