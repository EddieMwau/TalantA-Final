from kivy.uix.screenmanager import Screen
import pymysql


class Account(Screen):
    def show_upload(self):
        self.manager.current = 'upload'

    def exit_from_acc(self):
        self.manager.current = 'base'

    def show_edit_account(self):
        db = pymysql.connect('localhost','root','','talanta')
        cursor = db.cursor()

        f = open('current.txt', 'r')
        username = f.read()
        f.close()

        ac_name = self.ids.acc_name
        ac_name.text = username

        user_des = ''
        sql = "SELECT * FROM USERS WHERE USER_NAME = '%s'" % username
        cursor.execute(sql)
        results = cursor.fetchall()
        for result in results:
            user_des = result[6]

        if user_des == 'artist':
            self.manager.current = 'manage_artist'
        elif user_des == 'gallery':
            self.manager.current = 'manage_gallery'
        else:
            self.manager.current = 'manage'
