class Yahtzee:

    @staticmethod
    def chance(d1, d2, d3, d4, d5):
        total = 0
        lista = (d1, d2, d3, d4, d5)
        for i in lista:
            total += i
        return total

    @staticmethod
    def yahtzee(dice):
        counts = [0]*(len(dice)+1)
        for die in dice:
            counts[die-1] += 1
        for i in range(len(counts)):
            if counts[i] == 5:
                return 50
        return 0
    
    @staticmethod
    def ones(d1, d2, d3, d4, d5):
        sum = 0
        lista = (d1, d2, d3, d4, d5)
        for i in lista:
            if i == 1:
                sum += 1
        return sum
    

    @staticmethod
    def twos(d1, d2, d3, d4, d5):
        sum = 0
        lista = (d1, d2, d3, d4, d5)
        for i in lista:
            if i == 2:
                sum += 2
        return sum

    @staticmethod
    def threes(d1, d2, d3, d4, d5):
        sum = 0
        lista = (d1, d2, d3, d4, d5)
        for i in lista:
            if i == 3:
                sum += 3
        return sum


    def __init__(self, d1, d2, d3, d4, d5):
        self.dice = [0]*5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = d5
    
    def fours(self):
        sum = 0
        for i in range(5):
            if (self.dice[i] == 4): 
                sum += 4
        return sum
    
    def fives(self):
        sum = 0
        for i in range(5):
            if (self.dice[i] == 5): 
                sum += 5
        return sum
    
    def sixes(self):
        sum = 0
        for i in range(5):
            if (self.dice[i] == 6): 
                sum += 6
        return sum
    
    @staticmethod
    def score_pair( d1,  d2,  d3,  d4,  d5):
        counts = [0]*6
        lista = (d1, d2, d3, d4, d5)
        for i in lista:
            counts[i-1] += 1
        for e in range(6):
            if (counts[6-e-1] == 2):
                return (6-e)*2
        return 0
    
    @staticmethod
    def two_pair( d1,  d2,  d3,  d4,  d5):
        counts = [0]*6
        lista = (d1, d2, d3, d4, d5)
        for i in lista:
            counts[i-1] += 1
        n = 0
        score = 0
        for i in range(6):
            if (counts[6-i-1] >= 2):
                n = n+1
                score += (6-i)
        if (n == 2):
            return score * 2
        else:
            return 0
    
    @staticmethod
    def four_of_a_kind( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        lista = (d1, d2, d3, d4, d5)
        for i in lista:
            tallies[i-1] += 1
        for i in range(6):
            if (tallies[i] >= 4):
                return (i+1) * 4
        return 0
    

    @staticmethod
    def three_of_a_kind( d1,  d2,  d3,  d4,  d5):
        t = [0]*6
        lista = (d1, d2, d3, d4, d5)
        for i in lista:
            t[i-1] += 1
        for i in range(6):
            if (t[i] >= 3):
                return (i+1) * 3
        return 0
    
    @staticmethod
    def smallStraight(d1, d2, d3, d4, d5):
        tallies = [0]*6
        lista = (d1, d2, d3, d4, d5)
        for i in lista:
            tallies[i-1] += 1
        if (tallies[0] == 1 and
            tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1):
            return 15
        return 0

    @staticmethod
    def largeStraight(d1, d2, d3, d4, d5):
        tallies = [0]*6
        lista = (d1, d2, d3, d4, d5)
        for i in lista:
            tallies[i-1] += 1
        if (tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1 and
            tallies[5] == 1):
            return 20
        return 0
    
    @staticmethod
    def fullHouse(d1, d2, d3, d4, d5):
        var1 = False
        i = 0
        sum1 = 0
        var2 = False
        sum2 = 0
        tallies = [0]*6
        lista = (d1, d2, d3, d4, d5)
        for i in lista:
            tallies[i-1] += 1

        for i in range(6):
            if (tallies[i] == 2): 
                var1 = True
                sum1 = i+1

        for i in range(6):
            if (tallies[i] == 3): 
                var2 = True
                sum2 = i+1

        if (var1 and var2):
            return sum1 * 2 + sum2 * 3
        else:
            return 0
