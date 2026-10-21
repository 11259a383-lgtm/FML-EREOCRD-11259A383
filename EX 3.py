marks = [78, 85, 92, 67, 88, 90, 76]
print("Highest Mark:", max(marks))
print("Lowest Mark:", min(marks))
print("Average Mark:", sum(marks)/len(marks))
temperature = [30, 32, 31, 29, 35, 34, 33]

print("Maximum Temperature:", max(temperature))
print("Minimum Temperature:", min(temperature))
print("Average Temperature:", sum(temperature)/len(temperature))
Output
Maximum Temperature: 35
Minimum Temperature: 29
Average Temperature: 32.0
sales = [2500, 3000, 2800, 3500, 4000, 3800, 4200]
print("Total Sales:", sum(sales))
print("Average Sales:", sum(sales)/len(sales))

ids = [101, 102, 103, 104, 105, 106]

even = []
odd = []
for i in ids:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("Even IDs:", even)
print("Odd IDs:", odd)
values = [20, -5, 15, -10, 30, -2]
positive = 0
negative = 0
for i in values:
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1
print("Positive Values:", positive)
print("Negative Values:", negative)
customer_ids = [101, 102, 103, 102, 104, 105, 101]
duplicates = []
for i in customer_ids:
    if customer_ids.count(i) > 1 and i not in duplicates:
        duplicates.append(i)
print("Duplicate IDs:", duplicates)
prices = [250, 450, 120, 600, 350]
print("Highest Price:", max(prices))
print("Lowest Price:", min(prices))
salary = [25000, 30000, 40000, 35000]
new_salary = []
for s in salary:
    new_salary.append(s * 1.10)
print("Updated Salaries:", new_salary)
total_classes = 90
attended = 81
percentage = (attended / total_classes) * 100
print("Attendance Percentage:", percentage)
marks = [45, 67, 89, 32, 78, 55, 49]
passed = []
for m in marks:
    if m >= 50:
        passed.append(m)

print("Passed Students Marks:", passed)
prices = [120, 80, 150, 200]
total = sum(prices)
print("Total Bill:", total)
feedback = "good service good quality excellent service"
words = feedback.split()
for word in set(words):
    print(word, ":", words.count(word))
ages = [12, 25, 45, 67, 15]
for age in ages:
    if age < 18:
        print(age, "Child")
    elif age < 60:
        print(age, "Adult")
    else:
        print(age, "Senior Citizen")
units = 250
if units <= 100:
    bill = units * 2
elif units <= 200:
    bill = 100 * 2 + (units - 100) * 3
else:
    bill = 100 * 2 + 100 * 3 + (units - 200) * 5
print("Electricity Bill:", bill)
expenses = [12000, 15000, 18000, 11000, 17000]
highest = max(expenses)
month = expenses.index(highest) + 1
print("Highest Expense:", highest)
print("Month:", month)

