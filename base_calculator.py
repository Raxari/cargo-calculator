class BasePriceCalculator:
    def calculate_base_price(self, weight):
        if weight <= 50:
            return 300
        elif weight <= 100:
            return 1000
        elif weight <= 300:
            return 2000
        else:
            raise ValueError("Вес превышает максимально допустимый")