# -*- coding: utf-8 -*-

import pygame
from connection import *
from constants import *


SCREEN = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Duel Monsters')

global HAND
global GRAVE
global ACTIVEPHASE
global DECK
global FIELD
global P2HAND
global P2GRAVE
global P2DECK
global P2FIELD
global SummonedMonsters
global LP
global P2LP
global EPEffects


HAND = []
GRAVE = []
DECK = []
FIELD = []
P2HAND = []
P2GRAVE = []
P2DECK = []
P2FIELD = []
EPEffects = []
LP = 8000
P2LP = 8000
ACTIVEPHASE = 'Draw Phase'
SummonedMonsters = 0


#print 'inicio -- ', LP, P2LP


def CheckMouseOver((Startx, Starty), (Sizex, Sizey)):    
    Rect = pygame.Rect(Startx, Starty, Sizex, Sizey)
   # print LP, P2LP
    if Rect.collidepoint(pygame.mouse.get_pos()):
        return True
    else:
        return False
    

def GoToGrave(card, field, grave):
    if field == P2FIELD:
        spot = P2GRAVESPOT
    else:
        spot = GRAVESPOT

    #card.img = pygame.transform.scale(card.imgLoad, CARDSIZE)
    SCREEN.blit(card.img, spot )
    field.remove(card)
    grave.append(card)

def CalcPoints(player, points):
    global LP
    global P2LP
    if player == 'P2':
        P2LP += points
    else:
        LP += points

def DrawStatusBar(NameP1, NameP2):
    # --- Desenha a barra de status contendo o Nome dos jogadores
    # --- e seus respectivos pontos de vida (LP)
    global LP
    global P2LP

    # Define tipos e tamanhos de fonte
    NameFont = pygame.font.Font('freesansbold.ttf', 16)
    LpFont = pygame.font.Font('freesansbold.ttf', 22)

    # Player 1 StatusBar
    # Barra
    STATUSBARP2 = pygame.draw.rect(SCREEN, LIGHTBLUE, (INFOSIZE[0], 0, STATUSSIZE[0], STATUSSIZE[1]))
    pygame.draw.rect(SCREEN, DARKBLUE, (INFOSIZE[0], 0, STATUSSIZE[0], STATUSSIZE[1]), 4)
    
    # Nome
    space = GetTextCenter(NameP1)
    textObj = NameFont.render(NameP1, True, BLACK)                    # define o texto e a cor
    textRect = textObj.get_rect()                                     # pega o espaço ocupado 
    textRect.center = (INFOSIZE[0] +  space, (STATUSSIZE[1] / 2))     # define a posição do ponto central dotexto 
    SCREEN.blit(textObj, textRect)                                    # desenha o texto na tela

    # Pontos
    textObj = LpFont.render(str(LP), True, BLACK)
    #print 'dentro da funcao -- ', LP
    textRect = textObj.get_rect()
    textRect.center = (INFOSIZE[0] + (STATUSSIZE[0] - 35), (STATUSSIZE[1] / 2)) 
    SCREEN.blit(textObj, textRect)
    

    # Player 2 StatusBar
    x = INFOSIZE[0] + STATUSSIZE[0] + STATUSSIZE[2]
    
    STATUSBARP1 = pygame.draw.rect(SCREEN, LIGHTBLUE, (x , 0, STATUSSIZE[0], STATUSSIZE[1]))
    pygame.draw.rect(SCREEN, DARKBLUE, (x , 0, STATUSSIZE[0], STATUSSIZE[1]), 4)

    # Nome
    space = GetTextCenter(NameP2)
    textObj = NameFont.render(NameP2, True, BLACK)
    textRect = textObj.get_rect()
    textRect.center = (INFOSIZE[0] + (STATUSSIZE[0]* 2) - space + STATUSSIZE[2] , (STATUSSIZE[1] / 2))
    SCREEN.blit(textObj, textRect)
    
    # Pontos
    textObj = LpFont.render(str(P2LP), True, BLACK)
    #print 'dentro da funcao -- ', P2LP
    textRect = textObj.get_rect()
    textRect.center = (INFOSIZE[0] + STATUSSIZE[0] + STATUSSIZE[2] + 35), (STATUSSIZE[1] / 2)
    SCREEN.blit(textObj, textRect)
    

