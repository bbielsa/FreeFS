from sys import argv
from fuse import FUSE, FuseOSError, Operations, LoggingMixIn


class FreeFS(LoggingMixIn, Operations):
    def __init__(self):
        pass

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
