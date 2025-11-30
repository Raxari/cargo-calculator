class BasePriceCalculator:
    def calculate_base_price(self, weight):
        # ДРУГИЕ ИЗМЕНЕНИЯ - СИСТЕМА СКИДОК (конфликт!)
        if weight <= 50:
            price = 300
        elif weight <= 100:
            price = 1000
        elif weight <= 300:
            price = 2000
            # НОВОЕ: скидка для тяжелых грузов
            if weight > 200:
                price = int(price * 0.9)  # 10% скидка
        else:
            raise ValueError("Вес превышает максимально допустимый")
        return price