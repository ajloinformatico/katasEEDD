### 1º
# La ubicacón del codigo no es la más asecudada

### 2º
# No hay ingun comentario en ninguna función

### 3º
# La función chance revibe 5 dados y los suma si es la suma de 5 dados se podfria
# simplement recibir self y sumar los dados de seff
class Yahtzee:

    @staticmethod # podria ser un metodo de la clase
    def chance(d1, d2, d3, d4, d5):
        return d1 + d2 + d3 + d4 + d5

    @staticmethod
    def yathzee_scores_50(lista):
        if lista.count(lista[0]) == 5:
            return 50
        else:
            return 0

    @staticmethod
    def ones(d1, d2, d3, d4, d5):
        lista = (d1, d2, d3, d4, d5)
        return lista.count(1)

    @staticmethod
    def twos(d1, d2, d3, d4, d5):
        lista = (d1, d2, d3, d4, d5)
        return lista.count(2)*2

    @staticmethod
    def threes(d1, d2, d3, d4, d5):
        lista = (d1, d2, d3, d4, d5)
        return lista.count(3)*3

    def __init__(self, d1, d2, d3, d4, d5): # debe ir al principio de la clase
        self.dice = [d1, d2, d3, d4, d5]

    def fours(self):
        return self.dice.count(4)*4

    def fives(self):
        return self.dice.count(5)*5

    def sixes(self):
        return self.dice.count(6)*6

    @staticmethod
    def score_pair(d1,  d2,  d3,  d4,  d5):
        counts = [0]*6
        counts[d1-1] += 1
        counts[d2-1] += 1
        counts[d3-1] += 1
        counts[d4-1] += 1
        counts[d5-1] += 1
        at = 0
        for at in range(6):
            if (counts[6-at-1] == 2):
                return (6-at)*2
        return 0

    @staticmethod
    def two_pair(d1,  d2,  d3,  d4,  d5):
        counts = [0]*6
        counts[d1-1] += 1
        counts[d2-1] += 1
        counts[d3-1] += 1
        counts[d4-1] += 1
        counts[d5-1] += 1
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
    def four_of_a_kind(d1,  d2,  d3,  d4,  d5):
        lista = [d1, d2, d3, d4, d5]
        if lista.count(lista[0]) >= 4:
            return lista[0]*4
        elif lista.count(lista[1]) >= 4:
            return lista[1]*4
        else:
            return 0

    @staticmethod
    def three_of_a_kind(d1,  d2,  d3,  d4,  d5):
        lista = [d1, d2, d3, d4, d5]
        if lista.count(lista[0]) >= 3:
            return lista[0]*3
        elif lista.count(lista[1]) >= 3:
            return lista[1]*3
        else:
            return 0

    @staticmethod
    def smallStraight(d1,  d2,  d3,  d4,  d5):
        if sorted((d1, d2, d3, d4, d5)) == [1, 2, 3, 4, 5]:
            return 15
        else: 
            return 0

    @staticmethod
    def largeStraight(d1,  d2,  d3,  d4,  d5):
        if sorted((d1, d2, d3, d4, d5 )) == [2,3,4,5,6]: 
            return 20 
        else: 
            return 0
        

    @staticmethod
    def fullHouse(d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2):
                _2 = True
                _2_at = i+1

        for i in range(6):
            if (tallies[i] == 3):
                _3 = True
                _3_at = i+1

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0