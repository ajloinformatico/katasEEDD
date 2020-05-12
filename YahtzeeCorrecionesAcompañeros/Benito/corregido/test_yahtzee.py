import pytest
from yahtzee import Yahtzee

# These unit tests can be run using the py.test framework
# available from http://pytest.org/





def test_chance_scores_sum_of_all_dice():
    Game = Yahtzee(1,2,3,4,5) # Al formar el metodo parte 
                            # de la clase es necesario instanciarlo
                            # para probarlo
    expected = 15
    actual = Game.chance(2, 3, 4, 5, 1)
    assert expected == actual


def test_yahtzee_scores_50():
    Game = Yahtzee(1,2,3,4,5)# Al formar el metodo parte 
                            # de la clase es necesario instanciarlo
                            # para probarlo
    assert 50 == Game.yathzee_scores_50([4, 4, 4, 4, 4])
    assert 50 == Game.yathzee_scores_50([6, 6, 6, 6, 6])
    assert 0 == Game.yathzee_scores_50([6, 6, 6, 6, 3])


def test_1s_2s_3s():
    Game = Yahtzee(1,2,3,4,5)# Al formar el metodo parte 
                            # de la clase es necesario instanciarlo
                            # para probarlo
    
    # asserts for ones
    assert Game.ones_twos_threes([1, 2, 3, 4, 5],"ones") == 1
    assert 2 == Game.ones_twos_threes([1, 2, 1, 4, 5],"ones")
    assert 0 == Game.ones_twos_threes([6, 2, 2, 4, 5],"ones")
    assert 4 == Game.ones_twos_threes([1, 2, 1, 1, 1],"ones")
    # asserts for twos
    assert 4 == Game.ones_twos_threes([1, 2, 3, 2, 6],"twos")
    assert 10 == Game.ones_twos_threes([2, 2, 2, 2, 2],"twos")
    # asserts for threes
    assert 6 == Game.ones_twos_threes([1, 2, 3, 2, 3],"threes")
    assert 12 == Game.ones_twos_threes([2, 3, 3, 3, 3], "threes")


def test_fours_test():
    assert 12 == Yahtzee(4, 4, 4, 5, 5).fours()
    assert 8 == Yahtzee(4, 4, 5, 5, 5).fours()
    assert 4 == Yahtzee(4, 5, 5, 5, 5).fours()


def test_fives():
    assert 10 == Yahtzee(4, 4, 4, 5, 5).fives()
    assert 15 == Yahtzee(4, 4, 5, 5, 5).fives()
    assert 20 == Yahtzee(4, 5, 5, 5, 5).fives()


def test_sixes_test():
    assert 0 == Yahtzee(4, 4, 4, 5, 5).sixes()
    assert 6 == Yahtzee(4, 4, 6, 5, 5).sixes()
    assert 18 == Yahtzee(6, 5, 6, 6, 5).sixes()


def test_one_pair(): # modificado para pasar test modifica la lista counts que pertenece a la clase
    # y se comprueban las funciones que ahora son de la clase
    Game = Yahtzee(1,2,3,4,5)
    Game.make_list_counts(3, 4, 3, 5, 6)
    assert 6 == Game.score_pair()
    Game.make_list_counts(5, 3, 3, 3, 5)
    assert 10 == Game.score_pair()
    Game.make_list_counts(5, 3, 6, 6, 5)
    assert 12 == Game.score_pair()


def test_two_Pair():# modificado para pasar test modifica la lista counts que pertenece a la clase
    # y se comprueban las funciones que ahora son de la clase
    Game = Yahtzee(1,2,3,4,5)
    Game.make_list_counts(3, 3, 5, 4, 5)
    assert 16 == Game.two_pair()
    Game.make_list_counts(3, 3, 6, 6, 6)
    assert 18 == Game.two_pair()
    Game.make_list_counts(3, 3, 6, 5, 4)
    assert 0 == Game.two_pair()


def test_three_of_a_kind():
    assert 9 == Yahtzee.three_of_a_kind(3, 3, 3, 4, 5)
    assert 15 == Yahtzee.three_of_a_kind(5, 3, 5, 4, 5)
    assert 9 == Yahtzee.three_of_a_kind(3, 3, 3, 3, 5)


def test_four_of_a_knd():
    assert 12 == Yahtzee.four_of_a_kind(3, 3, 3, 3, 5)
    assert 20 == Yahtzee.four_of_a_kind(5, 5, 5, 4, 5)
    assert 12 == Yahtzee.four_of_a_kind(3, 3, 3, 3, 3)
    assert 0 == Yahtzee.four_of_a_kind(3, 3, 3, 2, 1)


def test_smallStraight():
    assert 15 == Yahtzee.smallStraight(1, 2, 3, 4, 5)
    assert 15 == Yahtzee.smallStraight(2, 3, 4, 5, 1)
    assert 0 == Yahtzee.smallStraight(1, 2, 2, 4, 5)


def test_largeStraight():
    assert 20 == Yahtzee.largeStraight(6, 2, 3, 4, 5)
    assert 20 == Yahtzee.largeStraight(2, 3, 4, 5, 6)
    assert 0 == Yahtzee.largeStraight(1, 2, 2, 4, 5)


def test_fullHouse():
    assert 18 == Yahtzee.fullHouse(6, 2, 2, 2, 6)
    assert 0 == Yahtzee.fullHouse(2, 3, 4, 5, 6)
