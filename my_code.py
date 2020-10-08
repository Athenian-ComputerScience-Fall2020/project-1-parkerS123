# Collaborators (including web sites where you got help: (enter none if you didn't need help)
# Megan helped trouble shoot

answer1 = ["Pd4", "Qd3", "Qh3", "Qc8"] #these are the answers to the game, if they enter either of these they win
#print(answer1)
answer2 = ["Pc4", "Qa4", "Qc6", "Qc8"]
#print(answer2)

def hint_function(): #function that can be called as many times as the user wants, if they play again
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

def user_moves_function(number_of_moves): #function that appends user moves to a list then checks if that list is eqaul to one of the answers
    for x in range (4):
        user_moves = input("Okay, enter one move at a time to try and find chechmate in 4: ")
        user_list.append(user_moves) #puts each of their moves into a list
        number_of_moves = number_of_moves + 1

    if user_list == answer1:
        print("You win! You found the correct moves!")
    elif user_list == answer2:
        print("You win! You found the correct moves!")
    else:
        print("You didn't quite get the answer, but don't worry you can try again and ask for a hint")
        hint_function() #calls the hint function, but no variables in that function so no need for parameters

#These print statements explain the goal and how to play
print("There are 2 ways to beat the copycat in chess in 4 moves. Try to find the right combination and you'll win.")
print("Remember that whatever move you play, your oppenent will play the same move from their perspective (copycat)") 
print("To enter moves, Use the first letter of the piece first (capital letter), then the sqaure that piece is moving to.") 

#asks the player if they know how to play chess, if not tells them a little bit about the game
played_before = input("Have you ever played chess before? Type yes or no: ") 
while played_before == "yes" or "no":
    if played_before == "yes":
        print("Great!")
        break
    elif played_before == "no":
        print("No worries! In chees there is a black team with black pieces and a white team with white pieces.")
        print("The goal of the game is to caputure the other person's king, and you can do this by moving you pieces in a way that you win")
        break
    else:
        played_before = input("Please answer yes or no: have you ever played chess before? ")
        

practice = str(input("Try entering bishop to b4: ")) #gives them an oppurtunity to practice, to make sure they enter it correctly
if practice == "Bb4":
    print("You got it! ")
else:
    print("The correct input was: Bb4")

play_again = 1 #allows user to play again, if variable is equal to 1

while play_again == 1:
    user_list = []
    number_of_moves = 1
    user_moves_function(number_of_moves) #calls user moves function above, with parameter number_of_moves
    #hint_function is called within user_moves_function so they only get asked if they want a hint if they got it wrong

    try: 
        play_again = int(input("Do you want to try again? If you do type 1 if you don't type your favorite number: "))
    except: 
        print("Please enter a valid input!")
        except_play_again = input("Do you want to try again? If you do type 1 if you don't type anything else: ")
        if except_play_again == "1":
            play_again = 1
        else: 
            play_again = 0

    
