print("Welcome to my computer science term quiz!")

playing = input("Do you want to play the class review for MidTerm? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let the MidTerm games begin:)")
score = 0

answer = input("What does the term CS originally stand for class ? ")
if answer.lower() == "Computer Science":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is a quick way to refer to the massive amounts of data collected by organizations on a day-to-day basis? ")
if answer.lower() == "Big Data":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("is an alternative to storing data on a computers physical storage? ")
if answer.lower() == "Cloud storage ":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("what isis an approach to making the flow of tasks in a software development project more efficient? ")
if answer.lower() == "WorkFlow Automation":
    print('Correct!')
    score += 1
    
else:
    print("Incorrect!")
    
answer = input("What is the term used to describe the process of creating a software application? ")
if answer.lower() == "Software Development":
    print('Correct!')
    score += 1
    
else:
    print("Incorrect!") 
    
answer = input("What is the term used to describe arrays? ")
if answer.lower() == "List":
    print('Correct!')
    score += 1
    
else:
    print("Incorrect!")
    
answer = input("What is a Loop? ")
if answer.lower() == "A loop is a sequence of instructions that is repeated until a certain condition is met. ":
    print('Correct!')
    score += 1
    
else:
    print("Incorrect!")
    score+= 1 

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 3.5 ) * 100) + "%.")