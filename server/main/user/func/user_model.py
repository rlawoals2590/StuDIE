from datetime import datetime
import bcrypt


class Model:
    def __init__(self, **kwargs):
        self.stid = kwargs['stid']
        self.passwd = kwargs['passwd']
        self.name = kwargs['name']
        self.gender = kwargs['gender']
        self.school = kwargs['school']
        self.local = kwargs['local']
        self.join_date = datetime.now()
        self.rival = kwargs['rival']
        self.token = None

        self.user_info = []

    def pw_encryption(self):
        passwd = self.passwd
        hashed_passwd = bcrypt.hashpw(passwd.encode('utf-8'), bcrypt.gensalt())
        passwd_hash = hashed_passwd.decode('utf-8')
        return passwd_hash

    def user_model(self):
        passwd = self.pw_encryption()
        self.user_info = {
            'stid': self.stid,
            'passwd': passwd,
            'name': self.name,
            'gender': self.gender,
            'school': self.school,
            'local': self.local,
            'join_date': self.join_date,
            'rival': self.rival,
            'token': self.token
        }

        return self.user_info




