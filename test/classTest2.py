import time
class Logs:
    def __init__(self,d):
        self.d = d
    def setting(self):
        Id = self.d[0]
        start_time = int(time.time())
        end_time = start_time + 5
        start_amount = self.d[1]
        end_amount = self.d[2]
        return {'Id': Id, 'start_time': start_time, 'end_time': end_time, 'start_amount': start_amount, 'end_amount': end_amount}

if __name__ == '__main__':
    x = Logs([9999999999999, 4000000,4000005]).setting()
    print(x)
