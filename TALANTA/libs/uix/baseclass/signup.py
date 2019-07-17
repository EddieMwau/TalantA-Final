from kivy.uix.screenmanager import Screen
import re
import pymysql


class Signup(Screen):
    def register_user(self):
        firstname = self.ids.fname_field
        fname = firstname.text

        lastname = self.ids.lname_field
        lname = lastname.text

        username = self.ids.username_field
        uname = username.text

        emailadd = self.ids.email_field
        email = emailadd.text

        password = self.ids.pwd_field
        pwd = password.text

        confirm_pwd = self.ids.confirm_pwd_field
        c_pwd = confirm_pwd.text

        designation = self.ids.designation_field
        des = designation.text

        info = self.ids.info

        addressToVerify = email
        match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', addressToVerify)

        db = pymysql.connect('localhost', 'root', '', 'talanta')
        cursor = db.cursor()
        cursor1 = db.cursor()

        sql = "INSERT INTO USERS(FIRST_NAME,LAST_NAME,USER_NAME,EMAIL,PASSWORD,DESIGNATION)" \
              " VALUES ('%s','%s','%s','%s','%s','%s')" % (fname, lname, uname, email, pwd, des)

        sql2 = "SELECT * FROM USERS"
        cursor1.execute(sql2)
        results = cursor1.fetchall()

        usernames = []
        emails = []
        for result in results:
            usernames.append(result[3])
            emails.append(result[4])

        try:
            if fname == '' or lname == '' or uname == '' or email == '' or pwd == '' or des not in ['artist', 'gallery',
                                                                                                    'enthusiast']:
                info.text = '[color=#FF0000]please fill out all fields![/color]'
            elif match == None:
                info.text = '[color=#FF0000]Email address not valid. Try again!!![/color]'
            elif len(pwd) < 8:
                info.text = '[color=#FF0000]Password must be atleast 8 characters long.[/color]'
            elif uname in usernames:
                info.text = '[color=#FF0000]Username already exists. Try another![/color]'
            elif email in emails:
                info.text = '[color=#FF0000]Email address already exists![/color]'
            elif pwd != c_pwd:
                info.text = '[color=#FF0000]password mismatch![/color]'
            else:
                cursor.execute(sql)
                db.commit()
                # TODO: add clear widgets
                self.ids.pwd_field.text = ''
                self.ids.confirm_pwd_field.text = ''
                self.ids.designation_field.text = 'Sign up as?'
                self.ids.email_field.text = ''
                self.ids.fname_field.text = ''
                self.ids.lname_field.text = ''
                self.ids.username_field.text = ''

                self.manager.current = 'login'
                # self.parent.parent.current = 'scr_login'
        except:
            db.rollback()
            # for debugging purposes
            print('error')

        db.close()
