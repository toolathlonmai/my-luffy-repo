class User:
    def __init__(self, user_id, username, email=None):
        self.user_id = user_id
        self.username = username
        self.email = email

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email,
        }


def migrate():
    # Database migration logic
    return "migration_complete"
