print ("Welcome to my first game!")
name = input("What is your name? ")
age = input("What is your age? ")

health = 15

if int(age) >= 16:
    print("You are old enough to play!")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("You are starting with", health, "health")
        print("Let's play!")

        left_or_right = input("First choice... Left or Right (left/right)? ")
        if left_or_right == "left":
            ans = input("Nice, you follow the path an reach a lake... Do you swim across or go around (across/around)? ")

            if ans == "around":
                print("You went around and reached the other side of the lake")
            elif ans == "across":
                print("You managed to get across but was stung by a jellyfish and lost 5 health")
                health -= 5

            ans = input("You notice a house and a shed, which do you go into (shed/house)? ")
            if ans == "house":
                print("You go to the house and get bitten by the guard dog... You lose 5 health")
                health -= 5
            else:
                print("You go into the shed and pick up a matchette")
                
            ans = input("You spot quard dog... Do you pet the dog or kill it (pet/kill it)? ")
            if ans == "kill it":
                print("You have killed your bet friend... You lose 5 health")
                health -= 5

                if health <= 0:
                    print("You now have 0 health and you have lost the game")
                else:
                    print("You have suvived the game...")
                    
            else:
                print("You have made a new friend and gained protection for your house as the new owner...")
                

                
                 
        else:
            print("You fell down and lost...")
                

        
    else:
        print("Goodbye!")
        
else:
    print("You are not old enough to play, Goodbye!")

''' ** = exponential, % mud operator = remainder after division, // interger division = no it divides, == is equal to, != not equal to  '''