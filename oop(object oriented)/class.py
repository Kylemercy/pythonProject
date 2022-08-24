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
        turtle.done()


square = Polygon(4, 'square')
pentagon = Polygon(5, 'pentagon')

print(square.sides)
print(square.name)
print(square.interior_angle)
print(square.angle)

print(pentagon.sides)
print(pentagon.name)
print(pentagon.interior_angle)
print(pentagon.angle)
# square.draw()
pentagon.draw()
