startingWeight = 150
targetWeight =  220
currentWeight = startingWeight

eat_count = 0
exercise_count = 0

def eat():
    global currentWeight, eat_count
    currentWeight += 20
    eat_count += 1

def exercise():
    global currentWeight, exercise_count
    currentWeight -= 10
    exercise_count += 1

while currentWeight != targetWeight:
    if currentWeight > targetWeight:
        exercise()
    elif currentWeight < targetWeight:
        eat()

print("Your target weight is " + str(targetWeight) + " your starting weight was "
+ " and your current weight is now " + str(currentWeight))
print("You ate " + str(eat_count) + " times and " + 
"exercised " + str(exercise_count) + " times to reaschh your target weight")