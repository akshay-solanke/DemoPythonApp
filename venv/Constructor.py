class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self):
        print('move')

    def stop(self):
        print('stop')


point = Point(10,20)
print(point.x)