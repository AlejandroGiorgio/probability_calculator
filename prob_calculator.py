import copy
import random

class Hat:
    def __init__(self,**kwargs):
        self.contents = []
        for k,v in kwargs.items():
            for i in range(v):
                self.contents.append(k)

    def draw(self, num):
        takenList = []
        if num >len(self.contents):
            return self.contents
        for x in range(num):
            num = random.randint(0, len(self.contents)-1)
            drawn = self.contents[num]
            self.contents.pop(num)
            takenList.append(drawn)
        return takenList
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    succesRate = 0
    for x in range(num_experiments):
        hatCopy = copy.deepcopy(hat)
        drawn= hatCopy.draw(num_balls_drawn)
        succesCount = sum([1 for k,v in expected_balls.items() if drawn.count(k) >= v])
        succesRate += 1 if succesCount == len(expected_balls) else 0

    return succesRate/num_experiments
