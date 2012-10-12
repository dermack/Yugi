# -*- coding: utf-8 -*-
import pygame
import sys
import random
import thread
import time
import socket
import logging
import functions
import connection
import threading

from pygame.locals import *
from constants import *
#from connection import *
#from classe import *
from utils import *
from datetime import datetime
from threading import Thread
from sys import argv


Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Socket.connect(('localhost', 1234))
print 'Conectado...'

USER = argv[0]
PASSWD = argv[1]

pygame.init()
fpsClock = pygame.time.Clock()

# set up the window    


def main():
    global Player1Info
    global Player2Info
    global P1CardList
    global P2CardList
    global P2choose
    global FIRST

    thr = ThReceive(Socket)
    thr.start()
    
    Player1Info = GetUserInfo(USER, PASSWD)
    #Player2Info = GetUserInfo('Dracke', '123')
    GerarImagens(Player1Info[0])
    while Player2Info == []:
        print "aguardando conexão..."
    
    GerarImagens(Player2Info[0])
    user = (str(Player1Info[0]) + '|' + Player1Info[1] + '|' + Player1Info[2])
    # Descrição de UserInfo
    # UserInfo[0] = ID
    # UserInfo[1] = Nome
    # UserInfo[2] = Nick
    # UserInfo[3] = Senha (criptografada)
    # UserInfo[4] = E-mail

    '''while True:
        OptionList = DrawJanken()
        pygame.display.update()
        fpsClock.tick(FPS)
        
        P1choose = None
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if P1choose == None:
                    P1choose = ClickJanken(OptionList)
                Socket.send(choose)

        pygame.display.update()
        fpsClock.tick(FPS)

        if (P1choose != None) and (P2choose != None):
            winner = CheckJanken(P1choose, P2choose)
            
            if winner == P1choose:
                OptionList = DrawGetFirst(P2choose)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == MOUSEBUTTONDOWN:
                        if FIRST == None:
                            FIRST = ClickJanken(OptionList)
                Socket.send(FIRST)
            elif winner == P2choose:
                WaitForFirst()
            elif winner == None:
                pass'''
        
        
    

    P1CardList = GetUserCards(Player1Info[0])
    P2CardList = GetUserCards(Player2Info[0])
    
    

    StartGame()
    print 'Start ', LP, P2LP
    


    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='log/lala.log',
                    level=logging.DEBUG)
    
    while True:

        print threading.activeCount()
        
        
        checkForQuit()
        for event in pygame.event.get():
            if event.type == QUIT:
                print 'Saindo...'
                pygame.quit()
                sys.exit()
                Socket.close()
                thr.stop = True
            elif event.type == MOUSEBUTTONDOWN:
                OnClick()
                
        
        GetCardInfo()
        DrawPhaseSeq()

        pygame.display.update()
        



    #DrawStatusBar(Player1Info[2], Player2Info[2])
         

def DrawInfoBar():
    # --- Desenha a barra de informações contendo a carta
    # --- selecionada e sua descrição
    
    # Define Fontes
    Title = pygame.font.Font('freesansbold.ttf', 14)
    TextFont = pygame.font.Font('freesansbold.ttf', 10)
    
    # InfoBar
    INFOBAR = pygame.draw.rect(SCREEN, BLUE, (0, 0, INFOSIZE[0], INFOSIZE[1]))
    INFOBORDER = pygame.draw.rect(SCREEN, DARKBLUE, (0, 0, INFOSIZE[0], INFOSIZE[1]), 6)

    # InfoBar Descricao
    INFOTEXT = pygame.draw.rect(SCREEN, LIGHTBLUE, (10, 45 + CARDINFOSIZE[1] , INFOTEXTSIZE[0], INFOTEXTSIZE[1]))
    INFOTEXTBORDER = pygame.draw.rect(SCREEN, DARKBLUE, (10, 45 + CARDINFOSIZE[1] , INFOTEXTSIZE[0], INFOTEXTSIZE[1]), 3)
    pygame.draw.rect(SCREEN, DARKBLUE, (10, 45 + CARDINFOSIZE[1] , INFOTEXTSIZE[0], 20))
    title = Title.render('Descricao', True, LIGHTBLUE)
    rect = title.get_rect()
    rect.center = ((INFOTEXTSIZE[0] / 2) + 10, CARDINFOSIZE[1] + 55)
    SCREEN.blit(title, rect)

    # Desenha o texto no textBox
    # Obs: Fazer uma função para ativar qnd o mouse estiver sobre uma carta, dando entrada da carta
    #      e da descrição da mesma. EX: createINFO(card, description)
    text = TextFont.render('Texto que vai na descricao', True, BLACK)
    rect = title.get_rect()
    rect.center = ((INFOTEXTSIZE[0] / 2) - 25, CARDINFOSIZE[1] + 75)
    SCREEN.blit(text, rect)


