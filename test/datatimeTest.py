import time
def unixtime():
    #処理
    start = int(time.time())
    end = start + 5
    return start, end

if __name__ == '__main__':
    s, e = unixtime()
    print(s,e)
    print(type(s))
    print(type(e))
