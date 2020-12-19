import random

def getAnswer(answerNumber):
    if answerNumber == 1 :
        return "Okay Okay we can concider this plan !!"
    elif answerNumber == 2 :
        return "We should think over this plan !!!"
    elif answerNumber == 3 :
        return "Not interested, might concider it as plan B but definitly not plan A !!"
    elif answerNumber == 4 :
        return "What plan, you are calling this bullshit a plan"
    
r = random.randint(1, 4)
pridiction = getAnswer(r)
print(pridiction)