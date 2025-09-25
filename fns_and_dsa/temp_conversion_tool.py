# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS = 5 / 9
CELSIUS_TO_FAHRENHEIT = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS
    return round(celsius, 2)

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit"""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT) + 32
    return round(fahrenheit, 2)

def main():
    try:
        temp = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            result = convert_to_celsius(temp)
            print(f"{temp}°F is {result}°C")
        elif unit == "C":
            result = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {result}°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
