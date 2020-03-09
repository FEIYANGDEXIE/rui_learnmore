#buff为4096，读一个大数据文本
def readtobuff(ff, buff=4096):
    global start
    while True:
        data = ff.read(buff)
        for idx,i in enumerate(data):
            if i == '\n' or i == '\r':
                print(data[start:idx])
                start = idx
        print(data[start:])
        if not data:
            break
        yield data
start=0
f = open('./stopword.txt', encoding='utf-8' )
for chuck in readtobuff(f):
    print('1')

