# Create a program that converts temperatures between Celsius, Fahrenheit, and Kelvin scales. The program should prompt the user to input a temperature value and the original unit of measurement.
# It should then convert the temperature to the other two units and display the converted values to the user. For example, if the user enters a temperature of 25 degrees Celsius,
# the program should convert it to Fahrenheit and Kelvin, and present the converted values as outputs



def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32


def convert_temperature(value, unit):
    value = float(value)

    if unit.lower() == 'celsius':
        fahrenheit = celsius_to_fahrenheit(value)
        kelvin = celsius_to_kelvin(value)
        print(f"{value}° Celsius is equal to {fahrenheit:.2f}° Fahrenheit and {kelvin:.2f} Kelvin.")

    elif unit.lower() == 'fahrenheit':
        celsius = fahrenheit_to_celsius(value)
        kelvin = fahrenheit_to_kelvin(value)
        print(f"{value}° Fahrenheit is equal to {celsius:.2f}° Celsius and {kelvin:.2f} Kelvin.")

    elif unit.lower() == 'kelvin':
        celsius = kelvin_to_celsius(value)
        fahrenheit = kelvin_to_fahrenheit(value)
        print(f"{value} Kelvin is equal to {celsius:.2f}° Celsius and {fahrenheit:.2f}° Fahrenheit.")

    else:
        print("Invalid unit of measurement. Please enter 'Celsius', 'Fahrenheit', or 'Kelvin'.")


def main():
    print("Temperature Converter")
    temp_value = input("Enter the temperature value: ")
    temp_unit = input("Enter the unit of measurement (Celsius, Fahrenheit, Kelvin): ")

    convert_temperature(temp_value, temp_unit)


if __name__ == "__main__":
    main()
