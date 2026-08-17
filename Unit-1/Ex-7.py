# 1. Create a dictionary
user = {
    "name": "Divyesh",
    "age": 21,
    "city": "Rajkot"
}
print("Original dictionary:", user)

# 2. Use common methods
# Get a value safely (returns None if key is missing)
job = user.get("job", "Not Specified")
print("Job status:", job)

# Add or update items
user.update({"age": 22, "country": "INDIA"})
print("Updated dictionary:", user)

# Delete an item
user.pop("city")
print("After removing city:", user)

# 3. Iterate (Loop)
print("\n--- Looping ---")

# Loop through keys and values together
for key, value in user.items():
    print(f"{key}: {value}")
