import random
import time

loop = True

print("Hi, and welcome to this mathematical quiz!")

while loop:
    choice = str(input("Press:\na for multiplication. \nb for addition. \nc for subtraction. \nd for division \nPress q at any time to quit\nChoose: "))
    
    if choice not in ["a","b","c","d","q"]:
        print("You pressed an invalid character.\n")

    else:
        loop = False


#MULTIPLICATION
while choice != "q":

    a = random.randint(1,10)
    b = random.randint(1,10)

    points = 0
    counter = 0
    i = 0

    while(choice == "a"):

        
        numberOfTimes = int(input("How many times do you want to practice? "))
        if(numberOfTimes == "q"):
            break

        while (i < numberOfTimes):
            
            a = random.randint(1,10)
            b = random.randint(1,10)
            
            answer = input("What is " + str(a) + " * " + str(b) + " ? ")
            solution = a*b
            
            if(int(answer) ==  solution):
                print("Correct!")
                points += 1
                counter += 1
            else:
                print("Sorry that was a wrong answer")
                print("The correct answer is " + str(int(a*b)))
                counter += 1
            i += 1
            
        print("You have " + str(points) + "/" + str(counter) + " answers correct! Good job :)\n")

        i = 0
        choice = input("Press:\na for multiplication. \nb for addition. \nc for subtraction. \nd for division \nPress q at any time to quit\nYour choice: ")
        

#ADDITION
    while(choice == "b"):

        numberOfTimes = int(input("How many times do you want to practice? "))
        if(numberOfTimes == "q"):
            break

        while (i < numberOfTimes):
            
            a = random.randint(1,100)
            b = random.randint(1,100)
            
            if(choice == "q"):
                break;
            
            answer = input("What is " + str(a) + " + " + str(b) + " ? ")
            solution = a+b
            
            if(int(answer) ==  solution):
                print("Correct!")
                points += 1
                counter += 1
            else:
                print("Sorry that was a wrong answer")
                print("The correct answer is " + str(int(a+b)))
                counter += 1
                
            i += 1
            
        print("You have " + str(points) + "/" + str(counter) + " answers correct! Good job :)\n")
        i = 0
        choice = input("Press:\na for multiplication. \nb for addition. \nc for subtraction. \nd for division \nPress q at any time to quit\nYour choice: ")


#SUBTRACTION
    while(choice == "c"):

        numberOfTimes = int(input("How many times do you want to practice? "))
        if(numberOfTimes == "q"):
            break
        
        while (i < numberOfTimes):
            
            a = random.randint(1,100)
            b = random.randint(1,100)
            
            if(choice == "q"):
                break;
            
            answer = input("What is " + str(a) + " - " + str(b) + " ? ")
            solution = a-b
            
            if(int(answer) ==  solution):
                print("Correct!")
                points += 1
                counter += 1
            else:
                print("Sorry that was a wrong answer")
                print("The correct answer is " + str(int(a-b)))
                counter += 1
                
            i += 1
            
        print("You have " + str(points) + "/" + str(counter) + " answers correct! Good job :)\n")
        i = 0
        choice = input("Press:\na for multiplication. \nb for addition. \nc for subtraction. \nd for division \nPress q at any time to quit\nYour choice: ")


#DIVISION
    while(choice == "d"):

        numberOfTimes = int(input("How many times do you want to practice? "))
        if(numberOfTimes == "q"):
            break
        
        while (i < numberOfTimes):

            a = random.randint(1,10)
            b = random.randint(1,10)
            if (a>b and a%b == 0):
            
                answer = input("What is " + str(a) + " / " + str(b) + " ? ")
                solution = a/b
                
                if(int(answer) ==  solution):
                    print("Correct!")
                    points += 1
                    counter += 1
                else:
                    print("Sorry that was a wrong answer")
                    print("The correct answer is " + str(int(a/b)))
                    counter += 1
                    
                i += 1
            
            
        print("You have " + str(points) + "/" + str(counter) + " answers correct! Good job :)\n")
        i = 0
        choice = input("Press:\na for multiplication. \nb for addition. \nc for subtraction. \nd for division \nPress q at any time to quit\nYour choice: ")

end = perf_counter()

time = (end-start)
print(time)
