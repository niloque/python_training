"""Implementation for Rectangle class:"""

class Rectangle:
    """A Rectangle,

    Args:
        width: width of the rectangle
        height: height of the rectangle
    Both width and height should be positive numbers.
    """

    def __init__(self, width, height):
        if width <= 0:
            raise ValueError('Width has to be positive')
        if height <= 0:
            raise ValueError('Height has to be positive')
        self.width = width
        self.height = height

    def area(self):
        """Computes the area of the rectangle"""
        self.x = 0
        return self.height * self.width

    def perimeter(self):
        """Computes the perimeter of the rectangle"""
        return 2 * (self.height + self.width)

    def draw(self):
        pass


rect = Rectangle(10, 20)
print('Wysokość:', rect.height)
print('Szerokość:', rect.width)
print('Pole:', rect.area())
print('Obwod:', rect.perimeter())
print('x:', rect.x)