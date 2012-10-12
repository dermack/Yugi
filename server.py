#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket, select, logging, pygame

from threadin import thread

# List of socket objects that are currently open
open_sockets = []
dic = {}

pygame.init()
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='log/connection.log',
                    level=logging.DEBUG)

# AF_INET means IPv4.
# SOCK_STREAM means a TCP connection.
# SOCK_DGRAM would mean an UDP "connection".
listening_socket = socket.socket( socket.AF_INET, socket.SOCK_STREAM )

# The parameter is (host, port).
# The host, when empty or when 0.0.0.0, means to accept connections for
# all IP addresses of current machine. Otherwise, the socket will bind
# itself only to one IP.
# The port must greater than 1023 if you plan running this script as a
# normal user. Ports below 1024 require root privileges.
listening_socket.bind( ("localhost", 1234) )

# The parameter defines how many new connections can wait in queue.
# Note that this is NOT the number of open connections (which has no limit).
# Read listen(2) man page for more information.
listening_socket.listen(20)


try:
    server = ThServer()
    server.start()                   
                    

except KeyboardInterrupt:   #   Trata o CTRL+C
    #sock.send("{FONTE}")
    print "Saindo..."
    exit(0)

except socket.error :
    logging.error(' erro desconhecido')


    

class ThServer(Thread):

    def __init__(self):
        super(ThServer, self).__init__()
        #self.socket = socket
        self.stop = False

    def run(self):
        while not self.stop:
            # Waits for I/O being available for reading from any socket object.
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        print 'Saindo...'
                        try:
                            listening_socket.close()
                            exit(0)
                            pygame.quit()
                            self.stop = True
                        except:
                            logging.error(' Erro ao fechar servidor')
                        
            rlist, wlist, xlist = select.select( [listening_socket] + open_sockets, [], [] )
            for i in rlist:
                if i is listening_socket:
                    new_socket, addr = listening_socket.accept()
                    print addr
                    open_sockets.append(new_socket)
                else:
                    try:
                        data = i.recv(256)
                        
                    except:
                        open_sockets.remove(i)
                        print "Connection closed"
                        for n in range(1, len(dic)+ 1):
                            if i in dic[n]:
                                if i == dic[n][0]:
                                    dic[n][1].send('LOST CONNECTION')
                                    dic[n].pop(0)
                                else:
                                    dic[n][0].send('LOST CONNECTION')
                                    dic[n].pop(1)

                                if dic[n] == []:
                                    dic.pop(n)
                 
                        
                    if data.startswith('sala'):
                            x, sala = msg.split()
                            sala = int(sala)
                            if dic.has_key(sala):
                                dic[sala].append(i)
                            else:
                                dic[sala] = [i]
                    else:
                        if len(open_sockets) > 1:
                            for n in range(1, len(dic)+ 1):
                                if i in dic[n]:
                                    if i == dic[n][0]:
                                        snd = dic[n][1]
                                    else:
                                        snd = dic[n][0]
                            snd.send(data) 
