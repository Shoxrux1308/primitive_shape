from polygon import Polygon

class Rectangle(Polygon):
    def __init__(self, height, width) -> None:
        super().__init__(height, width)
    def getPerimeter(self):
        return self.height*2+self.width*2
    def getArea(self):
        return self.height*self.height
rec=Rectangle(12,11)

print(rec.getPerimeter(), rec.getArea())