import random

def randomChoicerReturnsAngle(choiceCount):
    randomIndex = random.randrange(0,choiceCount) 
    print(randomIndex)
    degreePerSlice = 360/choiceCount
    randomRealIndex = randomIndex
    randomIndex = choiceCount - randomIndex
    stop_angle = degreePerSlice * randomIndex - (degreePerSlice /2)
    return randomRealIndex,stop_angle