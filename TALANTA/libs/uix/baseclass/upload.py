from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
import pymysql


class Upload(Screen):
    labelText = StringProperty()

    def cancel_clicked(self):
        self.manager.current = 'account'

    def upload_clicked(self):
        self.manager.current = 'files'

    def select_clicked(self):

        f = open('current.txt', 'r')
        username = f.read()
        f.close()

        db = pymysql.connect('localhost','root','','talanta')
        cursor = db.cursor()
        cursor2 = db.cursor()

        sql = "SELECT * FROM USERS WHERE USER_NAME = '%s'" %username

        user_id = ''

        cursor.execute(sql)
        results = cursor.fetchall()
        for result in results:
            user_id = result[0]

        info = self.ids.info
        art_f = self.ids.art_field
        name_f = self.ids.name_field
        desc = self.ids.des_field
        type_f = self.ids.type_field

        art_img = art_f.text
        art_name = name_f.text
        art_des = desc.text
        art_type = type_f.text

        sql2 = "INSERT INTO ART(USER_ID,ART_NAME,ART_DESCRIPTION,ART_TYPE,ART_IMAGE)" \
               " VALUES ('%s','%s','%s','%s','%s')" % (user_id, art_name, art_des, art_type, art_img)

        try:
            if art_img == '' or art_name == '' or art_des == '' or art_type not in ['paintings','sculptures','digital photography','3d models']:
                info.text = '[color=#FF0000]Please fill out all fields[/color]'
            else:
                cursor2.execute(sql2)
                db.commit()
                info.text = '[color=#00FF00]success[/color]'
        except:
            db.rollback()
            # for debugging
            print('error')
        db.close()

