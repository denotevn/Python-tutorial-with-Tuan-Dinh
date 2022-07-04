class Point:

    description = "thuc hanh class voi python"

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    def move(self):
        print("move")
    def draw(self):
        print("Draw")
point = Point(10,20)
print("lam cai class nay de {}".format(point.__class__.description))
point.draw()
point.move()
print(point.x, point.y) # 10 20

