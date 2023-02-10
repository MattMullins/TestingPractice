class ScoreMachine:
    def __init__(self):
        pass
    
    def aces(self,rolls):
        total = 0
        for item in rolls:
            if item == 1:
                total += item
        return total
    
    def deuces(self, rolls):
        total = 0
        for item in rolls:
            if item == 2:
                total += item
        return total
    
    def tres(self, rolls):
        total = 0
        for item in rolls:
            if item == 3:
                total += item
        return total
    
    def quads(self, rolls):
        total = 0
        for item in rolls:
            if item == 4:
                total += item
        return total
    
    def pentas(self, rolls):
        total = 0
        for item in rolls:
            if item == 5:
                total += item
        return total
    
    def hextas(self, rolls):
        total = 0
        for item in rolls:
            if item == 6:
                total += item
        return total
