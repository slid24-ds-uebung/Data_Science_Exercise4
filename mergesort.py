"""Implementierung von Merge Sort mit Visualisierung der Sortierung.

Merge Sort ist ein Teile-und-herrsche-Algorithmus: Die Liste wird
rekursiv halbiert, bis nur noch Einzelelemente uebrig sind, und die
sortierten Haelften werden anschliessend wieder zusammengefuehrt.
Die Laufzeit ist O(n log n).
"""

import matplotlib.pyplot as plt


def merge_sort(values: list[int]) -> None:
    """Sortiert ``values`` aufsteigend in-place.

    Args:
        values: Die zu sortierende Liste. Sie wird direkt veraendert.
    """
    # Eine Liste mit 0 oder 1 Element ist bereits sortiert (Basisfall).
    if len(values) <= 1:
        return

    mid = len(values) // 2
    left = values[:mid]
    right = values[mid:]

    # Beide Haelften rekursiv sortieren.
    merge_sort(left)
    merge_sort(right)

    # Die beiden sortierten Haelften zu values zusammenfuehren.
    left_index = 0
    right_index = 0
    merged_index = 0

    # Solange beide Haelften Elemente haben, das kleinere uebernehmen.
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            values[merged_index] = left[left_index]
            left_index += 1
        else:
            values[merged_index] = right[right_index]
            right_index += 1
        merged_index += 1

    # Restliche Elemente der linken Haelfte anhaengen.
    while left_index < len(left):
        values[merged_index] = left[left_index]
        left_index += 1
        merged_index += 1

    # Restliche Elemente der rechten Haelfte anhaengen.
    while right_index < len(right):
        values[merged_index] = right[right_index]
        right_index += 1
        merged_index += 1


def plot_values(values: list[int], title: str) -> None:
    """Stellt die Werte als Balkendiagramm dar.

    Ein Balkendiagramm passt hier besser als ein Liniendiagramm: Die
    Werte sind unabhaengige Einzelwerte an diskreten Positionen, keine
    zusammenhaengende Kurve.

    Args:
        values: Die darzustellenden Werte.
        title: Titel des Diagramms.
    """
    positions = range(len(values))
    plt.bar(positions, values)
    plt.title(title)
    plt.xlabel("Index")
    plt.ylabel("Wert")
    plt.show()


if __name__ == "__main__":
    numbers = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    plot_values(numbers, "Vor dem Sortieren")
    merge_sort(numbers)
    plot_values(numbers, "Nach dem Sortieren")
