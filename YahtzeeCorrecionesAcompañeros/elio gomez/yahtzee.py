class Yahtzee:

    @staticmethod
    def chance(d1, d2, d3, d4, d5):
        return d1 + d2 + d3 + d4 + d5

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
    def ones( d1,  d2,  d3,  d4,  d5):
        dados=[d1, d2, d3, d4, d5]
        return dados.count(1)
    

    @staticmethod
    def twos( d1,  d2,  d3,  d4,  d5):
        dados=[d1, d2, d3, d4, d5]
        return dados.count(2) *2
    
    @staticmethod
    def threes( d1,  d2,  d3,  d4,  d5):
        dados=[d1, d2, d3, d4, d5]
        return dados.count(3) *3
    

    def __init__(self, d1, d2, d3, d4, d5):
        self.dice = [d1, d2, d3, d4, d5]

    
    def fours(self):
        return self.dice.count(4) *4

    def fives(self):
        return self.dice.count(5) *5
    

    def sixes(self):
        return self.dice.count(6) *6

    @staticmethod
    def funcount(d1, d2, d3, d4, d5):
        counts = [0]*6
        counts[d1-1] += 1
        counts[d2-1] += 1
        counts[d3-1] += 1
        counts[d4-1] += 1
        counts[d5-1] += 1
        return counts

    @staticmethod
    def score_pair( d1,  d2,  d3,  d4,  d5):
        counts = Yahtzee.funcount(d1, d2, d3, d4, d5)
        for i in range(5,-1,-1):
            if (counts[i] == 2):
                return (i + 1)*2
        return 0
    
    @staticmethod
    def two_pair( d1,  d2,  d3,  d4,  d5):
        counts = Yahtzee.funcount(d1, d2, d3, d4, d5)
        n=0
        score = 0
        for i in range(6):
            if (counts[i] >= 2):
                n = n+1
                score += (i+1)                   
        if (n == 2):
            return score * 2
        else:
            return 0
    
    @staticmethod
    def four_of_a_kind( d1,  d2,  d3,  d4,  d5):
        lista = [d1, d2, d3, d4, d5]
        if lista.count(lista[0]) >= 4:
            return lista[0]*4
        elif lista.count(lista[1]) >= 4:
            return lista[1]*4
        else:
            return 0
    

    @staticmethod
    def three_of_a_kind( d1,  d2,  d3,  d4,  d5):
        lista = [d1, d2, d3, d4, d5]
        if lista.count(lista[0]) >= 3:
            return lista[0]*3
        elif lista.count(lista[1]) >= 3:
            return lista[1]*3
        elif lista.count(lista[2]) >= 3:
            return lista[2]*3
        else:
            return 0
    
    @staticmethod
    def smallStraight( d1,  d2,  d3,  d4,  d5):
        counts = Yahtzee.funcount(d1, d2, d3, d4, d5)
        if (counts[0] == 1 and
            counts[1] == 1 and
            counts[2] == 1 and
            counts[3] == 1 and
            counts[4] == 1):
            return 15
        return 0
    
    @staticmethod
    def largeStraight( d1,  d2,  d3,  d4,  d5):
        counts = Yahtzee.funcount(d1, d2, d3, d4, d5)
        if (counts[1] == 1 and
            counts[2] == 1 and
            counts[3] == 1 and
            counts[4] == 1
            and counts[5] == 1):
            return 20
        return 0

    @staticmethod
    def fullHouse( d1,  d2,  d3,  d4,  d5):
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        counts = Yahtzee.funcount(d1, d2, d3, d4, d5)

        for i in range(6):
            if (counts[i] == 2): 
                _2 = True
                _2_at = i+1
            

        for i in range(6):
            if (counts[i] == 3): 
                _3 = True
                _3_at = i+1
            

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0