#!/usr/bin/python3
"""
island parameter
"""


def island_perimeter(grid):
    """
    island perimeter
    """
    width = len(grid[0])
    height = len(grid)
    edges = 0
    size = 0
    # parcourir chaque ligne de la grille
    for ligne in range(height):
        # parcourir chaque colonne de la grille
        for colonne in range(width):
            # si la cellule est un morceau de terre
            if grid[ligne][colonne] == 1:
                # vérifier si la cellule est à l'intérieur de la grille
                size += 1
                if (colonne > 0 and grid[ligne][colonne - 1] == 1):
                    edges += 1
                if (ligne > 0 and grid[ligne - 1][colonne] == 1):
                    edges += 1
    return size * 4 - edges * 2