def GetTextCenter(nome):
    # --- Define o espaço em px conforme o tamanho do nome
    # --- para que o nome fique ajustado a esquerda(P1) ou direita(P2)
    if len(nome) <= 3:
        return 30
    elif (len(nome) > 3) and (len(nome) < 10):
        return 50
    elif (len(nome) >= 10) and (len(nome) < 15):
        return 70
    elif (len(nome) >= 15) and (len(nome) < 20):
        return 100
    else:
        return 120


def ShowMessage(msg, tipo):
    Font = pygame.font.Font('freesansbold.ttf', 16)
    BtnFont = pygame.font.Font('freesansbold.ttf', 20)

    rect = pygame.draw.rect(SCREEN, BLACK, (350, 150, 350, 150))
    pygame.draw.rect(SCREEN, BLUE, (360, 160, 330, 130), 4)

    msg = msg.split()
    line = ''
    lines = []
        
    for word in msg[:]:
        if (len(line + word)) <= 35:
                line += word + ' '
                msg.remove(word)
                if len(msg) == 0:
                        lines.append(line)
        else:
                lines.append(line)
                msg.remove(word)
                line = word + ' '
                if len(msg) == 0:
                        lines.append(line)

    print rect.center
    y = 150 + rect[1] /2 - (rect[1]/4)
    for line in lines:
        textObj = Font.render(line, True, GRAY)
        textRect = textObj.get_rect()
        textRect.center = (350 + rect[0] /2 , y)
        SCREEN.blit(textObj, textRect)
        y += 20
        
    if tipo == 'Pergunta':
        btnYes = pygame.draw.rect(SCREEN, LIGHTBLUE, (350 + rect[0] /4, 150 + rect[1] /1.5, 70, 30))
        pygame.draw.rect(SCREEN, DARKBLUE, (btnYes), 3)

        textObj = Font.render('SIM', True, RED)
        textRect = textObj.get_rect()
        textRect.center = (btnYes.center)
        SCREEN.blit(textObj, textRect)

        btnNo = pygame.draw.rect(SCREEN, LIGHTBLUE, (360 + rect[0] /2, 150 + rect[1] /1.5, 70, 30))
        pygame.draw.rect(SCREEN, DARKBLUE, (btnNo), 3)

        textObj = Font.render('NAO', True, RED)
        textRect = textObj.get_rect()
        textRect.center = (btnNo.center)
        SCREEN.blit(textObj, textRect)

        pygame.display.update()
        
        while True:
            if pygame.event.wait().type == MOUSEBUTTONDOWN:
                if CheckMouseOver((btnYes[0], btnYes[1]),(btnYes[2], btnYes[3])):
                    return True
                    break
                elif CheckMouseOver((btnNo[0], btnNo[1]),(btnNo[2], btnNo[3])):
                    return False
                    break

    elif tipo == 'Exclamacao':
        btnOk = pygame.draw.rect(SCREEN, LIGHTBLUE, (370 + rect[0] /3, 150 + rect[1] /1.5, 70, 30))
        pygame.draw.rect(SCREEN, DARKBLUE, (btnOk), 3)

        textObj = Font.render('OK', True, RED)
        textRect = textObj.get_rect()
        textRect.center = (btnOk.center)
        SCREEN.blit(textObj, textRect)

        pygame.display.update()

        while True:
            if pygame.event.wait().type == MOUSEBUTTONDOWN:
                if CheckMouseOver((btnOk[0], btnOk[1]),(btnOk[2], btnOk[3])):
                    return True
                    break

