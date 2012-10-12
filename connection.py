# -*- coding: utf-8 -*-

#import pymysql
import MySQLdb
import sys
import os

HOST = 'localhost'
USER = 'root'
PASS = 'root'
#PASS = '436991rcp'
DB = 'yugi'

def main():
    user = CheckLogin()

    if user == 0:
        print 'Usuário ou senha inválidos'
        sys.exit()
    else:
        deck = GetUserCards(user)
        for card in deck:
            print card
        
def CheckLogin(username, password):
    con = MySQLdb.connect(host = HOST, user = USER, passwd = PASS, db= DB)
    cur = con.cursor()
           
    return cur.execute('select id from user where passwd = PASSWORD("' + password + '") and username = "' + username + '"')

def GetUserCards(userID):
    Deck = []
    con = MySQLdb.connect(host = HOST, user = USER, passwd = PASS, db= DB)
    cur = con.cursor()
    sql = 'select cards.nome, user_cards.qtd from cards inner join user_cards on ' \
          'user_cards.card = cards.id where user_cards.user = '
    cur.execute(sql + str(userID))

    for card in cur.fetchall():
	for numb in range(0, card[1]):
		Deck.append(card[0])

    return Deck

def GetUserInfo(user, passwd):
    con = MySQLdb.connect(host = HOST, user = USER, passwd = PASS, db= DB)
    cur = con.cursor()
    sql = 'select * from user where username = "' + user + '" and passwd = PASSWORD("' + passwd + '")'
    cur.execute(sql)

    for data in cur.fetchall():
        return data

def GetCardInfo(card):
    con = MySQLdb.connect(host = HOST, user = USER, passwd = PASS, db= DB)
    cur = con.cursor()
    sql = 'select * from cards where nome = "' + card + '"'
    cur.execute(sql)

    for CardInfo in cur.fetchall():
        return CardInfo

def GerarImagens(userID):
    
    con = MySQLdb.connect(host = HOST, user = USER, passwd = PASS, db= DB)
    cur = con.cursor()
    sql = 'select cards.nome, cards.image from cards inner join user_cards on ' \
        'user_cards.card = cards.id where user_cards.user = '
    cur.execute(sql + str(userID))


    d = os.path.dirname('tmp/')
    
    if not os.path.exists(d):
        print d
        os.makedirs(d)
        
    for CardInfo in cur.fetchall():
        fout = open('tmp/' + CardInfo[0] + '.bmp','wb')
        fout.write(CardInfo[1])
        fout.close()


if __name__ == '__main__':
    main()
