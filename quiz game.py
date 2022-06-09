print("welcome to computer quiz!")
playing = input("Do want to play? ")
text =  "Tim IS GReat!"
print(text.lower())

if playing.lower() != "yes":
    quit()

print("Okay ! lets play:)")
score = 0
answer = input("what does cpu stand for? ")
if answer.lower == "cental processing unit?":
    print('correct!')
    score += 1
else:
    print('Incorrect!')
answer = input("what does GPU stand for")
if answer.lower == "graphics processing unit":
    print('correct!')
    score += 1
else:
    print('Incorrect!')
answer = input("what does RAM stand for ")
if answer.lower == "random access memory":
    print('correct!')
    score += 1
else:
    print('Incorrect!')
answer = input("what does psu stand for ")
if answer.lower == "random access memory":
    print('correct!')
    score +=1
else:
    print('Incorrect!')
print("You got " + str(score) + "questions correct!")
#print("You got " + str(score / 4) * 100) + "%. "