def drawField():
    # --- Desenhando linhas que definem o campo
    # --- sintax = pygame.draw.line(Surface, color, start_pos, end_pos, width=1)
    Font = pygame.font.Font('freesansbold.ttf', 10)
    # Player 1
    xInicial = (INFOSIZE[0] + 25)
    yInicial = (FIELDSIZE[1] + PHASESIZE[1] + 65 + STATUSSIZE[1])
    xFinal = (INFOSIZE[0] + 20 + FIELDSIZE[0] + 6)
    yFinal = ((FIELDSIZE[1] * 2) + PHASESIZE[1] + 65 + STATUSSIZE[1])
    
    pygame.draw.rect(SCREEN, BLACK, (xInicial, yInicial, FIELDSIZE[0], FIELDSIZE[1]))
    for x in range(xInicial, xFinal, CARDSIZE[1] + 4):
        pygame.draw.line(SCREEN, BLUE,(x, yInicial),(x, yFinal), 4)
        pygame.draw.line(SCREEN, DARKBLUE,(x, yInicial),(x, yFinal), 2)
        
    for y in range(yInicial, yFinal, FIELDSIZE[1] / 2 - 1):
        pygame.draw.line(SCREEN, BLUE,(xInicial, y),(xFinal, y), 4)
        pygame.draw.line(SCREEN, DARKBLUE,(xInicial, y),(xFinal, y), 2)

    for card in FIELD:
        SCREEN.blit(card.img, card.pixPosition)
        if card.category == 'Monster':
            textObj = Font.render(str(card.ATK) + ' | ' + str(card.DEF), True, WHITE)
            textRect = textObj.get_rect()
            textRect.center = (card.pixPosition[0] + (card.size[0] / 2), card.pixPosition[1] + (card.size[1] + 8))
            SCREEN.blit(textObj, textRect)

    DrawDeck()

    # Player 2 
    xInicial = (INFOSIZE[0] + 25)
    yInicial = (STATUSSIZE[1] + 60)
    xFinal = (INFOSIZE[0] + 20 + FIELDSIZE[0] + 6)
    yFinal = (FIELDSIZE[1] + STATUSSIZE[1] + 60)

    pygame.draw.rect(SCREEN, BLACK, (xInicial, yInicial, FIELDSIZE[0], FIELDSIZE[1]))
    for x in range(xInicial, xFinal, CARDSIZE[1] + 4):
        pygame.draw.line(SCREEN, BLUE,(x, yInicial),(x, yFinal), 4)
        pygame.draw.line(SCREEN, DARKBLUE,(x, yInicial),(x, yFinal), 2)
        
    for y in range(yInicial, yFinal, FIELDSIZE[1] / 2 - 1):
        pygame.draw.line(SCREEN, BLUE,(xInicial, y),(xFinal, y), 4)
        pygame.draw.line(SCREEN, DARKBLUE,(xInicial, y),(xFinal, y), 2)

    for card in P2FIELD:
        SCREEN.blit(card.img, card.pixPosition)
        if card.category == 'Monster':
            textObj = Font.render(str(card.ATK) + ' | ' + str(card.DEF), True, WHITE)
            textRect = textObj.get_rect()
            textRect.center = (card.pixPosition[0] + (card.size[0] / 2), card.pixPosition[1] - 6)
            SCREEN.blit(textObj, textRect)

    DrawGrave()

def DrawGrave():
    if len(GRAVE) != 0:
        card = GRAVE[-1]
        #card.img = pygame.transform.scale(card.imgLoad, CARDSIZE)
        SCREEN.blit(card.img, GRAVESPOT)

    if len(P2GRAVE) != 0:
        card = P2GRAVE[-1]
        #card.img = pygame.transform.scale(card.imgLoad, CARDSIZE)
        SCREEN.blit(card.img, P2GRAVESPOT)

def DrawDeck():
    Font = pygame.font.Font('freesansbold.ttf', 40)
    
    img = pygame.image.load('yugi_lib/images/cards/bmp/BackCard.bmp')
    img = pygame.transform.scale(img, CARDSIZE)

    if len(DECK) > 40:
        n = 5
    elif len(DECK) < 40 and len(DECK) >= 20:
        n = 4
    elif len(DECK) < 20 and len(DECK) >= 6:
        n = 3
    elif len(DECK) < 6 and len(DECK) > 1:
        n = 2
    else:
        n = 1    

    x = 0
    y = -5
    for i in range(n):
        SCREEN.blit(img, (DECKSPOT[0] + x, DECKSPOT[1] + y))
        x += 1
        y -= 1

    textObj = Font.render(str(len(DECK)), True, BROWN)
    textRect = textObj.get_rect()
    textRect.center = (DECKSPOT[0] + (CARDSIZE[0] / 2) + x, DECKSPOT[1] + CARDSIZE[1] /2)
    SCREEN.blit(textObj, textRect)

def RemoveEffects():
    for effect in EPEffects[:]:
        if effect[0] == 'Reinforcements':
            card = effect[1]
            card.ATK -= 500

        EPEffects.remove(effect)

        
        
