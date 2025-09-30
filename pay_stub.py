class Car_Rental:
    
    def __init__(self, customer_name, ending_odometer, beginning_odometer, num_days):
        self.customer_name = customer_name
        self.ending_odometer = ending_odometer
        self.beginning_odometer = beginning_odometer
        self.num_days = num_days
        self._rental_charge = 0.0
    
    @property
    def rental_charge(self):
        return self._calculate_rental_charge()
    
    def _calculate_rental_charge(self):
        DAILY_RATE = 62.50
        MILEAGE_RATE = 0.57
        
        miles_driven = self.ending_odometer - self.beginning_odometer
        total_charge = (self.num_days * DAILY_RATE) + (miles_driven * MILEAGE_RATE)
        
        return total_charge
    
    def __str__(self):
        miles_driven = self.ending_odometer - self.beginning_odometer
        rental_charge = self.rental_charge
        
        result = f"Customer Name: {self.customer_name}\n"
        result += f"Number of Rental Days: {self.num_days}\n"
        result += f"Miles Driven: {miles_driven}\n"
        result += f"Rental Charge: ${rental_charge:.2f}"
        
        return result