def DrawPhase(phase, color, Centerx, Centery, Rectx, Recty):
    # --- Desenha os Icones das Fases do Jogo
    
    PhaseFont = pygame.font.Font('freesansbold.ttf', 20)

    # desenho    
    pygame.draw.rect(SCREEN, LIGHTBLUE, (Rectx , Recty, PHASESIZE[0], PHASESIZE[1]))   # desenha ret azul claro
    pygame.draw.rect(SCREEN, DARKBLUE, (Rectx , Recty, PHASESIZE[0], PHASESIZE[1]), 4) # desenha borda azul escuro
    phaseObj = PhaseFont.render(phase, True, color)                    # define o texto e a cor
    phaseRect = phaseObj.get_rect()                                     # pega o espaço ocupado 
    phaseRect.center = (Centerx, Centery)                              # define a posição do ponto central dotexto

    return (phaseObj, phaseRect)
    
def checkForQuit():
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            #Socket.close()
            pygame.quit()
            #sys.exit() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back

def StartGame():

    for c in P1CardList:
        card = Card(c)
        card.visible = True
        DECK.append(card)

    for c in P2CardList:
        card = Card(c)
        P2DECK.append(card)
    
    random.shuffle(DECK)
    random.shuffle(P2DECK)
    
    CurrentPhase = Phases[0]
    GetCard(5, DECK, HAND)
    GetCard(5, P2DECK, P2HAND)
    for card in P2HAND:
        logging.debug(card.name)
        
    drawField()
    DrawInfoBar()
    DrawStatusBar(Player1Info[2], Player2Info[2])


def GetCard(number, deck, hand):
    for card in deck[:number]:
        hand.append(card)
        deck.remove(card)
        time.sleep(0.3)
    DrawHand()
    DrawDeck()


def DrawHand():
    #print HAND
    #print len(CardList)
    # Player 1
    x = INFOSIZE[0] + 25
    y = (FIELDSIZE[1] * 2) + STATUSSIZE[1] + PHASESIZE[1] + 70
    pygame.draw.rect(SCREEN, BLACK, (x -3, y -3, WINDOWWIDTH, 100))
    space = AdjustHand(HAND)
    for card in HAND:
        card.img = pygame.transform.scale(card.imgLoad, (CARDHANDSIZE[0], CARDHANDSIZE[1]))
        card.size = card.img.get_size()
        card.pixPosition = (x, y)
        SCREEN.blit(card.img, card.pixPosition)
        x += CARDHANDSIZE[0] + space

    # Player 2
    x = INFOSIZE[0] + 25
    y = - 40
    pygame.draw.rect(SCREEN, BLACK, (x -3, y -3, WINDOWWIDTH, 130))
    space = AdjustHand(P2HAND)
    for card in P2HAND:
        if card.visible:
            card.img = card.imgLoad
        else:
            card.img = card.imgBack
        card.img = pygame.transform.scale(card.img, (CARDHANDSIZE[0], CARDHANDSIZE[1]))
        card.size = card.img.get_size()
        card.pixPosition = (x, y)
        SCREEN.blit(card.img, card.pixPosition)
        x += CARDHANDSIZE[0] + space
    DrawStatusBar(Player1Info[2], Player2Info[2])

def DrawPhaseSeq():
    # -- Desenha todas as Phases do Jogo
    # Set Variables 
    x = DPPos[0]  #(INFOSIZE[0] + 60)
    y = DPPos[1]  #(STATUSSIZE[1] + FIELDSIZE[1] + 62)
    Centerx = (INFOSIZE[0] + 95)
    Centery = (STATUSSIZE[1] + FIELDSIZE[1] + 63 + (PHASESIZE[1] /2))
    for phase in Phases:
        color = BLACK
        if CheckMouseOver((x, y), (PHASESIZE[0], PHASESIZE[1])):
            color = GREEN
        if phase == 'DP' and ACTIVEPHASE == 'Draw Phase':
            color = RED
        elif phase == 'SP' and ACTIVEPHASE == 'Standby Phase':
            color = RED
        elif phase == 'MP' and ACTIVEPHASE == 'Main Phase':
            color = RED
        elif phase == 'BP' and ACTIVEPHASE == 'Battle Phase':
            color = RED
        elif phase == 'MP2' and ACTIVEPHASE == 'Main Phase 2':
            color = RED
        elif phase == 'EP' and ACTIVEPHASE == 'End Phase':
            color = RED
        textObj, textRect = DrawPhase(phase, color, Centerx, Centery, x, y)
        SCREEN.blit(textObj, textRect)
        x += PHASESIZE[0] + 35                          
        Centerx += PHASESIZE[0] + 35

def AdjustHand(hand):
    # -- Ajusta o espaço entre as cartas na mão,
    # -- conforme a quantidade de cartas
    number = len(hand)
    if number <= 6:
        return 15
    elif number == 7:
        return 1
    elif number == 8:
        return -15
    elif number == 9:
        return -25
    elif number == 10:
        return -30
    else:
        return -35
        
def GetCardInfo():
    for card in HAND:
        if CheckMouseOver(card.pixPosition, card.size):            
            DrawHand()
            pygame.display.update()
            DrawCardInfo(card)
            DrawMouseEffect(card)

    for card in P2HAND:
        if CheckMouseOver(card.pixPosition, card.size):            
            DrawHand()
            pygame.display.update()
            DrawCardInfo(card)
            DrawMouseEffect(card)

    for card in FIELD:
        if CheckMouseOver(card.pixPosition, card.size):            
            DrawHand()
            pygame.display.update()
            DrawCardInfo(card)
            DrawMouseEffect(card)

    for card in P2FIELD:
        if CheckMouseOver(card.pixPosition, card.size):            
            DrawHand()
            pygame.display.update()
            DrawCardInfo(card)
            DrawMouseEffect(card)

            
