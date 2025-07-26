def format_indian_currency(number: float) -> str:
    """
    Converts a floating-point number into a comma-separated string
    formatted according to the Indian numbering system.


    Args:
        number (float): The number to be formatted.


    Returns:
        str: A string representation of the number in Indian currency format.
    """
    # Convert the number to a string and split into integer and fractional parts
    s = str(number)
    if '.' in s:
        integer_part, fractional_part = s.split('.')
    else:
        integer_part, fractional_part = s, None


    # Handle the integer part formatting
    # The last three digits are grouped first, then groups of two.
    if len(integer_part) <= 3:
        formatted_integer = integer_part
    else:
        last_three = integer_part[-3:]
        other_digits = integer_part[:-3]
        # Add commas every two digits from the right for the remaining part
        other_digits_formatted = ",".join(other_digits[max(0, i-2):i] for i in range(len(other_digits), 0, -2))[::-1]
        formatted_integer = other_digits_formatted + ',' + last_three


    # Combine the formatted integer part with the fractional part, if it exists
    if fractional_part:
        return f"{formatted_integer}.{fractional_part}"
    else:
        return formatted_integer


# --- Example Usage ---
if __name__ == "__main__":
    num1 = 123456.7891
    num2 = 987654321
    num3 = 5043.2
    num4 = 100


    print(f"{num1} -> {format_indian_currency(num1)}")
    print(f"{num2} -> {format_indian_currency(num2)}")
    print(f"{num3} -> {format_indian_currency(num3)}")
    print(f"{num4} -> {format_indian_currency(num4)}")
