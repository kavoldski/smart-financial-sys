class User:
    def __init__(self, user_id, name, email, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.balance = 0.0

    def register(self):
        # Code to register the user
        pass

    def login(self):
        # Code to log in the user
        pass

    def logout(self):
        # Code to log out the user
        pass

    def update_profile(self, name=None, email=None):
        if name:
            self.name = name
        if email:
            self.email = email