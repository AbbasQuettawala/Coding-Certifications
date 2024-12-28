"""
Suppose you are a medical professional curious about how certain factors contribute to medical insurance costs. Using a formula that estimates a person’s yearly insurance costs, you will investigate how different factors such as age, sex, BMI, etc. affect the prediction.

Note: while insurance companies do use BMI in their calculations, and that is reflected in this project, BMI is not necessarily an accurate predictor of health. As data scientists, we should always be skeptical of quantitative measures like BMI that reduce complex phenomena to a single number.

Setup Instructions
You have two options of completing this assignment. Either here, within Codecademy’s output terminal, or on your own, in case you’re more comfortable using a Jupyter notebook.If you choose to do this project on your computer instead of Codecademy, you can download what you’ll need by clicking the “Download” button below. If you need help setting up your computer, be sure to check out our setup guides:

Command Line Interface Setup
Introducing Jupyter Notebook
Setting up Jupyter Notebook
Getting Started with Jupyter
Getting More out of Jupyter Notebook
Open Python Syntax Medical Insurance Project.ipynb and follow the steps in the Jupyter Notebook. If you get stuck, you can look at Python Syntax Medical Insurance Project_Solution.ipynb for the answer.
"""
# create the initial variables below
age = 28
sex = 0
bmi = 26.2
num_of_children  = 3
smoker = 0

# Add insurance estimate formula below
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000*smoker - 12500

print(f"This person's insurance cost is {insurance_cost} dollars")

# Age Factor
age += 4
new_insurance_cost = 50 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000*smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print(f"The change in cost of insurance after increasing the age by 4 years is {change_in_insurance_cost} dollars.")

# BMI Factor
age = 28
bmi += 3.1

new_insurance_cost = 50 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000*smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print(f"The change in estimated insurance cost after increasing BMI by 3.1 is {change_in_insurance_cost}dollars.")

# Male vs. Female Factor
bmi = 26.2
sex = 1

new_insurance_cost = 50 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000*smoker - 12500

change_in_insurance_cost = new_insurance_cost - insurance_cost

print(f"The change in estimated cost for being male instead of female is {change_in_insurance_cost} dollars.")





# Extra Practice