class Shape:
    def __init__(self, name):
        self.name = name

    def draw(self):
        print(self.name)

    def area(self): # 로직은 없지만 해두게 되면 자식 클래스들이 동일한 메서드를 override 할 수 있겠네요.
        pass

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
        print(f'반지름이 {self.radius}인 {self.name}이 생성되었습니다.')

    def draw(self):
        print(f'이름이 {self.name}인 원의 넓이는 {self.area()}')

    def area(self):
        return 3.14 * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self,name ,width, height):
        super().__init__(name)
        self.width = width
        self.height = height
        print(f'너비가 {self.width}, 높이가 {self.height}인 {self.name}이 생성되었습니다.')

    def draw(self):
        # 메서드가 override 된거긴 한데 부모의 로직을 아예 안쓰는거죠
        print(f'이름이 {self.name}인 직사각형의 넓이는 {self.area()}입니다.')

    def area(self):
        return self.width * self.height

circle = Circle('원1', 5)
circle.draw()
print(f'원의 넓이 : {circle.area()}')

rectangle = Rectangle('직사각형1', 10, 8)
rectangle.draw()
print(f'직사각형의 넓이: {rectangle.area()}')