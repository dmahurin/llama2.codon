# simple file reader
# workaround for Codon's current inabilty to read file as unpackable bytes

def python(f):
    return f

@python
def fdread(fd, n):
    import os
    return os.read(fd, n)

@python
def fdopen(name):
    import os
    fd = os.open(name, os.O_RDONLY)
    return fd

@python
def fdtell(fd):
    import os
    return os.lseek(fd, 0, os.SEEK_CUR)

@python
def fdclose(fd):
    import os
    os.close(fd)

class File_:
    fd: int
    def __init__(self, name, mode):
        self.fd = fdopen(name)
    def read(self, n):
        return fdread(self.fd, n)
    def close(self):
        fdclose(self.fd)
    def tell(self):
        return fdtell(self.fd)
    def fileno(self):
        return self.fd
    def __enter__(self):
        return self
    def __exit__(self, t=None, v=None, tb=None):
        self.close()
    def __bool__(self):
        return self.fd > 0

def open(name, mode):
    r = File_(name, mode)
    return r
