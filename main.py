class Rectangle:

    def __init__(self, width=5, height=10) -> None:
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height
    
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * self.height + 2 * self.width
    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            result = "Too big for picture."
        else:
            result = ''
            for line in range(self.height):
                result += '*' * self.width + '\n'
        return result

    def get_amount_inside(self, obj):
        h_num = self.height // obj.height
        w_num = self.width // obj.width
        return h_num * w_num

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

class Square(Rectangle):

    def __init__(self, side):
        self.height = side
        self.width = side

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.height = height
        self.width = height

    def __str__(self):
        return f'Square(side={self.height})'
