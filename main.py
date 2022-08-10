print ("Welcome to my first game!")
name = input("What is your name? ")
age = input("What is your age? ")

print("Hello", name, "you are", age,"years old.")

if int(age) >= 16:
    print("You are old enough to play!")

    wants_to_play = input("Do you want to play? ").lower()
    if wants_to_play == "yes":
        print("Let's play!")

        left_or_right = input("First choice... Left or Right (left/right)? ")
        if left_or_right == "left":
            ans = input("Nice, you follow the path an reach a lake... Do you swim across or go around (across/around)? ")

        else:
            print("You fell down and lost...")
                

        
    else:
        print("Goodbye!")
        
else:
    print("You are not old enough to play, Goodbye!")

''' ** = exponential, % mud operator = remainder after division, // interger division = no it divides, == is equal to, != not equal to  '''