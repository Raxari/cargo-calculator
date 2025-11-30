# Версия 2.0.0 - улучшенная система цен со скидками

from base_calculator import BasePriceCalculator
from elevator_calculator import ElevatorCalculator
from manual_calculator import ManualLiftCalculator

class CargoCalculator:
    def calculate_total_cost(self, weight, floor, has_elevator):
        base_calc = BasePriceCalculator()
        elevator_calc = ElevatorCalculator()
        manual_calc = ManualLiftCalculator()
        
        base_price = base_calc.calculate_base_price(weight)
        
        if has_elevator:
            return base_price
        else:
            manual_cost = manual_calc.calculate_manual_cost(weight, floor)
            return base_price + manual_cost

if __name__ == "__main__":
    calculator = CargoCalculator()
    
    cost = calculator.calculate_total_cost(250, 3, False)
    print(f"Стоимость подъема: {cost} руб.")
    
    # Дополнительные примеры для проверки
    print(f"50кг с лифтом: {calculator.calculate_total_cost(50, 5, True)} руб.")
    print(f"100кг без лифта на 2 этаж: {calculator.calculate_total_cost(100, 2, False)} руб.")