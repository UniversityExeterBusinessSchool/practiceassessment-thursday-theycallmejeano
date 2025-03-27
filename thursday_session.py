#######################################################################################################################################################
# 
# Name: Jean Githae
# SID: 750000049
# Exam Date: 27 March 2025
# Module: BEMM458
# Github link for this assignment:  
#
# ######################################################################################################################################################
# 
# Instruction 1. Read the questions and instructions carefully and complete scripts.

# Instruction 2. Only ethical and minimal use of AI is allowed. You might use AI to give advice on how to use a tool or programming language.  
#                You must not use AI to create the code. You might make use of AI to aid debugging of the code.  
#                You must indicate clearly how and where you have used AI.

# Instruction 3. Copy the output of the code and insert it as a comment below your code e.g # OUTPUT (23,45)

# Instruction 4. Ensure you provide comments for the code and the output to show contextual understanding.

# Instruction 5. Upon completing this test, commit to Git, copy and paste your code into the word file and upload the saved file to ELE.
#                There is a leeway on when you need to upload to ELE, however, you must commit to Git at 
#                the end of your session.

# ######################################################################################################################################################
# %%
# Question 1 - Loops
# Create a list and use a for loop to answer the following question:
# You are given a dictionary called key_comments. Your allocated keys are the first and last digit of your SID.
# Find the start and end position of each of the items in the sentence using the find command.
# Create and populate a list called my_list with a tuple of (start location, end location) for each value in comments 
 

customer_feedback = """Your recent order experience has been satisfactory overall. While there were some minor issues,
we appreciate the effort made to resolve them promptly."
"""

# List of words to search for
key_comments = {
    0: 'satisfactory',
    1: 'order',
    2: 'effort',
    3: 'issues',
    4: 'promptly',
    5: 'appreciate',
    6: 'experience',
    7: 'resolve',
    8: 'overall',
    9: 'minor'
}

# NOTE: I'm interpreting this question That I need to search for my assigned words in the sentence
# define the start and end digits of my SID
start_digit = 7
end_digit = 9

# get my assigned value using dict comprehension
start_word_my_id = key_comments.get(start_digit) # resolve
end_word_my_id = key_comments.get(end_digit) # minor

start_search_first_digit = customer_feedback.find(start_word_my_id)
end_search_first_digit = start_search_first_digit + len(start_word_my_id)

start_search_last_digit = customer_feedback.find(end_word_my_id)
end_search_last_digit = start_search_last_digit + len(end_word_my_id)


my_list = [(start_search_first_digit, end_search_first_digit), (start_search_last_digit, end_search_last_digit)]
print(my_list)
# NOTE: response [(129, 136), (82, 87)]

# # Find the positions of 'improved'
# improved_start = customer_feedback.find("improved")
# improved_end = improved_start + len("improved")

# # Store positions in a list of tuples
# positions = [(good_start, good_end), (improved_start, improved_end)]
# print(positions)
# %%
# Write your search code here and provide comments. 

# Initialize an empty list to store (start, end) positions
# my_list = []

##########################################################################################################################################################
# %%
# Question 2 - Functions
# Scenario - You are working in an e-commerce firm as a business analyst, and your manager has tasked you to generate weekly reports on financial metrics like 
# Operating Profit Margin, Revenue per Customer, Customer Churn Rate, and Average Order Value. Use Python functions 
# that will take the values and return the metric needed. Use the first two and last two digits of your ID number as the input values.

# Insert first two digits of ID number here:
start_digit = 75

# Insert last two digits of ID number here:
end_digit = 49

# Write your code for Operating Profit Margin
def get_operating_profit_margin(operating_profit, total_revenue):
    op_profit_margin = (operating_profit/total_revenue) * 100

    # round up to two values
    return round(op_profit_margin, 2)


# Write your code for Revenue per Customer
def get_revenue_per_customer(total_revenue, total_customers):
    # To make this more realistic, I'm going to scale the total revenue by 1000
    scaled_revenue = total_revenue * 1000

    revenue_customer = scaled_revenue/total_customers

    return round(revenue_customer, 2)

# Write your code for Customer Churn Rate
def get_customer_churn_rate(total_customers, lost_customers):
    churn_rate = (lost_customers/total_customers) * 100

    return round(churn_rate, 2)


# Write your code for Average Order Value
def get_average_order_value(total_revenue, total_orders):
    aov = total_revenue/total_orders
    return aov

# Call your designed functions here
print(get_operating_profit_margin(end_digit, start_digit), '%')
# NOTE: operating profit margin is 65.33%


print('$', get_revenue_per_customer(start_digit, end_digit))
# NOTE: for units sold at $49 per customer, the revenue per customer is $1530.61

print('Churn rate', get_customer_churn_rate(start_digit, end_digit))
# NOTE: a churn rate of 65% in this period should be investigated for business performance, as this may affect revenues

print('Average order value', get_average_order_value(end_digit, start_digit))
# NOTE: average order value 0.65

# ############################################################################
# %%
# Question 3 - Regression
# A retail store has collected data on seasonal sales and price changes. The table below shows different price levels and their corresponding demand.
# Develop a linear regression model and determine:
# 1. The price at which the store can maximize revenue
# 2. The demand when the price is set at £52

"""
Price (£)    Demand (Units)
---------------------------
20           300
25           280
30           260
35           240
40           210
45           190
50           160
55           140
60           120
65           100
70           85
"""

# Write your code here
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.DataFrame(
    {
        'prices': [20, 25, 30, 35, 40, 45, 50,55,60,65,70],
        'demand': [300, 280, 260, 240, 210, 190, 160, 140, 120, 100, 87]
    }
)

# introduce a sales column
df['revenue'] = df['prices'] * df['demand']

# price at maximum revenue
max_revenue = max(df['revenue'])

# get the price at the maximum revenue
print(df[df['revenue']==max_revenue]['prices'])

# NOTE: the price at which the retail store can maximise revenue is £45

model = LinearRegression()
model.fit(df[['prices']], df[['demand']])

predicted_demand = model.predict(np.array([[52]]))

print('At £52 the predicted demand is', predicted_demand)
# NOTE: At £52 the predicted demand is 158.48 units
##########################################################################################################################################################
# %%
# Question 4 - Debugging; Plotting and data visualization chart

import random
import matplotlib.pyplot as plt

# Generate 100 random numbers between 1 and student id number
# NOTE: The initial value of max-value defined here had an error, as Python variables cannot be named using '-'. 
# The first step here was to correct it to max_value.
# I also declared the max value
# max-value = integer(input("Enter your Student ID: "))

max_value = 750000049
random_numbers = [random.randint(1, max_value) for i in range(0,100)]

# confirm that indeed 100 random numbers were generated
assert len(random_numbers) == 100

# Plotting the numbers in a line chart
# plt.plot(random_numbers, marker='O', markercolor='green', markeredgcolor='red', linestyle='--', lable='Random Numbers', color='blue');
# NOTE: The initial command has a number of errors, which I corrected as follows
# 1. The marker was set to 'O', which caused a ValueError as it isn't recognised as a marker style. I changed this to 'o'
# 2. There were unrecognised inputs markercolor, which caused an AttributeError. I retained the correct one `color`
# 3. Finally, there was a typing error for `lable`, which caused an AttributeError as this was an unexpected keyword. I corrected to label
plt.plot(random_numbers, marker='o', linestyle='--', label='Random Numbers', color='blue')
plt.title('Line Chart of 100 Random Numbers')
plt.xlabel="Index"
plt.ylabel="Random Number"
plt.legend('---')
plt.grid(True)
plt.show()
# %%
