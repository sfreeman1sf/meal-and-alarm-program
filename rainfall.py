# Part 1: Average Rainfall Program

def main():
    years = int(input("Enter the number of years: "))

    total_rainfall = 0.0
    total_months = 0

    for year in range(1, years + 1):
        print(f"\nYear {year}")
        for month in range(1, 13):
            rainfall = float(input(f"Enter the inches of rainfall for month {month}: "))
            total_rainfall += rainfall
            total_months += 1

    average_rainfall = total_rainfall / total_months if total_months else 0

    print("\n--- Rainfall Report ---")
    print(f"Total months: {total_months}")
    print(f"Total rainfall (inches): {total_rainfall:.2f}")
    print(f"Average rainfall per month: {average_rainfall:.2f}")

if __name__ == "__main__":
    main()