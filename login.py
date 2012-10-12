#!/usr/bin/env python
# -*- coding: cp1252 -*-

import pygtk
pygtk.require('2.0')
import gtk
import connection

USER = ''
PASS = ''

class EntryExample:
    def enter_callback(self, widget, user, passwd):
        if connection.CheckLogin(USER, PASS) == 0:
            
            mdErro.run()
            mdErro.destroy()
        elif connection.CheckLogin(USER, PASS) == 1:
            mdInfo = gtk.MessageDialog(self, 
            gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_INFO, 
            gtk.BUTTONS_CLOSE, "Bem Vindo")
            mdInfo.run()
            mdInfo.destroy()
            

    def entry_toggle_editable(self, checkbutton, entry):
        entry.set_editable(checkbutton.get_active())

    def entry_toggle_visibility(self, checkbutton, entry):
        entry.set_visibility(checkbutton.get_active())

    def __init__(self):
        #create a new window
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_size_request(200, 100)
        window.set_title('Login')
        window.connect('delete_event', lambda w,e: gtk.main_quit())

        vbox = gtk.VBox(False, 0)
        window.add(vbox)
        vbox.show()

        userLabel = gtk.Label('Login:')
        vbox.pack_start(userLabel, True, True, 0)
        userLabel.show()

        userLogin = gtk.Entry()
        userLogin.set_max_length(50)
        userLogin.connect('activate', self.enter_callback, userLogin)
        #userLogin.set_text('Hello')
        #userLogin.insert_text(' world', len(user.get_text()))
        vbox.pack_start(userLogin, True, True, 0)
        userLogin.show()

        passLabel = gtk.Label('Senha:')
        vbox.pack_start(passLabel, True, True, 0)
        passLabel.show()

        passLogin = gtk.Entry()
        passLogin.set_max_length(50)
        passLogin.connect('activate', self.enter_callback, userLogin, passLogin)
        #userLogin.set_text('Hello')
        #userLogin.insert_text(' world', len(user.get_text()))
        vbox.pack_start(passLogin, True, True, 0)
        passLogin.show()

        hbox = gtk.HBox(False, 0)
        vbox.add(hbox)
        hbox.show()

        button = gtk.Button(stock=gtk.STOCK_CLOSE)
        button.connect('clicked', lambda w: gtk.main_quit())
        vbox.pack_start(button, True, True, 0)
        button.set_flags(gtk.CAN_DEFAULT)
        button.grab_default()
        button.show()

        mdErro = gtk.MessageDialog('teste', window, gtk.MESSAGE_ERROR, gtk.BUTTONS_CLOSE, "Login ou Senha inválidos!")
        
        window.show()

def main():
    gtk.main()
    return 0

if __name__ == '__main__':
    EntryExample()
    main()
