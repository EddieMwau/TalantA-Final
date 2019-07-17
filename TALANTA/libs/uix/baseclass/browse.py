from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
import pymysql


class BrowseScreen(Screen):
    db = pymysql.connect('localhost', 'root', '', 'talanta')
    cursor = db.cursor()

    sql = """SELECT * 
                     FROM ART 
                     LEFT JOIN USERS 
                     ON USERS.USER_ID = ART.USER_ID
                     ORDER BY ART_ID ASC"""

    usernames = []
    artwork = []
    description = []
    title = []

    cursor.execute(sql)

    results = cursor.fetchall()
    for result in results:
        usernames.append(result[9])
        artwork.append(result[5])
        description.append(result[3])
        title.append(result[2])





