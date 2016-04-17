import time


class FileStatus:
    def __init__(self):
        self.group_id = 0
        self.user_id = 0

        self.mode = 0

        self.device = 0

        self.inode = 0

        self.num_links = 0

        self.access_time = 0
        self.modify_time = 0
        self.create_time = 0

        self.size = 0

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