def DrawCardInfo(card):
    DescFont = pygame.font.Font('freesansbold.ttf', 10)
    if card.visible == False:
        SCREEN.blit(card.imgBack,(10, 20))
        pygame.draw.rect(SCREEN, LIGHTBLUE, (13, 270 , INFOTEXTSIZE[0] - 6, INFOTEXTSIZE[1] - 22))
        pygame.display.update()
    else:    
        SCREEN.blit(card.imgLoad,(10, 20))
        pygame.display.update()

        desc = card.descricao.split()
        line = ''
        lines = []
        
        for word in desc[:]:
            if (len(line + word)) <= 25:
                    line += word + ' '
                    desc.remove(word)
                    if len(desc) == 0:
                            lines.append(line)
            else:
                    lines.append(line)
                    desc.remove(word)
                    line = word + ' '
                    if len(desc) == 0:
                            lines.append(line)


        pygame.draw.rect(SCREEN, LIGHTBLUE, (13, 270 , INFOTEXTSIZE[0] - 6, INFOTEXTSIZE[1] - 22))

        y = CARDINFOSIZE[1] + 75

        if card.category == 'Monster':
            textObj = DescFont.render('ATK ' + str(card.ATK) + ' / DEF ' + str(card.DEF) , True, BLACK)
            textRect = textObj.get_rect()
            textRect.center = ((INFOTEXTSIZE[0] / 2) + 10, y)
            SCREEN.blit(textObj, textRect)
            y += 14

            textObj = DescFont.render('[' + card.type + ']' , True, BLACK)
            textRect = textObj.get_rect()
            textRect.center = ((INFOTEXTSIZE[0] / 2) + 10, y)
            SCREEN.blit(textObj, textRect)
            y += 18
        
        for line in lines:
            textObj = DescFont.render(line, True, BLACK)
            textRect = textObj.get_rect()
            textRect.center = ((INFOTEXTSIZE[0] / 2) + 10, y)
            SCREEN.blit(textObj, textRect)
            y += 12

def DrawMouseEffect(card):
    x = card.pixPosition[0] - 2
    y = card.pixPosition[1] - 2
    pygame.draw.rect(SCREEN, LIGHTBLUE, (x, y, card.size[0] + 2, card.size[1] + 2), 1)

def OnClick():
    global SummonedMonsters

    
    
    for card in HAND:
        if CheckMouseOver(card.pixPosition, card.size):
            if ACTIVEPHASE in ['Main Phase', 'Main Phase 2']:
                if (SummonedMonsters < 1) or (card.category != 'Monster'):
                    if pygame.mouse.get_pressed()[0]:
                        POS = 'Attack'
                    elif pygame.mouse.get_pressed()[2]:
                        POS = 'Defense'
                    else:
                        POS = None
                    if GetTributeMonster(card):
                        spot = GetSpotSummon(card, POS, 'P1')
                        if spot != None:
                            card.Summon(POS, spot, 'P1')
                            if card.category == 'Monster':
                                SummonedMonsters += 1
                            DrawHand()
                            drawField()
                            
                elif card.category == 'Spell':
                    spot = GetSpotSummon(card, None)
                    DrawHand()
                    drawField()

    for card in FIELD:
        if CheckMouseOver(card.pixPosition, card.size):
            if ACTIVEPHASE == 'Battle Phase':
                if card.category == 'Monster' and card.position == 'Attack':
                    card.Attack()
                    drawField()
            elif ACTIVEPHASE == 'Main Phase':
                if card.category == 'Monster':
                    card.ChangePosition()
                    drawField()
    
    for card in P2HAND:
        if CheckMouseOver(card.pixPosition, card.size):
            if card.category == 'Monster':
                if pygame.mouse.get_pressed()[0]:
                    POS = 'Attack'
                elif pygame.mouse.get_pressed()[2]:
                    POS = 'Defense'
                else:
                    POS = None
                spot = GetSpotSummon(card, POS, 'P2')
                card.Summon(POS, spot, 'P2')
                #P2HAND.remove(card)
                #P2FIELD.append(card)

    if CheckMouseOver(GRAVESPOT, CARDSIZE):
        for card in GRAVE:
            print card.name

    if CheckMouseOver(P2GRAVESPOT, CARDSIZE):
        for card in P2GRAVE:
            print card.name

    if CheckMouseOver(DECKSPOT, CARDSIZE):
        if ACTIVEPHASE == 'Draw Phase':
            GetCard(1, DECK, HAND)
            th = ThChangePhase('Standby Phase')
            th.start()
            

    if CheckMouseOver(MPPos, PHASESIZE):
        if ACTIVEPHASE == 'Standby Phase':
            th = ThChangePhase('Draw Phase')
            th.start()
    elif CheckMouseOver(BPPos, PHASESIZE):
        if ACTIVEPHASE == 'Main Phase':
            th = ThChangePhase('Battle Phase')
            th.start()
    elif CheckMouseOver(MP2Pos, PHASESIZE):
        if ACTIVEPHASE == 'Battle Phase':
            th = ThChangePhase('Main Phase 2')
            th.start()
    elif CheckMouseOver(EPPos, PHASESIZE):
        if ACTIVEPHASE  in ['Main Phase', 'Battle Phase', 'Main Phase 2']:
            th = ThChangePhase('End Phase')
            th.start()
            SummonedMonsters = 0
            for card in FIELD:
                if card.category == 'Monster':
                    card.aktDone = 0
                    print 'End Phase - card.atkDone -  ', card.atkDone
                    card.positionChanged = False
            
        


