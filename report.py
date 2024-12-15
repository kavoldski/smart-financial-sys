# Class to create report for all user account
class UserReport:
    def __init__(self, user_list):
        self.user_list = user_list
        self.report = {}
        self.create_report()
        