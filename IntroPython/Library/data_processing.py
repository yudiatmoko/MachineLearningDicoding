# Pandas, for data processing and analytics
import pandas as pd

## Create DataFrame from dictionary
data = {
    'Name': ['John', 'Ilham', 'Yudiatmoko', 'Jawa'],
    'Age': [20, 21, 22, 24],
    'Job': ['Teacher', 'Designer', 'Doctor', 'Programmer']
}

df = pd.DataFrame(data)

## Show DataFrame
print(df)

# NumPy, scientific computing
import numpy

matrix = numpy.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(matrix)

# Matplotlib, data visualization
import matplotlib.pyplot as plt

## Data
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 18]

## Line Plot
plt.plot(x, y)

## Add title and axis labelling
plt.title('Line Plot Example')
plt.xlabel('Axis X')
plt.ylabel('Axis Y')

## Show
plt.show()

# Seaborn, data visualization
import seaborn as sns
import matplotlib.pyplot as plt

# Data
tips = sns.load_dataset('tips')  # create dataset

# Histogram Plot
sns.histplot(tips['total_bill'], kde=True)
plt.title('Histogram Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.show()