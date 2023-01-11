class GeometricObject:
    def __init__(self, c = "green", f = True) -> None:
        self.__color = c
        self.__filled = f

    def get_color(self):
        return self.__color

    def set_color(self, s):
        self.__color = s

    def is_filled(self):
        return self.__filled

    def set_filled(self, f):
        self.__filled = f
    
    def __str__(self) -> str:
        return "GeometricObject: color = " + str(self.__color) + " filled = " + str(self.__filled)

class Triangle(GeometricObject):
    def __init__(self, s1 = 1.0, s2 = 1.0, s3 = 1.0, c = None, f = None) -> None:
        is_valid = s1 + s2 > s3 and s1 + s3 > s2 and s3 + s2 > s1
        if not is_valid:
            raise RuntimeError("Invalid sides for triangle")

        super().__init__()
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
        

    def get_side1(self):
        return self.side1

    def get_side2(self):
        return self.side2

    def get_side3(self):
        return self.side3

    def get_area(self):
        s = self.get_perimeter() / 2.
        return (s*((s - self.side1) * (s - self.side2) * (s - self.side3))) ** 0.5

    def get_perimeter(self):
        return self.side1 + self.side2 + self.side3

    def __str__(self) -> str:
        return "Triangle: side1 = " + str(self.side1) + " side2 = " + str(self.side2) + " side3 = " + str(self.side3)


def main():
    s1 = float(input("Enter side1: "))
    s2 = float(input("Enter side2: "))
    s3 = float(input("Enter side3: "))

    try:
        trig = Triangle(s1, s2, s3)
    except RuntimeError as re:
        print(re)
        return

    print("The area is " + str(trig.get_area()))
    print("The perimeter is " + str(trig.get_perimeter()))

if __name__ == "__main__":
    main()