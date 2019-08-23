
print("Hello!, sagar welcome to the world of python")
print('My hovercraft is  full of eels')

class Circle(object):

    def __init__(self,radius):
         self.radius=radius

    def area(self):
        return 3.14*(self.radius**2)

    def perimeter(self):
        return 2*3.14*self.radius

    def test(self,x,y):
        print(x+y+self.radius)

circle = Circle(2)
circle_area = circle.area()
circle_perimeter = circle.perimeter()
circle.test(1,2)

print(circle_area)
print(circle_perimeter)

my_string = "hello world"
k = [(i.upper(), len(i)) for i in my_string]
print(k)

def f1():
    x=100
    print(x)
x=+1
print(x)
f1()