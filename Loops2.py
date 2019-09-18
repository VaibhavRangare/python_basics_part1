user_input = ""
while True:
    user_input = input("Enter Value:")
    if user_input == "Greet":
        print("Hello")
    elif user_input == "Say Again":
        print("Say Again")
    elif user_input == "QUIT":
        break
    else:
        print("I don't understand that")
