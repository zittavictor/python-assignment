from car_rental import Car_Rental


def main():
    customer_name = input("Enter the customer's name: ")
    beginning_odometer = int(input("Enter the beginning odometer reading: "))
    ending_odometer = int(input("Enter the ending odometer reading: "))
    num_days = int(input("Enter the number of rental days: "))
    
    rental = Car_Rental(customer_name, ending_odometer, beginning_odometer, num_days)
    
    print(rental)


if __name__ == "__main__":
    main()
