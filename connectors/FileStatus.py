import time


class FileStatus:
    def __init__(self):
        self.group_id = None
        self.user_id = None

        self.mode = None

        self.device = None

        self.inode = None

        self.num_links = None

        self.access_time = None
        self.modify_time = None
        self.create_time = None

        self.size = None

    @property
    def st_gid(self):
        return self.group_id

    @property
    def st_uid(self):
        return self.user_id

    @property
    def st_mode(self):
        return self.mode

    @property
    def st_ino(self):
        pass

    @property
    def st_device(self):
        return self.device

    @property
    def st_nlink(self):
        return self.num_links

    @property
    def st_atime(self):
        return self.access_time

    @property
    def st_ctime(self):
        return self.create_time

    @property
    def st_mtime(self):
        return self.modify_time

    @property
    def st_ino(self):
        return self.inode

    @staticmethod
    def get_unix_timestamp(date):
        return time.mktime(date.timetuple())

