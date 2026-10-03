import json

# Define the student dictionary
student = {
    "name": "Rahim",
    "age": 20,
    "department": "CSE"
}

# Convert dictionary to JSON string
json_string = json.dumps(student)

# Print the JSON string
print(json_string)