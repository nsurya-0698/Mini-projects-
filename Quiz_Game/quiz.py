print("Welcome to the quiz game!")

playing = input("Do you want to start the Game? ")
if playing.lower() != "yes":
    print("See you next time:)")
    quit()

print("Hurrah!! Lets start the game.")
print("You will get -1 for wrong answear")
name = input("Enter you name: ")
score = 0
num_of_que = 0

answer = input("What does CPU stands for? ")
num_of_que += 1
if answer.lower() == "central processing unit":
     print("Correct!") 
     score = score + 1
else:
     print("Incorrect")
     score = score - 1

answer = input("What is you height? ")
num_of_que += 1
if float(answer) >= 6:
     print("Correct!")
     score = score + 1 
else:
     print("Incorrect")
     score = score - 1

print(name +" got "+ str(score))
print(name + " got " + str((score/num_of_que) * 100) + " %")
if score > 1:
    print("Good job :)")
else:
    print("Better luck next time")
 

