#!/usr/bin/env python3

def island_perimeter(grid):
    """
    island perimeter
    """
    perimetre = 0
    # parcourir chaque ligne de la grille
    for ligne in range(len(grid)):
        # parcourir chaque colonne de la grille
        for colonne in range(len(grid[ligne])):
            # si la cellule est un morceau de terre
            if grid[ligne][colonne] == 1:
                # vérifier si la cellule est à l'intérieur de la grille
                voisins = 0
                if ligne > 0 and grid[ligne - 1][colonne] == 0:
                    voisins += 1
                if ligne < len(grid) - 1 and grid[ligne + 1][colonne] == 0:
                    voisins += 1
                if colonne > 0 and grid[ligne][colonne - 1] == 0:
                    voisins += 1
                if colonne < len(grid[ligne]) - 1:
                    if grid[ligne][colonne + 1] == 0:
                        voisins += 1
                perimetre += voisins
    return perimetre
