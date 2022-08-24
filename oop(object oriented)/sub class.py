import turtle


class Polygon:
    def __init__(self, sides, name, size=100, color='red', line_thickness=3):
        self.sides = sides
        self.name = name
        self.size = 100
        self.color = color
        self.line_thickness = line_thickness
        self.interior_angle = (self.sides - 2) * 180
        self.angle = self.interior_angle / self.sides

    def draw(self):
        turtle.color(self.color)
        turtle.pensize(self.line_thickness)
        for i in range(self.sides):
            turtle.forward(100)
            turtle.right(180 - self.angle)


# creating a subclass
class Square(Polygon):
    def __init__(self, size=100, color='red', line_thickness=3):
        super().__init__(4, 'square', size, color, line_thickness)

    def draw(self):
        turtle.begin_fill()
        super().draw()
        turtle.end_fill()


square = Square(color='blue')
print(square.sides)
print(square.size)
print(square.draw())
turtle.done()
