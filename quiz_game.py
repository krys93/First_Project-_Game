print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's Play:)")
score = 0
 
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

    answer = input("What does FLAB stand for? ")
if answer.lower() == "final land acquisition boundary":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

    answer = input("What does SOS stand for? ")
if answer.lower() == "save our ship":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

    answer = input("What does AC/DC stand for? ")
if answer.lower() == "rock band":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
