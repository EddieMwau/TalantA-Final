from kivy.uix.screenmanager import Screen
import pymysql


class UploadGallery(Screen):
    def cancel_clicked(self):
        self.manager.current = 'account'

    def upload_clicked(self):
        info = self.ids.info
        ename = self.ids.name_field
        desig = self.ids.des_field

        f =open('current.txt', 'r')
        username = f.read()
        f.close()

        db = pymysql.connect('localhost', 'root','','talanta')
        cursor = db.cursor()
        cursor2 = db.cursor()

        sql2 = "SELECT * FROM USERS WHERE USER_NAME = '%s'" % username
        cursor2.execute(sql2)

        user_id = ''
        results = cursor2.fetchall()
        for result in results:
            user_id = result[0]

        enames = ename.text
        desigs = desig.text

        sql ="INSERT INTO GALLERY(USER_ID, EVENT_NAME, EVENT_DESCRIPTION)" \
             "VALUES ('%s', '%s','%s')" % (user_id, enames, desigs)

        try:
            if ename.text == '' or desig.text == '':
                info.text = '[color=#FF0000]Please fill out all fields[/color]'
            else:
                cursor.execute(sql)
                db.commit()
                info.text = '[color=#00FF00]success[/color]'
                ename.text = ''
                desig.text = ''
        except:
            db.rollback()
            print('error')

        db.close()

    def select_clicked(self):
        pass
