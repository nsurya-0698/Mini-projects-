import random
import time
print("Welcom to the game")

ready = input("Ready to start Game? ")
top_range = str(int(input("Give me a number ")))

number_of_attemptes = 0
if ready.lower() == "yes" and top_range.isdigit():
    print("Let's Go")
else:
    print("See you next time ")

print("Loading a number.......")
time.sleep(3)

while True: 
        number = str(input("Guss my number ranging from 0 to the number you entered! "))
        number_of_attemptes += 1
        
        if number.isdigit() and int(number) >= 0 and int(number) <= 10:
            number = int(number)
            gussed_int = random.randint(0, int(top_range))

            if number > gussed_int:
                print("You are above the numebr")
            elif number < gussed_int:
                print("You are below the number")
            else: 
                print("Hurray!!! You got it.")
                print("Number of attempts {}".format(number_of_attemptes))
                break
        else:
            print("Enter a Valid integer from 0 to number you entered")
