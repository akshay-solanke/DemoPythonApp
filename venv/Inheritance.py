class mamel:
    def walk(self):
        print('walk')


class dog(mamel):
    def park(self):
        print('park')



class cat(mamel):
    pass

dog1=dog()
dog1.walk()
dog2=dog()
dog2.park()
