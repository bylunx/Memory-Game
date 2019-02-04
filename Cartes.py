#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import pygame
from Constantes import *

class Carte(pygame.sprite.Sprite):

    def __init__(self, numero, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.numero = numero
        self.__image_recto = pygame.image.load("Images/image{}.png".format(numero))
        self.__image_verso = pygame.image.load("Images/dos_de_carte.png")
        self.image = self.__image_verso
        self.rect = self.__image_verso.get_rect()
        self.coord_x = 45 + x * LARGEUR_CARTE
        self.coord_y = 20 + y * HAUTEUR_CARTE
        self.rect.topleft = (self.coord_x, self.coord_y)

    def update(self):
        pygame.sprite.Sprite.update(self)

    def retourner(self):
        if self.image == self.__image_verso:
            self.image = self.__image_recto
            return self.numero
        else:
            self.image = self.__image_verso
            return CACHE
