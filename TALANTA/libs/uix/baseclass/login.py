# -*- coding: utf-8 -*-
#
# This file created with KivyCreatorProject
# <https://github.com/HeaTTheatR/KivyCreatorProgect
#
# Copyright © 2017 Easy
#
# For suggestions and questions:
# <kivydevelopment@gmail.com>
# 
# LICENSE: MIT

from kivy.uix.screenmanager import Screen
import time
import pymysql


class Login(Screen):
    def reload_login(self):
        self.manager.current = 'login'

    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        info = self.ids.info

        uname = user.text
        passw = pwd.text

        db = pymysql.connect('localhost', 'root', '', 'talanta')
        cursor = db.cursor()

        sql = "SELECT * FROM USERS WHERE USER_NAME = '%s' AND PASSWORD = '%s' " % (uname, passw)

        cursor.execute(sql)
        users = cursor.fetchall()

        if uname == '' or passw == '':
            info.text = '[color=#FF0000]username and/or password required[/color]'
        else:
            if users:
                current_usr = open('current.txt', 'w')
                current_usr.write(uname)
                current_usr.close()
                self.ids.info.text = ''
                self.ids.username_field.text = ''
                self.ids.pwd_field.text = ''

                self.manager.current = 'base'

               # self.parent.parent.current = 'scr_welcome'
            else:
                info.text = '[color=#FF0000]Invalid username or password[/color]'
