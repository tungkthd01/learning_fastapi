import ctypes

# a = [1,2,3]
# b = a
# b[0]= 100

# print(a)
# con tro trong python
a = ctypes.c_long(200)
print(type(a))

ptr  = ctypes.pointer(a)

print(ptr.contents.value)
print(ctypes.addressof(ptr.contents))

ptr.contents.value = 300
print(a)
ptr_address = ctypes.addressof(ptr.contents)

ptr_new = ctypes.cast(ptr_address, ctypes.POINTER(ctypes.c_long))
print('ptr_new:',ptr_new.contents.value)
a = 100
b = 200
a,b = b, a
print(a,b)
# list comprehension

item = [n*2 for n in range(10)]

# tuple, list, dictionary but dict get key
tpl = {'tung': 1, "khai": 2}
x,y = tpl
print(tpl['tung'])
print(x,y)