from datetime import datetime

# Get current date and time
current_time = datetime.now()

# Format date and time as YYYY-MM-DD HH:MM:SS
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# Display output
print("Current Date and Time:", formatted_time)