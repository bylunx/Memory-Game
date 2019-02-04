# -*- coding: utf-8 -*-

import sys
import os
import pygame
from random import *
from Constantes import *
from Cartes import *

#Fonction pour retourner toutes les cartes
def retourner_tout(liste_objet):
    for objet in liste_objet:
        objet.retourner()

#On genere tout les sprites (cartes) aleatoirement
def generateur_sprite():
    memo = pygame.sprite.Group()
    liste_image = [ i for i in range(1, 9) ] * 2  #Creation d'une liste composee de toutes les cartes
    shuffle(liste_image)  # On melange le tout

    i = 0
    for x in range(0, 4):
        for y in range(0, 4):
            memo.add(Carte( liste_image[i], x, y ))  #On creer nos objet
            i += 1
    return memo


def main():

    # Initialisation de la librairie et de quelques paramètres
    pygame.init()
    size = width, height = 800, 600 # 1024, 768
    black = 0, 0, 0
    screen = pygame.display.set_mode(size)

    #Titre
    pygame.display.set_caption("Memory")

    #Chargement et collage du fond
    fond = pygame.image.load("./Images/background.png").convert()
    fond = pygame.transform.scale(fond,size)
    screen.blit(fond, (0,0))


    # Creation et mise en place des cartes : a vous de completer...
	#Boucle principale : action !
    clock = pygame.time.Clock()
    #Creation des sprites
    memo = generateur_sprite()

    liste_objet = []
    partie_terminee = False
    while 1:

        clock.tick(15)
        # Détection d'un événement (clic souris ou appui touche clavier) :
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN: #c'est un clic souris

            # On parcoure les objets au clic, si un objet est clique et qu'il n'est pas dans notre liste, on retourne l'objet.
                for objet in memo:
                    if ((objet.rect.collidepoint(event.pos)) and not (objet in liste_objet)):
                        if len(liste_objet) == 2: # Si notre liste comporte 2 objet, on retourne toutes les cartes.
                            retourner_tout(liste_objet)
                            liste_objet = []
                        retour_carte = objet.retourner()
                        liste_objet.append(objet)


            elif event.type == pygame.KEYDOWN: # C'est une touche clavier
                if event.key == pygame.K_ESCAPE:
                    sys.exit()      # Sortie du jeu
                    #Effacement de l'ancienne image
                elif event.key == pygame.K_RETURN:
                    if partie_terminee:
                        memo = generateur_sprite()
                        liste_objet = []
                        partie_terminee = False

            #Si 2 cartes sont retournee, on regarde leur numero, si ils sont les memes on supprime les cartes
        if len(liste_objet) == 2:
            if liste_objet[0].numero == liste_objet[1].numero:
                for objet in memo:
                    if liste_objet[0].numero == objet.numero:
                        memo.remove(objet)


        screen.blit(fond, (0,0))
        memo.update()
        memo.draw(screen)

        # en cas de victoire =(0 carte restantes) on affiche un message pour demander a l'utilisateur de rejouer
        if len(memo) == 0:
            myfont = pygame.font.SysFont("monospace", 46)
            myfont2 = pygame.font.SysFont("monospace", 30)
            label = myfont.render(u"Vous avez gagné", 1, (0,0,0))
            label2 = myfont2.render(u"Appuyez sur Entrée pour recommencer", 1, (0,0,0))
            screen.blit(label, (200, 250))
            screen.blit(label2, (100, 300))
            partie_terminee = True

        # Actualisation de l'écran
        pygame.display.flip()




if __name__ == '__main__':
    main()
