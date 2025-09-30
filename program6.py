from walk import Walk


def main():
    walker_name = input("Enter the walker's name: ")
    num_steps = int(input("Enter the number of steps: "))
    step_length = int(input("Enter the length of step in inches: "))
    
    walker = Walk(walker_name, num_steps, step_length)
    
    miles = walker.calculate_miles()
    
    print(f"\n{walker.walker_name}'s walk with {walker.num_steps:,} steps averaging {walker.step_length} inches per step equates to {miles:.2f} miles.")


if __name__ == "__main__":
    main()
