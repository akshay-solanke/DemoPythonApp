class Point:
    def move(self):
        print('move')

    def stop(self):
        print('stop')


# NOTE:
# class name always need to start with upper case parameter.
# every class needs to define an object which is nothing but an instance of the class
# object contains actual values and class is nothing but an footprint of an objects or we can say functions
point1 = Point()  # here point1 is an object of Point class
point1.stop()  # we are calling function stop using object with the class reference

# object can have attributes like below
point1.x = 200
print(point1.x)

# one class can have multiple objects like below
point2 = Point()
point2.move()