def GetSpotSummon(c, pos, player):
    if player == 'P1':
        MSpotList = [MSPOT1, MSPOT2, MSPOT3, MSPOT4, MSPOT5]
        SSpotList = [SSPOT1, SSPOT2, SSPOT3, SSPOT4, SSPOT5]
        DMSpotList = [DMSPOT1, DMSPOT2, DMSPOT3, DMSPOT4, DMSPOT5]
 
        if c.category == 'Monster':
            for card in FIELD[:]:
                for spot in MSpotList:
                    if (card.pixPosition in [spot, (spot[0] -14, spot[1] + 10)]):
                        MSpotList.remove(spot)
                        DMSpotList.remove((spot[0] -14, spot[1] + 10))
                    
                    
    elif player == 'P2':
        MSpotList = [P2MSPOT1, P2MSPOT2, P2MSPOT3, P2MSPOT4, P2MSPOT5]
        SSpotList = [P2SSPOT1, P2SSPOT2, P2SSPOT3, P2SSPOT4, P2SSPOT5]
        DMSpotList = [P2DMSPOT1, P2DMSPOT2, P2DMSPOT3, P2DMSPOT4, P2DMSPOT5]
        
        if c.category == 'Monster':
            for card in P2FIELD[:]:
                for spot in MSpotList:
                    if (card.pixPosition in [spot, (spot[0] -14, spot[1] + 10)]):
                        MSpotList.remove(spot)
                        DMSpotList.remove((spot[0] -14, spot[1] + 10))
               

            
    if c.category == 'Monster':
        if len(MSpotList) == 0 or len(DMSpotList) == 0:
            return None
        if pos == 'Attack':
            print MSpotList
            return MSpotList[0]
                
        if pos == 'Defense':
            return DMSpotList[0]
        
    elif c.category in ['Spell', 'Trap']:
        for card in FIELD[:]:
            for spot in SSpotList[:]:
                if card.pixPosition == spot:
                    SSpotList.remove(spot)
        if len(SSpotList) == 0:
            return None
        else:
            return SSpotList[0]




def GetTributeMonster(card):
    if card.category != 'Monster':
        return True

    if card.nivel < 5:
        return True
    elif card.nivel in [5,6]:
        n = 1
    elif card.nivel > 6:
        n = 2

    count = 0
    check = 0
    
    for trib in FIELD:
        if trib.category == 'Monster':
            check += 1

    if check == 0:
        return False

    if (check == 1) and (n == 2):
        return False

    
    while count < n:
        if pygame.event.wait().type == MOUSEBUTTONUP:
            for trib in FIELD:
                if trib.category == 'Monster':
                    if CheckMouseOver(trib.pixPosition, trib.size):
                        GRAVE.append(trib)
                        FIELD.remove(trib)
                        trib.pixPosition = GRAVESPOT
                        trib.img = pygame.transform.scale(trib.imgLoad, CARDSIZE)
                        SCREEN.blit(trib.img, trib.pixPosition)
                        count += 1
    return True




def UpdateGame(msg):
    global Player2Info
    global P2choose
    
    msg = msg.split()
    print msg

    if msg[0] == 'Summon':
        for card in P2HAND:
            if card.name == msg[1]:
                pos = msg[2]
                pix = tuple(map(int, msg[3][1:-1].split(',')))
                card.Summon(pos, pix, 'P2')

    # Effect

    elif msg[0] == 'player2':
        Player2Info = GetUserInfo(msg[1], msg[2])

    elif msg[0] == 'janken':
        P2choose = msg[1]

    elif msg[0] == 'FIRST':
        FIRST = msg[1]


    # Attack


    # Update Status

    pygame.display.update()

