from dropbox import Dropbox
from connectors import FileStatus


class DropboxConnector:
    def __init__(self, account):
        self.client = Dropbox(account["access_token"])

    # Dropbox does not like the "/" path for some stupid reason...
    # "" refers to the root directory
    @staticmethod
    def convert_to_dropbox_path(path):
        if path == "/":
            return ""
        else:
            return path

    def make_directory(self, path):
        self.client.files_create_folder(path)

    def change_mode(self, path, mode):
        pass

    def change_owner(self, path, user_id, group_id):
        pass

    def getattr(self, path, file_handle=None):
        dropbox_path = DropboxConnector.convert_to_dropbox_path(path)
        metadata = self.client.files_get_metadata(dropbox_path)
        file_status = FileStatus()

        # I'm going to change this hard coded stuff later
        file_status.group_id = 20
        file_status.user_id = 501

    @property
    def total_storage(self):
        space_usage = self.client.users_get_space_usage()
        return space_usage.allocation.get_individual()

    @property
    def free_storage(self):
        space_usage = self.client.users_get_space_usage()
        return space_usage.used