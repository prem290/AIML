# Generate and Test Algorithm for 4-digit PIN

# Allowed even digits
even_digits = {'0', '2', '4', '6', '8'}

print("Possible PINs:")

count = 0

# Generate all 4-digit numbers from 0000 to 9999
for pin in range(10000):

    # Convert number to a 4-digit string using zfill()
    pin_str = str(pin).zfill(4)

    # Test Condition 1: All digits must be even
    if all(digit in even_digits for digit in pin_str):

        # Test Condition 2: Sum of digits must be 16
        digit_sum = sum(int(digit) for digit in pin_str)

        if digit_sum == 16:
            print(pin_str)
            count += 1

print("\nTotal Possible PINs:", count)