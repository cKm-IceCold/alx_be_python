def safe_divide(numerator, denominator):
    try:
        # Convert inputs explicitly to floats
        numerator = float(numerator)
        denominator = float(denominator)

        # Check for division by zero
        if denominator == 0:
            return "Error: Cannot divide by zero."

        result = numerator / denominator
        return f"The result of the division is {result}"

    except ValueError:
        return "Error: Please enter numeric values only."

    except Exception as e:
        return f"An unexpected error occurred: {e}"
