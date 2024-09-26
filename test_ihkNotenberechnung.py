import pytest
from ihkNotenBerechnung import ihk_noten_schriftlich
from ihkNotenBerechnung import ihk_prozent_wertcalc

def test_ihk_prozent_wertcalc__failedErrorType():
    test_erreichtenPunkte = "ens"
    test_moeglichenPunkte = "le"
    with pytest.raises(TypeError):
        ihk_prozent_wertcalc(test_erreichtenPunkte, test_moeglichenPunkte)

def test_ihk_prozent_wertcalc__failedErrorValue():
    test_erreichtenPunkte : int  = -15
    test_moeglichenPunkte : int = 1
    with pytest.raises(ValueError):
        ihk_prozent_wertcalc(test_erreichtenPunkte, test_moeglichenPunkte)

def test_ihk_prozent_wertcalc__grosserAlsMoeglichen():
    test_erreichtenPunkte : int = 101
    test_moeglichenPunkte :int = 100
    with pytest.raises(ValueError):
        ihk_prozent_wertcalc(test_erreichtenPunkte, test_moeglichenPunkte)

def test_ihk_prozent_wertcalc__bestandenTest():
    test_erreichtenPunkte : int = 90
    test_moeglichenPunkte : int = 100
    soll_ergebnis = 90
    ist_ergebnis = ihk_prozent_wertcalc(test_erreichtenPunkte , test_moeglichenPunkte)
    print(ist_ergebnis)
    assert soll_ergebnis == ist_ergebnis


def test_ihk_noten_schriftlich__typeError():
    test_prozent = "ensar"
    with pytest.raises(TypeError):
        ihk_noten_schriftlich(test_prozent)

def test_ihk_noten_schriftlich__sehrGut():
    test_prozent : int = 95
    soll_ergebnis = "sehr gut"
    ist_ergebnis = ihk_noten_schriftlich(test_prozent)
    assert ist_ergebnis == soll_ergebnis

def test_ihk_noten_schriftlich__gut():
    test_prozent : int = 85
    soll_ergebnis = "gut"
    ist_ergebnis = ihk_noten_schriftlich(test_prozent)
    assert ist_ergebnis == soll_ergebnis

def test_ihk_noten_schriftlich__befriedigend():
    test_prozent : int = 75
    soll_ergebnis = "befriedigend"
    ist_ergebnis = ihk_noten_schriftlich(test_prozent)
    assert ist_ergebnis == soll_ergebnis

def test_ihk_noten_schriftlich__ausreichend():
    test_prozent : int = 60 
    soll_ergebnis = "ausreichend"
    ist_ergebnis = ihk_noten_schriftlich(test_prozent)
    assert ist_ergebnis == soll_ergebnis


def test_ihk_noten_schriftlich__mangelhaft():
    test_prozent : int = 40 
    soll_ergebnis = "mangelhaft"
    ist_ergebnis = ihk_noten_schriftlich(test_prozent)
    assert ist_ergebnis == soll_ergebnis


def test_ihk_noten_schriftlich__ungenügend():
    test_prozent : int = 25 
    soll_ergebnis = "ungenügend"
    ist_ergebnis = ihk_noten_schriftlich(test_prozent)
    assert ist_ergebnis == soll_ergebnis

def test_ihk_noten_schriftlich__valueError():
    test_prozent : int = 101 
    with pytest.raises(ValueError):
        ihk_noten_schriftlich(test_prozent)
