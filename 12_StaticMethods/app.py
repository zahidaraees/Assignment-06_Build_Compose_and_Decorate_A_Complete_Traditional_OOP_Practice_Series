# Define the TemperatureConverter class
class TemperatureConverter:
    
    # Static method to convert Celsius to Fahrenheit
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32

celsius = 25
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)

print(f"{celsius}°C is equal to {fahrenheit}°F")