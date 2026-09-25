import random
print("Welcome to Rock-Paper-Scissors")
print("Winning Rules")
print("Rock vs Paper == Paper")
print("Paper vs Scissors == Scissors")
print("Scissors vs Rock == Rock")

choices = ["Rock", "Paper", "Scissors"]

while True:
    print("1.Rock")
    print("2.Paper")
    print("3.Scissors")
    print("4.Exit")
    try:
      choice = int(input("Enter your choice(1-4): "))
    except ValueError:
      print("Invalid input. Please enter a number.")
      continue
    if choice == 4:
      break
    elif choice < 1 or choice > 4:
      print("Invalid choice. Please enter a number between 1 and 4.")
      continue
    
    # Map integer choice to string choice using the 'choices' list
    user_choice = choices[choice - 1]
    print("\nUser choice is:", user_choice)
    print("Now it's Computer's Turn...")
    
    comp_choice = random.randint(1, 3)
    # Map integer computer choice to string choice using the 'choices' list
    computer_choice = choices[comp_choice - 1]
    print("Computer choice is:", computer_choice)
    print(user_choice, "vs", computer_choice)

    # Determine winner
    if choice == comp_choice:
        print("<== It's a Tie! ==>")

    elif (
        (choice == 1 and comp_choice == 3) or
        (choice == 2 and comp_choice == 1) or
        (choice == 3 and comp_choice == 2)
    ):
        print("<== User Wins! ==>")

    else:
        print("<== Computer Wins! ==>")


print("\nThanks for playing!")
