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


def plot_before_after(values: list[int]) -> None:
    """Zeigt die Werte vor und nach dem Sortieren als Balkendiagramme.

    Ein Balkendiagramm passt hier besser als ein Liniendiagramm: Die
    Werte sind unabhaengige Einzelwerte an diskreten Positionen, keine
    zusammenhaengende Kurve. Beide Diagramme werden zum direkten
    Vergleich nebeneinander in einer Figur dargestellt.

    Args:
        values: Die darzustellenden Werte (wird nicht veraendert).
    """
    sorted_values = values.copy()
    merge_sort(sorted_values)

    positions = range(len(values))
    figure, (axis_before, axis_after) = plt.subplots(1, 2, figsize=(10, 4))

    axis_before.bar(positions, values)
    axis_before.set_title("Vor dem Sortieren")
    axis_before.set_xlabel("Index")
    axis_before.set_ylabel("Wert")

    axis_after.bar(positions, sorted_values)
    axis_after.set_title("Nach dem Sortieren")
    axis_after.set_xlabel("Index")
    axis_after.set_ylabel("Wert")

    figure.tight_layout()
    plt.show()


if __name__ == "__main__":
    numbers = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    plot_before_after(numbers)
