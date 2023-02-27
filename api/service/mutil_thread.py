from threading import Thread
import threading
import time


# def cal_square(numbers):
# 	print("calculate square number")
# 	for n in numbers:
# 		time.sleep(0.2)
# 		print ('square:', n*n)


# def cal_cube(numbers):
# 	print("calculate cube number \n")
# 	for n in numbers:
# 		time.sleep(0.2)
# 		print ('cube:', n*n*n)

# arr = [2,3,7,9]

# try:
# 	t = time.time()
# 	t1 = threading.Thread(target=cal_square, args=(arr,))
# 	t2 = threading.Thread(target=cal_cube, args=(arr,))
# 	t1.start()
# 	t2.start()
# 	t1.join()
# 	t2.join()
# 	print ("done in ", time.time()- t)
# except:
# 	print ("error")
 
import threading
import time
 
def daemon():
    print (threading.current_thread().name, 'Starting')
    time.sleep(2)
    print (threading.current_thread().name, 'Exiting')
 
def non_daemon():
    print (threading.current_thread().name, 'Starting')
    print (threading.current_thread().name, 'Exiting')
 
d = threading.Thread(name='daemon', target=daemon)
d.daemon = True
t = threading.Thread(name='non_daemon', target=non_daemon)
 
d.start()
t.start()

with (open('README.md', 'r') as fin,
      open('file2.txt', 'w+') as fout):
    fout.write(fin.read())
    
colors = ['red', 'blue', 'pink']
ints = [1, 3, 5, 4, 2]