'''def DrawJanken():
    Font = pygame.font.Font('freesansbold.ttf', 50)

    pygame.draw.rect(SCREEN, ORANGE, (0, 0 , WINDOWWIDTH, WINDOWHEIGHT))
    pygame.draw.rect(SCREEN, DARKORANGE, (0, 0 , WINDOWWIDTH, WINDOWHEIGHT), 5)

    OptionList = {'Pedra': None, 'Papel': None, 'Tesoura': None}

    x = 50
    for option in OptionList:
        btn = pygame.draw.rect(SCREEN, DARKORANGE, (x, 215 , 230, 200), 8)

        if CheckMouseOver((btn[0], btn[1]), (btn[2], btn[3])):
            color = LIGHTORANGE
        else:
            color = RED
            
        textObj = Font.render(option, True, color)
        textRect = textObj.get_rect()
        textRect.center = (btn.center)
        SCREEN.blit(textObj, textRect)

        OptionList[option] = btn.get_rect()
        x += 260
    return OptionList

def DrawGetFirst(choose):
    global Player1Info
    global Player2Info
    
    Font = pygame.font.Font('freesansbold.ttf', 50)
    msFont = pygame.font.Font('freesansbold.ttf', 20)

    pygame.draw.rect(SCREEN, ORANGE, (0, 0 , WINDOWWIDTH, WINDOWHEIGHT))
    pygame.draw.rect(SCREEN, DARKORANGE, (0, 0 , WINDOWWIDTH, WINDOWHEIGHT), 5)

    OptionList = {Player1Info[1]: None, Player2Info[1]: None}

    x = 195
    for option in OptionList:
        btn = pygame.draw.rect(SCREEN, DARKORANGE, (x, y , 230, 200), 8)

        if CheckMouseOver((btn[0], btn[1]), (btn[2], btn[3])):
            color = LIGHTORANGE
        else:
            color = RED
            
        textObj = Font.render(option, True, color)
        textRect = textObj.get_rect()
        textRect.center = (btn.center)
        SCREEN.blit(textObj, textRect)

        OptionList[option] = btn.get_rect()
        x += 260

    textObj = msFont.render(Player2Info[1] +' escolheu ' + choose + ', você ganhou. Escolha quem começa.', True, RED)
    textRect = textObj.get_rect()
    textRect.center = (WINDOWWIDTH /2, WINDOWHEIGHT - 50)
    SCREEN.blit(textObj, textRect)

    return OptionList

    
def WaitForFirst(choose):
    global Player2Info
    
    Font = pygame.font.Font('freesansbold.ttf', 50)

    pygame.draw.rect(SCREEN, ORANGE, (0, 0 , WINDOWWIDTH, WINDOWHEIGHT))
    pygame.draw.rect(SCREEN, DARKORANGE, (0, 0 , WINDOWWIDTH, WINDOWHEIGHT), 5)

    textObj = Font.render(Player2Info[1] + ' escolheu ' + choose + ', você perdeu. Ele escolhe quem começa.', True, RED)
    textRect = textObj.get_rect()
    textRect.center = (SCREEN.center)
    SCREEN.blit(textObj, textRect)

def ClickJanken(OptionList):

    choose = None
    for option in OptionList:
        btn = OptionList[option]
        if CheckMouseOver((btn[0], btn[1]), (btn[2], btn[3])):
            choose = option
    return choose

def CheckJunken(v1, v2):
    if v1 == 'pedra':
        if v2 == 'tesoura':
            winner = v1
        elif v2 == 'papel':
            winner = v2
        elif v2 == 'pedra':
            winner = None
    elif v1 == 'papel':
        if v2 == 'tesoura':
            winner = v2
        elif v2 == 'papel':
            winner = None
        elif v2 == 'pedra':
            winner = v1
    elif v1 == 'tesoura':
        if v2 == 'tesoura':
            winner = None
        elif v2 == 'papel':
            winner = v1
        elif v2 == 'pedra':
            winner = v2
            
    return winner'''
        

class ThChangePhase(Thread):

    def __init__(self, phase):
        Thread.__init__(self)
        self.phase = phase

    def run(self):
        global ACTIVEPHASE
        
        Font = pygame.font.Font('freesansbold.ttf', 50)

        textObj = Font.render(self.phase, True, RED)
        print self.phase
        textRect = textObj.get_rect()
        textRect.center = ((WINDOWWIDTH / 2) + (INFOSIZE[0] / 2), WINDOWHEIGHT - 200)
        SCREEN.blit(textObj, textRect)
        pygame.display.update()
    
        time.sleep(1)

        drawField()

        ACTIVEPHASE = self.phase

        if ACTIVEPHASE == 'Draw Phase':
            pass
        elif ACTIVEPHASE == 'Standby Phase':
            th = ThChangePhase('Main Phase')
            th.start()
        elif ACTIVEPHASE == 'Main Phase':
            pass
        elif ACTIVEPHASE == 'Battle Phase':
            pass
        elif ACTIVEPHASE == 'Main Phase 2':
            pass
        elif ACTIVEPHASE == 'End Phase':
            th = ThChangePhase('Draw Phase')
            th.start()
                

class ThReceive(Thread):

    def __init__(self, socket):
        super(ThReceive, self).__init__()
        self.socket = socket
        self.stop = False

    def run(self):
        while not self.stop:
            msg = self.socket.recv(256)
            if msg != '':
                UpdateGame(msg)

# ----- CLASSE CARD --------------------------------------------------------------------------------------------------------
# ==========================================================================================================================


