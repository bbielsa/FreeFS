from dropbox import Dropbox

class DropboxConnector:
    def __init__(self, account):
        self.client = Dropbox(account.accessToken)

    # Dropbox does not like the "/" path for some stupid reason...
    # "" refers to the root directory
    @staticmethod
    def convert_to_dropbox_path(path):
        if path == "/":
            return ""
        else:
            return path

    def mkdir(self, path):
        self.client.files_create_folder(path)

    def chmod(self, path, mode):
        pass

    def chown(self, path, user_id, group_id):
        pass

    def getattr(self, path, file_handle=None):
        dropbox_path = DropboxConnector.convert_to_dropbox_path(path)
        metadata = self.client.files_get_metadata(dropbox_path)