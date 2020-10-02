# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  

answer1 = ["Pd4", "Qd3", "Qh3", "Qc8"] #these are the answers to the game, if they enter either of these they win
#print(answer1)
answer2 = ["Pc4", "Qa4", "Qc6", "Qc8"]
#print(answer2)

print("There are 2 ways to beat the copycat in chess in 4 moves. Try to find the right combination and you'll win.") #explains the goal
print("To enter moves, Use the first letter of the piece first (capital letter), then the sqaure that piece is moving to.") #explains how to play

practice = str(input("Try entering bishop to b4: ")) #gives them an oppurtunity to practice, to make sure they enter it correctly
if practice == "Bb4":
    print("You got it! ")
else:
    print("The correct input was: Bb4")

play_again = 1 #allows user to play again
while play_again == 1:

    user_list = []
    number_of_moves = 1

    while number_of_moves < 5:
        user_moves = input("Okay, enter one move at a time to try and find chechmate in 4: ")
        user_list.append(user_moves) #puts each of their moves into a list
        number_of_moves = number_of_moves + 1

    if user_list == answer1:
        print("You win! You found the correct moves!")
    elif user_list == answer2:
        print("ou win! You found the correct moves!")
    else:
        print("You didn't quite get the answer, but don't worry you can try again and ask for a hint")

    hint = input("Would you like a hint? If yes type y, if no type n: ") #hints give them one move of one of the solutions
    if hint == "y":
        hint_number = input("Okay, you want a hint. If you want the first move of one of the solutions type 1, second 2, third 3, fourth 4: ") #choose what move they want to know
        if hint_number == "1":
            print("The first move is: Pd4")
        elif hint_number == "2":
            print("The second move is: Qd3")
        elif hint_number == "3":
            print("The third move is: Qh3")
        elif hint_number == "4":
            print("The fourth move is: Qc8")
        else:
            print("You didn't enter 1,2,3, or 4 so no hint for you...")
    elif hint == "n":
        print("You must be really confident if you don't want a hint, good luck")
    else:
        print("You didn't enter n or y :(")

    play_again = int(input("Do you want to try again? If you do type 1 if you don't type 2: "))
    
