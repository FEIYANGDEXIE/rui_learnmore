import threading
global_num = 0
#关于线程

def test1():
    global global_num
    for i in range(1000000):
        global_num += 1

    print("test1", global_num)


def test2():
    global global_num
    for i in range(1000000):
        global_num += 1

    print("test2", global_num)

t1 = threading.Thread(target=test1)
t2 = threading.Thread(target=test2)
t1.start()
t2.start()
