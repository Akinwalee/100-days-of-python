print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

if size == "S":
    p_price = 15
    if add_pepperoni == "Y":
        p_price += 2
elif size == "M":
    p_price = 20
    if add_pepperoni == "Y":
        p_price += 3
elif size == "L":
    p_price = 25
    if add_pepperoni == "Y":
        p_price += 3

if extra_cheese == "Y":
    p_price += 1

print("Your final bill is: ${}".format(p_price))