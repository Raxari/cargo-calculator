class ManualLiftCalculator:
    def calculate_manual_cost(self, weight, floor):
        if floor <= 1:
            return 0
        
        base_cost_per_floor = 300
        weight_factor = (weight + 99) // 100
        
        return base_cost_per_floor * (floor - 1) * weight_factor