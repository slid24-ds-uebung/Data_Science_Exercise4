"""Findet das einzelne Element in einer Liste, in der alle anderen
Elemente genau zweimal vorkommen."""


def find_single_element(numbers: list[int]) -> int:
    """Gibt das Element zurueck, das genau einmal vorkommt.

    Alle Elemente in ``numbers`` kommen genau zweimal vor, ausser einem,
    das nur einmal vorkommt. Dieses einzelne Element wird zurueckgegeben.

    Die Loesung nutzt den XOR-Operator (``^``):
        * ``x ^ x == 0``  (ein Wert hebt sich selbst auf)
        * ``x ^ 0 == x``  (XOR mit 0 laesst einen Wert unveraendert)
    XOR-t man alle Zahlen, heben sich alle Paare auf und nur der
    einzelne Wert bleibt uebrig. Laufzeit O(n), Speicher O(1).
    """
    if not isinstance(numbers, list):
        raise TypeError("Eingabe muss eine Liste sein.")
    if len(numbers) == 0:
        raise ValueError("Liste darf nicht leer sein.")
    if len(numbers) % 2 == 0:
        raise ValueError("Liste muss ungerade Laenge haben.")
    if not all(isinstance(value, int) for value in numbers):
        raise TypeError("Alle Elemente muessen Integer sein.")

    result = 0
    for value in numbers:
        result ^= value
    return result