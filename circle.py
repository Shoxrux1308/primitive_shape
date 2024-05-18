from math import pi
class Circle:
    def __init__(self, r) -> None:
        self.r = r

    def getArea(self):
        """
        This method finds the area of the Circle.

        Args:
            No
        Returns:
            float or int: result.
        """
        return self.r**2*pi

        pass

    def getLength(self):
        """
        This method finds the length of the cirle.

        Args:
            No
        Returns:
            float or int: result..
        """
        return 2*pi*self.r
        pass

cir=Circle(2)
print(cir.getArea())
print(cir.getLength())