# Import necessary libraries
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Read in the data from a CSV file containing Netflix activity
try:
    activity = pd.read_csv("ViewingActivity.csv")
except FileNotFoundError:
    print("File not found.")
except pd.errors.EmptyDataError:
    print("No data")
# Read in the data from a CSV file containing Netflix billing history
try:
    billing = pd.read_csv("BillingHistory.csv")
except FileNotFoundError:
    print("File not found.")
except pd.errors.EmptyDataError:
    print("No data")

# Format the times so we can calculate and plot them
activity['Start Time'] = pd.to_datetime(activity['Start Time'], utc=True)
activity['Duration'] = pd.to_timedelta(activity['Duration'])

# function for displaying used devices
def usage_devices(file):
    # changes the size of the font
    matplotlib.rcParams.update({'font.size': 7})
    # set outer background color
    plt.figure(facecolor='whitesmoke')
    # Setting the background color of the plot
    # using set_facecolor() method
    backgroundcolor = plt.axes()
    backgroundcolor.set_facecolor("lightgrey")
    # counts how many times a device appears in the column and plots it as a horizontal bar
    file['Device Type'].value_counts().plot(kind='barh', color = 'firebrick')
    # names the x and y label of the bar
    plt.xlabel("Total amount used")
    plt.ylabel("Device")
    # sets a titel to the bar
    plt.title("Devices used", fontweight='bold')
    # shows the bar to the user
    plt.show()

# stores the number of row occurrences for each Profile and therefore the amount of activities
def amount_of_activities(file):
    # changes the size of the font
    matplotlib.rcParams.update({'font.size': 8})
    # set outer background color
    plt.figure(facecolor='whitesmoke')
    # Setting the background color of the plot
    # using set_facecolor() method
    backgroundcolor = plt.axes()
    backgroundcolor.set_facecolor("lightgrey")
    # counts how many times a profile name appears in the column and plots it as a bar    
    file['Profile Name'].value_counts().plot(kind='bar', color = 'firebrick')
    # names the x and y label of the bar
    plt.xlabel("User")
    plt.ylabel("Total amount watched")
    # sets a titel to the bar
    plt.title("Total Activities", fontweight='bold')
    # shows the bar to the user
    plt.show()

# stores the total time watched in total_watched and prints it
def total_time_watched(file):
    # changes the size of the font
    matplotlib.rcParams.update({'font.size': 10})
    # set outer background color
    plt.figure(facecolor='whitesmoke')
    # Setting the background color of the plot
    # using set_facecolor() method
    backgroundcolor = plt.axes()
    backgroundcolor.set_facecolor("lightgrey")
    # Finds the unique elements of the column "Profile Name" and stores it as an
    # array in users
    users = np.array(activity["Profile Name"].unique())
    # Creates a data structure called dictionary
    duration_array = {} 
    # iterates through all users, sums up their durations and stores it in the dictionary
    for i in users:
        duration_array.update({i: file.loc[activity['Profile Name'] == i,'Duration'].astype('timedelta64[s]').sum()})
    # convert seconds into hours
    for i in duration_array:
        duration_array[i] = duration_array[i] / 3600
    # names the x and y label of the bar
    plt.xlabel("User")
    plt.ylabel("Time spent in hours")
    # sets a titel to the bar
    plt.title("Total Time Watched", fontweight='bold')
    # The * in zip(*D.items()), unpacks the duration_array object, and zip, aggregates elements from each of the iterables.
    plt.bar(*zip(*duration_array.items()), color = 'firebrick')
    # shows the bar to the user
    plt.show()

# stores the amount of countries and plots a bar
def country(file):
    # changes the size of the font
    matplotlib.rcParams.update({'font.size': 7.8})
    # set outer background color
    plt.figure(facecolor='whitesmoke')
    backgroundcolor = plt.axes()
    # Setting the background color of the plot
    # using set_facecolor() method
    backgroundcolor.set_facecolor("lightgrey")
    # since the amount of some countries can be way higher than others, we log it
    file['Country'].value_counts().plot(logx=True, kind='barh', color = 'firebrick')
    # names the x and y label of the bar
    plt.xlabel("Total amount of country logarithmized")
    plt.ylabel("Country")
    # sets a titel to the bar
    plt.title("Countries", fontweight='bold')
    # shows the bar to the user
    plt.show()

def billing_history(file):
    # changes the size of the font
    matplotlib.rcParams.update({'font.size': 7})
    # set outer background color
    plt.figure(facecolor='whitesmoke')
    # Setting the background color of the plot
    # using set_facecolor() method
    backgroundcolor = plt.axes()
    backgroundcolor.set_facecolor("lightgrey")
    # plots the cumulative sum as a line graph
    file['Item Price Amt'].cumsum().plot(color = 'firebrick')
    # names the x and y label of the bar
    plt.xlabel("Number of transaction")
    plt.ylabel("Total spent within current transaction")
    # sets a titel to the bar
    plt.title("Billing History", fontweight='bold')
    # shows the bar to the user
    plt.show()

print("Hello! This is a Netflix User Data Analyser!" + " If you want to have one of the informations shown below displayed, insert the related number next to it.")
print("used devices: 1 \n" +
      "amount of activities: 2 \n" +
      "total time watched: 3 \n" +
      "countries in which you used your account: 4 \n" +
      "billing history: 5 \n" +
      "If you don't want to quit the application: 0")

# runs the code below while the user input is not 0
while True:
    try:
        # stores the user input in the variable "user_input"
        user_input = input()
        # runs the functions according to user input
        if(int(user_input) == 0):
            break
        elif(int(user_input) == 1):
            usage_devices(activity)
        elif(int(user_input) == 2):
            amount_of_activities(activity)
        elif(int(user_input) == 3):
            total_time_watched(activity)
        elif(int(user_input) == 4):
            country(activity)
        elif(int(user_input) == 5):
            billing_history(billing)
        # if the user should not enter a defined variable, 
        # the statement below is printed 
        # and the user has to try again
        else:
            print("For this input is no information. Try again with a valid input!")
    except ValueError:
        print("You did not enter a number, please try again with an integer defined above.")
