name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ")

    if answer == "swim":
        print("You swam across and was eaten by a frog.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print('Not a valid option. You lose!')

elif answer == "right":
    answer = input("You come to a bridge, it is wobbly, do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("You go back and lose the game!")
    elif answer == "cross":
        answer = input("You meet a troll on the bridge and she ask you a riddle, do you answer the riddle correct or wrong (correct/wrong)? ")

        if answer == "correct":
            print ("You answer correctly and win the pot of GOLD!!!, You have won the game!!!.")
        elif answer == "wrong":
            print ("The lady troll eates you up and you die. You have lost the game!!!")
        else:
            print('Not a valid option. You lose!')

    else:
        print('Not a valid option. You lose!')

else:
    print('Not a valid option. You lose!')

print("Thank you for playing see you next time!!!", name)