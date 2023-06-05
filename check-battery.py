from djitellopy import tello

# Create an instance of the Tello class
me = tello.Tello()

# Connect to the Tello drone
me.connect()

# Get the battery level of the Tello drone and print it
battery_level = me.get_battery()
print("Battery Level:", battery_level)
