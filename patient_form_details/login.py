from flask import request, session
import hashlib

#from general_details_positive import GeneralDetailsPositive

class Login:
    def __init__(self, dbconnection):
        self.con = dbconnection

        self.username = None
        self.password = None




    def username_password_input(self):

        self.username = request.form.get('emailid')
        self.password = request.form.get('passid')


    #     self.session_for_medical_details()
    #
    # def session_for_medical_details(self):
    #     session['listOfVariable'] = {}
    #     session['listOfVariable'].update(
    #         {'temp': self.temp, 'oxymeter': self.oxymeter, 'spiro_fec': self.spiro_fec, 'spiro_fvc': self.spiro_fvc})
    #
    #     session.modified = True
    #     list_var = {}
    #     list_var.update(session['listOfVariable'])
    #     self.inserting_into_database_medical_details(list_var)
    #


    def inserting_into_database_login_details(self, list_var):
        cur = self.con.cursor()
        # hashlib.sha256(str2hash.encode()).hexdigest()
        cur.execute(
                "INSERT INTO login (username,password)VALUES (?,?)",
                (self.username,hashlib.sha256(self.password.encode()).hexdigest()
                 ))
        self.con.commit()
        print("record added ")