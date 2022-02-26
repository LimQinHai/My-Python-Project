import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome To Python Password Generator.")
no_number = int(input("How many numbers would you like to have in your password?\n"))
no_symbol = int(input("How many symbols would you like to have in your password? \n"))
no_letter = int(input("How many letters would you like to have in your password? \n"))

print("Example High Level Password: 34vRf$7Op&h@     Easy Level Password: 4567&#Abcd")
answer = input("Would like to generate 'High Level' or 'Easy Level' password?\n ")
answer = answer.lower()

if answer == "easy level":
    Password = ""

    for char in range(1,no_number+1):
        Password += random.choice(numbers)
    for char in range(1,no_symbol+1):
        Password += random.choice(symbols)
    for char in range(1,no_letter+1):
        Password += random.choice(letters)
    print(f"Your Password is {Password}.")
    print("Thank you for using Python Password Generator.")

elif answer == "high level":
    Password_list = []

    for char in range(1,no_number+1):
        Password_list.append(random.choice(numbers))

    for char in range(1,no_symbol+1):
        Password_list.append(random.choice(symbols))

    for char in range(1,no_letter+1):
        Password_list.append(random.choice(letters))

    random.shuffle(Password_list)

    Password = ""
    for char in Password_list:
        Password += char

    print(f"Your Password is {Password}.")
    print("Thank you for using Python Password Generator.")
else:
    print("You have entered invalid answer.Please try again.")
