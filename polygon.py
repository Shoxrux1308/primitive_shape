class Polygon:
    def __init__(self, height, width) -> None:
        self.height = height
        self.width = width

    def getArea(self):
        """
        This method finds the area of the Polygon.

        Args:
            No
        Returns:
            float or int: return perimeter of the polygon.
        """
        return self.height*self.width
        pass

    def getPerimeter(self):
        """
        This method finds the perimeter of the Polygon.

        Args:
            No
        Returns:
            float or int: return perimeter of the polygon.
        """
        return self.height*2+self.width*2
        pass
polygon=Polygon(25,22)
