
class Car:
          # self referring to the car
    def __init__(self, model, year, color, for_sale):  # constructor
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    # Methods
    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stopped the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")