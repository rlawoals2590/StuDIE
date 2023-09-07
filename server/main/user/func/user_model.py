from datetime import datetime
import secrets
import bcrypt


class Model:
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.belong = kwargs['belong']
        self.local = kwargs['local']
        self.passwd = kwargs['passwd']
        self.token = None
        self.point = 0

        self.user_info = []

    def pw_encryption(self):
        passwd = self.passwd
        hashed_passwd = bcrypt.hashpw(passwd.encode('utf-8'), bcrypt.gensalt())
        passwd_hash = hashed_passwd.decode('utf-8')
        return passwd_hash

    def user_model(self):
        passwd = self.pw_encryption()
        self.user_info = {
            'id': self.id,
            'belong': self.belong,
            'local': self.local,
            'passwd': passwd,
            'token': self.token,
            'point': self.point
        }

        return self.user_info




