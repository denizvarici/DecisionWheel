import random

def randomChoicerReturnsAngle(choiceCount):
    randomIndex = random.randrange(0,choiceCount) 
    print(randomIndex)
    degreePerSlice = 360/choiceCount
    randomIndex = choiceCount - randomIndex
    return degreePerSlice * randomIndex - (degreePerSlice /2)