
import ctypes as ct

lib = ct.cdll.LoadLibrary('libtest.so')

ret = lib.cprint(b"testing!\n")

print(lib.cprint.argtypes)
print("returned: {}".format(ret))

sum_list = [1, 2, 3]


c_list = (ct.c_int * len(sum_list))(*sum_list)
for i in range(0, len(c_list)):
	print(c_list[i])


print(lib.csum(c_list, ct.c_int(len(c_list))))
print(c_list[-1])
