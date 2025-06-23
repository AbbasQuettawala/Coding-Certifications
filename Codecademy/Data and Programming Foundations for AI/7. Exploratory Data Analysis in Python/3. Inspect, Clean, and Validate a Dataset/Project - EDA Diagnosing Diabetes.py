'''
EDA: Diagnosing Diabetes
In this project, you’ll imagine you are a data scientist interested in exploring data that looks at how certain diagnostic factors affect the diabetes outcome of women patients.

You will use your EDA skills to help inspect, clean, and validate the data.

Note: This dataset is from the National Institute of Diabetes and Digestive and Kidney Diseases. It contains the following columns:

Pregnancies: Number of times pregnant
Glucose: Plasma glucose concentration at 2 hours in an oral glucose tolerance test
BloodPressure: Diastolic blood pressure
SkinThickness: Triceps skinfold thickness
Insulin: 2-Hour serum insulin
BMI: Body mass index
DiabetesPedigreeFunction: Diabetes pedigree function
Age: Age (years)
Outcome: Class variable (0 or 1)
Let’s get started!

Setup Instructions
You have two options of completing this assignment. Either here, within Codecademy’s output terminal, or on your own, in case you’re more comfortable using a Jupyter notebook.If you choose to do this project on your computer instead of Codecademy, you can download what you’ll need by clicking the “Download” button below. If you need help setting up your computer, be sure to check out our setup guides:

Command Line Interface Setup
Introducing Jupyter Notebook
Setting up Jupyter Notebook
Getting Started with Jupyter
Getting More out of Jupyter Notebook
Open EDA Diagnosing Diabetes.ipynb and follow the steps in the Jupyter Notebook. If you get stuck, you can look at EDA Diagnosing Diabetes_Solution.ipynb for the answer.

Download
Tasks
16/16 complete
Mark the tasks as complete by checking them off
Initial Inspection
1.
First, familiarize yourself with the dataset here.

Look at each of the nine columns in the documentation.

What do you expect each data type to be?

Take a look at the structure of the data and each of the columns.

Here are the expected data types for each column:

Pregnancies: int64
Glucose: int64
BloodPressure: int64
SkinThickness: int64
Insulin: int64
BMI: float64
DiabetesPedigreeFunction: float64
Age: int64
Outcome: int64
2.
Next, let’s load in the diabetes data to start exploring.

Load the data in a variable called diabetes_data and print the first few rows.

Note: The data is stored in a file called diabetes.csv.

3.
How many columns (features) does the data contain?

4.
How many rows (observations) does the data contain?

Further Inspection
5.
Let’s inspect diabetes_data further.

Do any of the columns in the data contain null (missing) values?

6.
If you answered no to the question above, not so fast!

While it’s technically true that none of the columns contain null values, that doesn’t necessarily mean that the data isn’t missing any values.

When exploring data, you should always question your assumptions and try to dig deeper.

To investigate further, calculate summary statistics on diabetes_data using the .describe() method.

7.
Looking at the summary statistics, do you notice anything odd about the following columns?

Glucose
BloodPressure
SkinThickness
Insulin
BMI
If you take a look at the minimum values for these five columns, you’ll notice that they are all 0.

How can Blood Pressure or BMI be 0? That makes no sense! These values also seem to be way off from their respective medians and means, another indicator that something is off.

One way to interpret this is that these are missing values in the data.

8.
Do you spot any other outliers in the data?

In addition to the 0 values that show up for the five columns above, there appear to be additional outliers, such as:

The maximum value of the Insulin column is 846, which is abnormally high.
The maximum value of the Pregnancies column is 17. While having 17 pregnancies is not impossible, this case might be something to look further into to determine its accuracy.
As you can see, EDA helps inform the data cleaning process by helping catch things that aren’t immediately obvious.

9.
Let’s see if we can get a more accurate view of the missing values in the data.

Use the following code to replace the instances of 0 with NaN in the five columns mentioned:

diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.nan)

Copy to Clipboard

10.
Next, check for missing (null) values in all of the columns just like you did in Step 5.

Now how many missing values are there?

11.
Let’s take a closer look at these rows to get a better idea of why some data might be missing.

Print out all of the rows that contain missing (null) values.

To print out the rows with missing values, you can use the following code:

print(diabetes_data[diabetes_data.isnull().any(axis=1)])

Copy to Clipboard

12.
Go through the rows with missing data. Do you notice any patterns or overlaps between the missing data?

One thing you might notice is that most rows with missing data have missing values in more than one column. In fact, every single row with at least one missing value also has a missing value in the insulin column. This is a clue as to why this data is missing! If patients did not have their insulin measured, why might they also not have had these other measurements taken?

Depending on how much data is missing, you might choose to remove specific rows or impute the missing values somehow.

13.
Next, take a closer look at the data types of each column in diabetes_data.

Does the result match what you would expect?

To print the data types of each column, you can use .dtypes:

print(diabetes_data.dtypes)

Copy to Clipboard

The outlook should look like:

Pregnancies                   int64
Glucose                     float64
BloodPressure               float64
SkinThickness               float64
Insulin                     float64
BMI                         float64
DiabetesPedigreeFunction    float64
Age                           int64
Outcome                      object
dtype: object

Copy to Clipboard

Alternatively, you can use the .info() method, which will print out a concise summary of the DataFrame with the data types of each column included:

print(diabetes_data.info())

Copy to Clipboard

The output should look like this:

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 768 entries, 0 to 767
Data columns (total 9 columns):
 #   Column                    Non-Null Count  Dtype  
---  ------                    --------------  -----  
 0   Pregnancies               768 non-null    int64  
 1   Glucose                   768 non-null    int64  
 2   BloodPressure             768 non-null    int64  
 3   SkinThickness             768 non-null    int64  
 4   Insulin                   768 non-null    int64  
 5   BMI                       768 non-null    float64
 6   DiabetesPedigreeFunction  768 non-null    float64
 7   Age                       768 non-null    int64  
 8   Outcome                   768 non-null    object  
dtypes: float64(2), int64(7)
memory usage: 54.1 KB
None

Copy to Clipboard

It looks like the Outcome column is of type object (string) even though in our initial inspection we expected it to be of type int64.

Let’s figure out why this might be.

14.
To figure out why the Outcome column is of type object (string) instead of type int64, print out the unique values in the Outcome column.

To print out the unique values of Outcome, you can use the .unique() method:

print(diabetes_data.Outcome.unique())

Copy to Clipboard

You should see the following output:

['1' '0' 'O']

Copy to Clipboard

Notice that we have instances of the character 'O' in addition to the number 0.

The documentation tells us that the value of the Outcome column should either be a 0 or a 1, so it seems likely that instances of the character 'O' are misentries.

15.
How might you resolve this issue?

A possible next step would be to replace instances of 'O' with 0 and convert the Outcome column to type int64.

Next Steps
16.
Congratulations! In this project, you saw how EDA can help with the initial data inspection and cleaning process. This is an important step as it helps to keep your datasets clean and reliable.

Here are some ways you might extend this project if you’d like:

Use .value_counts() to more fully explore the values in each column.
Investigate other outliers in the data that may be easily overlooked.
Instead of changing the 0 values in the five columns to NaN, try replacing the values with the median or mean of each column.
'''



import codecademylib3
import pandas as pd
import numpy as np

# code goes here

# Printing data
diabetes_data = pd.read_csv('diabetes.csv')
print(diabetes_data.head())

# Number of columns
print(len(diabetes_data.columns))

# Number of rows
print(len(diabetes_data))

# Finding null values:
print(diabetes_data.isnull().sum())

# Investigating further:
print(diabetes_data.describe())

# Values in Glucose, BloodPressure etc cant be 0, not possible, we must have missing values

# There are also some outliers:
# The maximum value of the Insulin column is 846, which is abnormally high.
# The maximum value of the Pregnancies column is 17. While having 17 pregnancies is not impossible, this case might be something to look further into to determine its accuracy.#

diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.nan)

print(diabetes_data.isnull().sum())

print(diabetes_data[diabetes_data.isnull().any(axis=1)])

print(diabetes_data.dtypes)

print(diabetes_data.Outcome.unique())

# A possible next step would be to replace instances of 'O' with 0 and convert the Outcome column to type int64.





