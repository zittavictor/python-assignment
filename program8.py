from pay_stub import Pay_Stub


def main():
    employee_name = input("Enter the employee's name: ")
    hours_worked = float(input("Enter hours worked: "))
    pay_rate = float(input("Enter pay rate: "))
    
    pay_stub = Pay_Stub(employee_name, hours_worked, pay_rate)
    
    print(pay_stub)
    print()


if __name__ == "__main__":
    print("=== Pay Stub 1 ===")
    main()
    
    print("=== Pay Stub 2 ===")
    main()
    
    print("=== Pay Stub 3 ===")
    main()
    
    print("=== SUMMARY INFORMATION ===")
    print(Pay_Stub.get_summary_information())
