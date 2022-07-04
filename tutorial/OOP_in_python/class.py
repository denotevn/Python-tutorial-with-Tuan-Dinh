class Car:
    range_of_vehilce = "Car"
    def __init__(self, name, color, ingredient):
        self.name = name
        self.color = color
        self.ingredient = ingredient

# instantiate the Car class
toyota = Car("Toyota", "Đỏ", "Điện")
lamborghini = Car("Lamborghini", "Vàng", "Deisel")
porsche = Car("Porsche", "Xanh", "Gas")

# access the class attributes
print("Porsche là {}.".format(porsche.__class__.range_of_vehilce))
print("Toyota là {}.".format(toyota.__class__.range_of_vehilce))
print("Lamborghini cũng là {}.".format(lamborghini.__class__.range_of_vehilce))

# access the instance attributes
print("Xe {} có màu {}. {} là nguyên liệu vận hành.".format( toyota.name, toyota.color, toyota.ingredient))
print("Xe {} có màu {}. {} là nguyên liệu vận hành.".format( lamborghini.name, lamborghini.color,lamborghini.ingredient))
print("Xe {} có màu {}. {} là nguyên liệu vận hành.".format( porsche.name, porsche.color, porsche.ingredient))

