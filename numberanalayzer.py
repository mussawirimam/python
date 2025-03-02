def analyze_numbers():
    numbers = []
    while True:
        user_input = input("Enter a number (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")

    if not numbers:
        print("No numbers entered.")
        return

    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    print(f"\nAnalysis of {len(numbers)} numbers:")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")

    print("\nNumber distribution:")
    for num in numbers:
        if num < average:
            print(f"{num} is below average")
        elif num > average:
            print(f"{num} is above average")
        else:
            print(f"{num} is equal to average")

if __name__ == "__main__":
    analyze_numbers()
