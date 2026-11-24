# 8. Plot line, bar, histogram, and pie charts using Python.
# Different types of charts using Matplotlib
import matplotlib.pyplot as plt

names = ['Rahul', 'Amit', 'Priya', 'Neha']
marks = [85, 90, 78, 88]

# Line Chart
plt.plot(names, marks, marker='o')
plt.title("Line Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Bar Chart
plt.bar(names, marks)
plt.title("Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Histogram
plt.hist(marks, bins=5)
plt.title("Histogram")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# Pie Chart
plt.pie(marks, labels=names, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()
