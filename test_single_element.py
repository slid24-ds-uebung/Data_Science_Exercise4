"""Testfaelle fuer find_single_element (Ausfuehren mit: pytest)."""

import pytest

from single_element import find_single_element


def test_beispiel_aus_aufgabe():
    assert find_single_element([1, 2, 3, 4, 3, 1, 2]) == 4


def test_nur_ein_element():
    assert find_single_element([7]) == 7


def test_einzelnes_element_am_anfang():
    assert find_single_element([9, 1, 1, 2, 2]) == 9


def test_mit_negativen_zahlen():
    assert find_single_element([-3, 5, 5, -3, -8]) == -8


def test_mit_null_als_einzelnem_wert():
    assert find_single_element([0, 4, 4, 6, 6]) == 0


def test_groessere_unsortierte_eingabe():
    assert find_single_element([10, 22, 10, 99, 22, 5, 5]) == 99


def test_leere_liste_wirft_fehler():
    with pytest.raises(ValueError):
        find_single_element([])


def test_gerade_laenge_wirft_fehler():
    with pytest.raises(ValueError):
        find_single_element([1, 1, 2, 2])


def test_keine_liste_wirft_fehler():
    with pytest.raises(TypeError):
        find_single_element("123")


def test_nicht_integer_wirft_fehler():
    with pytest.raises(TypeError):
        find_single_element([1, 1, 2.5])