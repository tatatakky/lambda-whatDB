class TestAPI:
    def __init__(self, data):
        self.data = data
    def printer(self):
        print(self.data[0])

if __name__ == '__main__':
    data = [[1,2,3],[4,5,6],[7,8,9]]
    testapi = TestAPI(data)
    testapi.printer()

