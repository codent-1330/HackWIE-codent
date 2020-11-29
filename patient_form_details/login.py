from flask import request, session
import hashlib


class Login:
    def __init__(self, dbconnection):

        self.con = dbconnection

        self.username = None
        self.password = None

    def username_password_input(self):

        self.username = request.form.get('emailid')
        self.password = request.form.get('passid')
        self.password_encrypted = hashlib.sha256(self.password.encode()).hexdigest()
        # self.session_for_login_details()

    # def session_for_login_details(self):
    #     session['listOfVariable'] = {}
    #     session['listOfVariable'].update(
    #         {'username': self.username, 'password': self.password_encrypted})
    #
    #     session.modified = True
    #     list_var = {}
    #     list_var.update(session['listOfVariable'])
        self.inserting_into_database_login_details()

    def inserting_into_database_login_details(self, list_var):
        cur = self.con.cursor()
        # hashlib.sha256(str2hash.encode()).hexdigest()
        cur.execute(
                "INSERT INTO login(username, password)VALUES (?,?)", (self.username,self.password_encrypted ))
        self.con.commit()
        print("record added ")
