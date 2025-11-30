class BasePriceCalculator:
    def calculate_base_price(self, weight):
        # ОБЪЕДИНЕННАЯ ЛОГИКА: новые цены + система скидок
        if weight <= 50:
            price = 350
        elif weight <= 100:
            price = 1200
        elif weight <= 300:
            price = 2500
            if weight > 200:
                price = int(price * 0.9)  # 10% скидка
        else:
            raise ValueError("Вес превышает максимально допустимый")
        return price