# temperature_alert.py

# Accept temperature in Celsius
temperature = 35

# Determine status
if temperature < 20:
    status = "Cold"
elif 20 <= temperature <= 30:
    status = "Normal"
else:
    status = "Hot"

print(f"Temperature: {temperature}°C")
print(f"Status: {status}")
