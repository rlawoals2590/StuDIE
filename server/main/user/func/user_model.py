from datetime import datetime
import secrets
import bcrypt


class Model:
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.name = kwargs['name']
        self.birth = kwargs['birth']
        self.belong = kwargs['belong']
        self.gender = kwargs['gender']
        self.local = kwargs['local']
        self.vision = kwargs['vision']
        self.rival_id = None
        self.passwd = kwargs['passwd']
        self.join_date = datetime.now()
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
            'id': self.id,
            'name': self.name,
            'birth': self.birth,
            'belong': self.belong,
            'gender': self.gender,
            'local': self.local,
            'vision': self.vision,
            'rival_id': self.rival_id,
            'passwd': passwd,
            'join_date': self.join_date,
            'token': self.token
        }

        return self.user_info




