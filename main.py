import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

df = pd.read_csv(r"C:\Users\mzahm\OneDrive\Desktop\Study\Python\all_stocks_5yr.csv")

# #print(df.head())

missing_data = df.isnull().sum()
# print(missing_data)  # to see total number of rows containing null values under each column
# print("\nDisplayed above are the total number of missing data points in each column.\n")

df = df.dropna(axis=0)  # to drop rows with null values
# print(df.isnull().sum())  # to make sure rows with null values have been dropped
# print("\nDisplayed above,after removing rows with null values, there should now be no missing data points.\n")

stocks = df['Name'].unique()
print(stocks)  # to see every unique ticker (defined as 'Name' in the dataset) within the S&P500
print(f"\nThere are {len(stocks)} different stocks in this dataset. They have been displayed above.\n")

valid_stock_choice = False  # initializing conditions to accept valid user input for stock ticker and label
valid_label_choice = False

while valid_stock_choice is False:  # accepting valid stock input from user
    stock_choice = input("From the list above, which stock would you like to examine further?\t")
    if stock_choice in stocks:
        chosen_stock_data = df[df['Name'] == stock_choice]  # isolating data for user selected stock
        valid_stock_choice = True
        pass
    else:
        print(f"\n{stock_choice} is not a valid selection. Please try again.")

labels = list(df)[1:6]

while valid_label_choice is False:  # accepting valid label input from user
    label_choice = input(f"For {stock_choice}, which value would you like to examine further? "
                         f"Please enter 'open', 'high', 'low', 'close' or 'volume'.\t")
    if label_choice in labels:
        valid_label_choice = True
        pass
    else:
        print(f"\n{label_choice} is not a valid selection. Please try again.")

x = [dt.datetime.strptime(i, '%Y-%m-%d') for i in chosen_stock_data['date']]
y = chosen_stock_data[label_choice]

plt.plot(x, y)
plt.title(stock_choice + " daily " + label_choice + " data")
plt.xlabel('date')
plt.ylabel(label_choice)
plt.ylim(0)
plt.grid()

plt.savefig(stock_choice + "_" + label_choice + ".jpg")

print(f"\nYour plot for the daily {label_choice} of {stock_choice} has "
      f"been generated as {stock_choice}_{label_choice}.jpg")
