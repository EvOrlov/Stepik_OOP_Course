class Laptop:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f"{self.brand} {self.model}"

laptop1 = Laptop('hp', '16-bw0xx', 58000)
laptop2 = Laptop('hp', '17-bw0xx', 59000)