class Card(object):
    def __init__(self, name):
        self.info = connection.GetCardInfo(name)
        self.name = name
        self.visible = False
        self.imgLoad = pygame.image.load('tmp/' + self.name + '.bmp')
        self.imgBack = pygame.image.load('yugi_lib/images/cards/bmp/BackCard.bmp')
        #self.imgLoad = pygame.transform.scale(self.imgLoad, (CARDINFOSIZE[0], CARDINFOSIZE[1]))
        self.img = None
        self.positionChanged = False
        self.descricao = self.info[3]
        self.type = self.info[5]
        self.category = self.info[9]
        self.position = ''
        self.pixPosition = []
        self.size = []
        self.FaceUp = False
        if self.category == 'Monster':
            self.ATK = self.info[7]
            self.DEF = self.info[8]
            self.nivel = self.info[4]
            self.attribute = self.info[6]
            self.atkDone = 0
        elif self.category == 'Trap':
            self.CanActive = False

        logging.basicConfig(filename='debug.log',level=logging.DEBUG)
        
        
    def Attack(self):
        count = 0
        check = 0
        #global LP
        #global P2LP
        if self.atkDone > 0:
            return None
        
        for card in P2FIELD:
            if card.category == 'Monster':
                check += 1
        if check == 0:
            CalcPoints('P2', -(self.ATK))
            self.atkDone += 1
        else:
            while count < 1:
                if pygame.event.wait().type == MOUSEBUTTONUP:
                    for enemy in P2FIELD:
                        if CheckMouseOver(enemy.pixPosition, enemy.size):
                            if enemy.category == 'Monster':
                                if enemy.position == 'Attack':
                                    enemy.RecvAttack(self)
                                    if self.ATK > enemy.ATK:
                                        GoToGrave(enemy, P2FIELD, P2GRAVE)
                                        CalcPoints('P2', -(self.ATK - enemy.ATK))
                                        self.atkDone += 1
                                        count += 1
                                        self.positionChanged = True
                                    elif self.ATK < enemy.ATK:
                                        GoToGrave(self, FIELD, GRAVE)
                                        CalcPoints('P1', -(enemy.ATK - self.ATK))
                                        self.atkDone += 1
                                        count += 1
                                        self.positionChanged = True
                                    else:
                                        GoToGrave(self, FIELD, GRAVE)
                                        GoToGrave(enemy, P2FIELD, P2GRAVE)
                                        self.atkDone += 1
                                        count += 1 
                                elif enemy.position == 'Defense':
                                    if self.ATK > enemy.DEF:
                                        GoToGrave(enemy, P2FIELD, P2GRAVE)
                                        self.atkDone += 1
                                        count += 1
                                        self.positionChanged = True
                                
        
    def Summon(self, position, pixPosition, player):
        Font = pygame.font.Font('freesansbold.ttf', 10)
        self.position = position
        self.pixPosition = pixPosition
        self.positionChanged = True
        self.img = pygame.transform.scale(self.imgLoad, CARDSIZE)            
            
        if player == 'P2':
            P2HAND.remove(self)
            P2FIELD.append(self)
            self.img = pygame.transform.rotate(self.img, -180)
            if self.category == 'Monster':
                if position == 'Defense':
                    self.img = pygame.transform.scale(self.imgBack, CARDSIZE)
                    self.size = DefCARDSIZE
                    self.img = pygame.transform.rotate(self.img, 90)
                    self.visible = False                  
                else:
                    self.size = CARDSIZE
                    self.visible = True
                    self.FaceUp = True
                    textObj = Font.render(str(self.ATK) + ' | ' + str(self.DEF), True, WHITE)
                    textRect = textObj.get_rect()
                    textRect.center = (self.pixPosition[0] + (self.size[0] / 2), self.pixPosition[1] - 6)
                    SCREEN.blit(textObj, textRect)
        else:
            HAND.remove(self)
            FIELD.append(self)
            self.size = CARDSIZE
            if self.category == 'Monster':
                if position == 'Defense':
                    self.img = pygame.transform.scale(self.imgBack, CARDSIZE)
                    self.img = pygame.transform.rotate(self.img, -90)
                    self.size = DefCARDSIZE
                else:
                    #self.size = CARDSIZE
                    textObj = Font.render(str(self.ATK) + ' | ' + str(self.DEF), True, WHITE)
                    textRect = textObj.get_rect()
                    textRect.center = (self.pixPosition[0] + (self.size[0] / 2), self.pixPosition[1] + (self.size[1] + 8))
                    SCREEN.blit(textObj, textRect)
                    
            elif self.category == 'Spell':
                thread.start_new_thread(self.ActiveEffect,())

            elif self.category == 'Trap':
                self.img = pygame.transform.scale(self.imgBack, CARDSIZE)
                
                
        SCREEN.blit(self.img, pixPosition)

    def RecvAttack(self, enemy):
        if ShowMessage('Oponente está atacando, deseja ativar alguma carta?', 'Pergunta'):
            drawField()
            pygame.display.update()
            count = 0
            while count < 1:
                if pygame.event.wait().type == MOUSEBUTTONDOWN:
                    for card in FIELD:
                        if CheckMouseOver(card.pixPosition, card.size):
                            if card.category == 'Trap':
                                card.ActiveEffect()
                                count +=1
                                print count
            print 'saiu da porra do loop'
        else:
            return None
        
    def ChangePosition(self):
        if self.positionChanged == True:
            return None

        if self.position == 'Attack':
            self.position = 'Defense'
            self.img = pygame.transform.rotate(self.img, 90)
            self.positionChanged = True
            
            if self.pixPosition == MSPOT1:
                self.pixPosition = DMSPOT1
            elif self.pixPosition == MSPOT2:
                self.pixPosition = DMSPOT2
            elif self.pixPosition == MSPOT3:
                self.pixPosition = DMSPOT3
            elif self.pixPosition == MSPOT4:
                self.pixPosition = DMSPOT4
            elif self.pixPosition == MSPOT5:
                self.pixPosition = DMSPOT5
                
            self.size = DefCARDSIZE
            SCREEN.blit(self.img, self.pixPosition)
        else:
            self.position = 'Attack'
            self.img = pygame.transform.scale(self.imgLoad, CARDSIZE)
            self.FaceUp = True
            self.positionChanged = True
            
            if self.pixPosition == DMSPOT1:
                self.pixPosition = MSPOT1
            elif self.pixPosition == DMSPOT2:
                self.pixPosition = MSPOT2
            elif self.pixPosition == DMSPOT3:
                self.pixPosition = MSPOT3
            elif self.pixPosition == DMSPOT4:
                self.pixPosition = MSPOT4
            elif self.pixPosition == DMSPOT5:
                self.pixPosition = MSPOT5
                
            self.size = CARDSIZE
            SCREEN.blit(self.img, self.pixPosition)

    def ActiveEffect(self):
        if self.name == 'DarkHole':
            if len(FIELD) != 0:
                for card in FIELD[:]:
                    if card.category == 'Monster':
                        GoToGrave(card, FIELD, GRAVE)
                        pygame.draw.rect(SCREEN, BLACK,(card.pixPosition[0] -3, card.pixPosition[1] -3, CARDSIZE[0] +3, CARDSIZE[1] +16))
                        time.sleep(0.5)

            if len(P2FIELD) != 0:
                for card in P2FIELD[:]:
                    if card.category == 'Monster':
                        GoToGrave(card, P2FIELD, P2GRAVE)
                        pygame.draw.rect(SCREEN, BLACK,(card.pixPosition[0] -3, card.pixPosition[1] -14, CARDSIZE[0] +3, CARDSIZE[1] +14))
                        time.sleep(0.5)

            pygame.draw.rect(SCREEN, BLACK,(self.pixPosition[0] -3, self.pixPosition[1] -3, CARDSIZE[0] +3, CARDSIZE[1] +3))
            GoToGrave(self, FIELD, GRAVE)

            
        elif self.name == 'Reinforcements':
            ShowMessage('Selecione o monstro!', 'Exclamacao')
            self.img = pygame.transform.scale(self.imgLoad, CARDSIZE)
            drawField()
            #pygame.display.update()
            count = 0
            while count < 1:
                if pygame.event.wait().type == MOUSEBUTTONDOWN:
                    for card in FIELD:
                        if CheckMouseOver(card.pixPosition, card.size):
                            if card.category == 'Monster':
                                card.ATK += 500
                                EPEffects.append(('Reinforcements', card))
                                print 'colocando o ATK em ', card.name
                                GoToGrave(self, FIELD, GRAVE)
                                count += 1
                                print count
                    #for card in P2FIELD:
                    #    if CheckMouseOver(card.pixPosition, card.size):
                    #        if card.category == 'Monster':
                    #            card.ATK += 500
                    #            count += 1

                    
        elif self.name == 'MysticalSpaceTyphoon':
            ShowMessage('Selecione a carta!', 'Exclamacao')
            self.img = pygame.transform.scale(self.imgLoad, CARDSIZE)
            drawField()
            #pygame.display.update()
            count = 0
            while count < 1:
                if pygame.event.wait().type == MOUSEBUTTONDOWN:
                    for card in P2FIELD:
                        if CheckMouseOver(card.pixPosition, card.size):
                            if card.category in ['Trap', 'Spell']:
                                GoToGrave(card, P2FIELD, P2GRAVE)
                                time.sleep(0.5)
                                GoToGrave(self, FIELD, GRAVE)
                                count += 1
                    for card in FIELD:
                        if CheckMouseOver(card.pixPosition, card.size):
                            if card.category in ['Trap', 'Spell']:
                                GoToGrave(card, FIELD, GRAVE)
                                time.sleep(0.5)
                                GoToGrave(self, FIELD, GRAVE)
                                count += 1

        elif self.name == 'PotofGreed':
            GetCard(2, DECK, HAND)
            GoToGrave(self, FIELD, GRAVE)

        elif self.name == 'Fissure':            
            for card in P2FIELD:
                if card.category == 'Monster' and card.FaceUp == True:
                    menor = card

            for card in P2FIELD:
                if card.category == 'Monster' and card.FaceUp == True:
                    if card.ATK < menor.ATK:
                        menor = card

            GoToGrave(menor, P2FIELD, P2GRAVE)
            time.sleep(0.5)
            GoToGrave(self, FIELD, GRAVE)

        elif self.name == 'BlackPendant':
            ShowMessage('Selecione o monstro!', 'Exclamacao')
            self.img = pygame.transform.scale(self.imgLoad, CARDSIZE)
            #drawField()
            #pygame.display.update()
            count = 0
            while count < 1:
                if pygame.event.wait().type == MOUSEBUTTONDOWN:
                    for card in FIELD:
                        if CheckMouseOver(card.pixPosition, card.size):
                            if card.category == 'Monster':
                                card.ATK += 500
                                print 'colocando o ATK em ', card.name
                                count += 1
                                print count
                                
        elif self.name == 'DianKetotheCureMaster':
            CalcPoints('P1', 1000)
            time.sleep(1)
            GoToGrave(self, FIELD, GRAVE)
            drawField()

        elif self.name == 'HammerShot':
            for card in P2FIELD:
                if card.category == 'Monster' and card.position == 'Attack':
                    P2maior = card

            for card in P2FIELD[:]:
                if card.category == 'Monster' and card.position == 'Attack':
                    if card.ATK > P2maior.ATK:
                        P2maior = card

            for card in FIELD:
                if card.category == 'Monster' and card.position == 'Attack':
                    P1maior = card

            for card in FIELD[:]:
                if card.category == 'Monster' and card.position == 'Attack':
                    if card.ATK > P1maior.ATK:
                        P1maior = card
            if P2maior.ATK > P1maior.ATK:
                maior = P2maior
            else:
                maior = P1maior
            
            GoToGrave(maior, P2FIELD, P2GRAVE)
            GoToGrave(self, FIELD, GRAVE)

        elif self.name == 'HeavyStorm':
            if len(P2FIELD) != 0:  
                for card in P2FIELD[:]:
                    if card.category in ['Spell','Trap']:
                        GoToGrave(card, P2FIELD, P2GRAVE)
                        pygame.draw.rect(SCREEN, BLACK,(card.pixPosition[0] -3, card.pixPosition[1] -3, CARDSIZE[0] +3, CARDSIZE[1] +16))
                        time.sleep(0.5)
            if len(FIELD) != 0:
                for card in FIELD[:]:
                    if card.category == 'Monster':
                        GoToGrave(card, P2FIELD, P2GRAVE)
                        pygame.draw.rect(SCREEN, BLACK,(card.pixPosition[0] -3, card.pixPosition[1] -14, CARDSIZE[0] +3, CARDSIZE[1] +14))
                        time.sleep(0.5)

            pygame.draw.rect(SCREEN, BLACK,(self.pixPosition[0] -3, self.pixPosition[1] -3, CARDSIZE[0] +3, CARDSIZE[1] +3))
            GoToGrave(self, FIELD, GRAVE)
                        
        elif self.name == 'MalevolentNuzzler':
            ShowMessage('Selecione o monstro!', 'Exclamacao')
            self.img = pygame.transform.scale(self.imgLoad, CARDSIZE)
            #drawField()
            #pygame.display.update()
            count = 0
            while count < 1:
                if pygame.event.wait().type == MOUSEBUTTONDOWN:
                    for card in FIELD:
                        if CheckMouseOver(card.pixPosition, card.size):
                            if card.category == 'Monster':
                                card.ATK += 700
                                print 'colocando o ATK em ', card.name
                                count += 1
                                print count
                                
        elif self.name == 'Reload':
            count = 0
            for card in HAND[:]:
                DECK.append(card)
                HAND.remove(card)
                count += 1
                DrawHand()
                time.sleep(0.5)
                
            random.shuffle(DECK)
            GetCard(count, DECK, HAND)
            print count

        elif self.name == 'SmashingGround':
            for card in P2FIELD:
                if card.category == 'Monster' and card.FaceUp == True:
                    maior = card

            for card in P2FIELD[:]:
                if card.category == 'Monster' and card.FaceUp == True:
                    if card.DEF > maior.DEF:
                        maior = card

            GoToGrave(maior, P2FIELD, P2GRAVE)
            time.sleep(0.5)
            GoToGrave(self, FIELD, GRAVE)

        elif self.name == 'TributetotheDoomed':
            ShowMessage('Descarte uma carta!', 'Exclamacao')
            self.img = pygame.transform.scale(self.imgLoad, CARDSIZE)
            #drawField()
            #pygame.display.update()
            count = 0
            while count < 1:
                if pygame.event.wait().type == MOUSEBUTTONDOWN:
                    for card in HAND:
                        if CheckMouseOver(card.pixPosition, card.size):
                            HAND.remove(card)
                            GRAVE.append(card)
                            count += 1

            ShowMessage('Selecione o monstro que deseja destruir!', 'Exclamacao')
            self.img = pygame.transform.scale(self.imgLoad, CARDSIZE)
            drawField()
            pygame.display.update()
            count = 0
            while count < 1:
                if pygame.event.wait().type == MOUSEBUTTONDOWN:
                    for card in FIELD:
                        if CheckMouseOver(card.pixPosition, card.size):
                            if card.category == 'Monster':
                                GoToGrave(card, FIELD, GRAVE)
                                count += 1
                    for card in P2FIELD:
                        if CheckMouseOver(card.pixPosition, card.size):
                            if card.category == 'Monster':
                                GoToGrave(card, P2FIELD, P2GRAVE)
                                count += 1
                           


    def Draw(self, pixPosition, surface):
        x =1

    def __del__(self):
       pass

# ==========================================================================================================================
# ==========================================================================================================================


if __name__ == '__main__':
    if CheckLogin(USER, PASSWD) == 1:
        main()
    else:
        print 'Usuario ou senha invalidos'
        pygame.quit()
        sys.exit()       
        
