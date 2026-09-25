#Write a program to display current date and time using datetime module.

from datetime import datetime

# Get current date and time
now = datetime.now()

print("Current date and time:", now)
print("Current date:", now.date())
print("Current time:", now.time())

print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
