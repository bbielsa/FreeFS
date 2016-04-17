import json


class AccountLoader:
    def __init__(self, accounts_file_path):
        self.accounts = []
        self.accounts_file = open(accounts_file_path, "r")

    def load_accounts(self):
        for account in json.load(self.accounts_file):
            self.accounts += [account]
