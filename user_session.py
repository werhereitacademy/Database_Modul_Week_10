# user_session.py

class UserSession:
    _user_info = {}

    @classmethod
    def set_user(cls, username, role):
        cls._user_info = {"username": username, "role": role}

    @classmethod
    def get_user(cls):
        return cls._user_info

    @classmethod
    def get_role(cls):
        return cls._user_info.get("role", None)
