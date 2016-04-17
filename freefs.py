from sys import argv
from fuse import FUSE, FuseOSError, Operations, LoggingMixIn
from connectors import FileStatus


class FreeFS(LoggingMixIn, Operations):
    def __init__(self):
        self.connectors = []
        pass
    """
    def getattr(self, path, fh=None):
        print("getattr called on %s" % path)
        return FileStatus()
    """

    def calculate_total_storage(self):
        total = 0

        for connector in self.connectors:
            total += connector.total_storage()

        return total

    def readdir(self, path, fh):
        test = ["hello", "world"]

        for directory in test:
            yield directory

if __name__ == "__main__":
    if len(argv) != 2:
        print("usage: %s <mount point>" % argv[0])
        exit(-1)
    else:
        fuse = FUSE(FreeFS(), argv[1], foreground=True)
