from random import randint
player_points = 0
comp_points = 0
choice_list = ["stone", "paper", "scissors"]
win = int(input("Winner should have how many points: "))
while player_points < win and comp_points < win:
    print("Stone")
    print("Paper")
    print("Scissors")
    player_choice = input("Choose one: ").strip().lower()
    if player_choice not in choice_list:
        print("Please enter a valid input\n")
        continue
    comp_choice = choice_list[randint(0, 2)]
    print(f"Computer chose {comp_choice.capitalize()}")
    if player_choice == comp_choice:
        print("It's a tie")
    elif (
        (player_choice == "stone" and comp_choice == "scissors") or
        (player_choice == "paper" and comp_choice == "stone") or
        (player_choice == "scissors" and comp_choice == "paper")
    ):
        player_points += 1
        print("You win this round!")
    else:
        comp_points += 1
        print("Computer wins this round!")
    print(f"You have {player_points} points")
    print(f"Computer has {comp_points} points\n")
if comp_points == win:
    print("The computer won")
else:
    print("You won")
