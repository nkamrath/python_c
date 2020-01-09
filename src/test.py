
from ctypes import cdll
lib = cdll.LoadLibrary('libtest.so')

ret = lib.cprint(b"testing!\n")
print("returned: {}".format(ret))