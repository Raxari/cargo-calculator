class BasePriceCalculator:
    def calculate_base_price(self, weight):
        # НОВАЯ ЛОГИКА - УВЕЛИЧИЛИ ЦЕНЫ (конфликт!)
        if weight <= 50:
            return 350
        elif weight <= 100:
            return 1200 
        elif weight <= 300:
            return 2500
        else:
            raise ValueError("Вес превышает максимально допустимый")