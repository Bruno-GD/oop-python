import pytest
from logging import getLogger as gL
LOGGER = gL(__name__)

from src.Yatzy import Yatzy

@pytest.mark.yatzy
def test_aces():
    assert Yatzy(1, 2, 3, 4, 5).aces() == 1
    assert Yatzy(1, 1, 3, 4, 5).aces() == 1*2
    assert Yatzy(1, 1, 1, 1, 1).aces() == 1*5

@pytest.mark.yatzy
def test_twos():
    assert Yatzy(1, 2, 3, 4, 5).twos() == 2
    assert Yatzy(2, 2, 3, 4, 5).twos() == 2*2
    assert Yatzy(2, 2, 2, 2, 2).twos() == 2*5

@pytest.mark.yatzy
def test_threes():
    assert Yatzy(1, 2, 3, 4, 5).threes() == 3
    assert Yatzy(1, 2, 3, 3, 5).threes() == 3*2
    assert Yatzy(3, 3, 3, 3, 3).threes() == 3*5

@pytest.mark.yatzy
def test_fours():
    assert Yatzy(1, 2, 3, 4, 5).fours() == 4
    assert Yatzy(1, 2, 4, 4, 5).fours() == 4*2
    assert Yatzy(4, 4, 4, 4, 4).fours() == 4*5

@pytest.mark.yatzy
def test_fives():
    assert Yatzy(1, 2, 3, 4, 5).fives() == 5
    assert Yatzy(1, 2, 3, 5, 5).fives() == 5*2
    assert Yatzy(5, 5, 5, 5, 5).fives() == 5*5

@pytest.mark.yatzy
def test_sixes():
    assert Yatzy(1, 2, 3, 4, 6).sixes() == 6
    assert Yatzy(1, 2, 3, 6, 6).sixes() == 6*2
    assert Yatzy(6, 6, 6, 6, 6).sixes() == 6*5

@pytest.mark.yatzy
def test_three_of_a_kind():
    assert Yatzy(1, 2, 3, 4, 5).three_of_a_kind() == 0
    assert Yatzy(1, 1, 1, 2, 3).three_of_a_kind() == sum([1, 1, 1, 2, 3])
    assert Yatzy(2, 2, 2, 2, 3).three_of_a_kind() == sum([2, 2, 2, 2, 3])

@pytest.mark.yatzy
def test_four_of_a_kind():
    assert Yatzy(1, 2, 3, 4, 5).four_of_a_kind() == 0
    assert Yatzy(1, 1, 1, 1, 3).four_of_a_kind() == sum([1, 1, 1, 1, 3])
    assert Yatzy(2, 2, 2, 2, 3).four_of_a_kind() == sum([2, 2, 2, 2, 3])

@pytest.mark.yatzy
def test_full_house():
    assert Yatzy(1, 1, 1, 2, 2).full_house() == 25
    assert Yatzy(1, 2, 3, 4, 5).full_house() == 0
    assert Yatzy(2, 2, 2, 3, 3).full_house() == 25
    assert Yatzy(2, 2, 2, 3, 4).full_house() == 0

@pytest.mark.yatzy
def test_small_straight():
    assert Yatzy(1, 2, 3, 4, 5).small_straight() == 30
    assert Yatzy(1, 1, 1, 1, 1).small_straight() == 0
    assert Yatzy(1, 2, 4, 5, 6).small_straight() == 0
    assert Yatzy(2, 2, 3, 4, 5).small_straight() == 30
    assert Yatzy(1, 1, 3, 4, 5).small_straight() == 0

@pytest.mark.yatzy
def test_large_straight():
    assert Yatzy(1, 2, 3, 4, 5).large_straight() == 40
    assert Yatzy(2, 3, 4, 5, 6).large_straight() == 40
    assert Yatzy(2, 3, 4, 5, 5).large_straight() == 0
    assert Yatzy(2, 3, 3, 5, 5).large_straight() == 0
    assert Yatzy(6, 3, 4, 5, 2).large_straight() == 40

@pytest.mark.yatzy
def test_yahtzee():
    assert Yatzy(1, 2, 3, 4, 5).yahtzee() == 0
    assert Yatzy(1, 1, 1, 1, 1).yahtzee() == 50
    assert Yatzy(2, 2, 2, 2, 2).yahtzee() == 50

@pytest.mark.yatzy
def test_chance():
    assert Yatzy(1, 2, 3, 4, 5).chance() == sum([1, 2, 3, 4, 5])
    assert Yatzy(2, 3, 1, 4, 5).chance() == sum([2, 3, 1, 4, 5])
    assert Yatzy(1, 1, 1, 1, 1).chance() == sum([1, 1, 1, 1, 1])
    assert Yatzy(2, 2, 3, 4, 1).chance() == sum([2, 2, 3, 4, 1])