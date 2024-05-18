from polygon import Polygon

class Square(Polygon):
    def __init__(self, height,width) -> None:
        super().__init__(height,width)
    
    def getArea1(self):
        return self.height**2
    def getPerimeter2(self):
        return self.height*4
squ=Square(12,12)
print(squ.getArea1())
print(squ.getPerimeter2())