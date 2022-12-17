# Netflix User Data Analyser
## Skills: Programming - Introduction Level HSG

Have you ever thought about how much time you spent on Netflix or how many movies and series you watched until now? 

That's exactly the purpose of this little project! The user is able to visualize the amount of time used and moreover also on which devices! As a little extra, the code also shows a graph of the amount of money spent.

### Description

An in-depth description of our code can be directly found in the code itself as comments.

## Getting Started

### Dependencies
The following libraries are used in our code and therefore needed before running it:
* pandas
* matplotlib
* numpy

In addition, you need an IDE working with Python. Please install Anaconda Navigator to make sure the code runs correctly together with the jupyter notebook environment. You can download the Anaconda Navigator directly from the link below. 
```
https://www.anaconda.com/products/distribution
```

If you're new to Python, it is most likely that some of the used libraries are not yet installed on your device. 
To make sure that you can run the code successfully, please install these libraries. Therefore run the following commands in your terminal separately:
```
  pip install pandas
```
```
  pip install matplotlib
```
```
  pip install numpy
```
Prior running the code, you also have to download your user data from the Netflix website:
```
https://www.netflix.com/account/getmyinfo
```
After clicking on the link, you'll see a button: "Submit Request". After clicking on it, you are going to receive a link to verify the request. Some time later you are able to download the data directly from link above. Make sure you do this prior running the code and to save the file on your desktop!

### Executing the program
In this example here, we'll work with Anaconda Navigator together with jupyter notebook.
To run the code successfully, follow the step-by-step instructions:
* Open the Anaconda Navigator
* Launch jupyter Notebook
* Open the "Desktop" folder
* Open "netflix-report"
* Open "CONTENT_INTERACTION"
* Click on: "New"
* Click on: "Python 3 Notebook"
* Copy our code (Netflix.py) and paste it in your just created Notebook
* Click on: "Run"

Important: You have to save the project directly in the same folder like both files ("ViewingActivity.csv" and "BillingHistory"). There is also the option to make a new folder on your device and save your Notebook/project and a copy of both files in it. If for any reason your IDE cannot find the file, check out the chapter "Help".  

### Help

If the IDE should not be able to find the csv files, update the path of the files in the lines:

```
activity = pd.read_csv("ViewingActivity.csv")
```
```
billing = pd.read_csv("BillingHistory.csv")
```
#### On Windows 11:
* Right clicking on each of them ("ViewingActivity.csv" and "BillingHistory")
* Click “Copy as path”
* Replace the expression in the brackets with the copied file path

#### On Mac:
* Navigate to Finder > Go > Utilities
* Launch the Terminal app
* Drag both files separately in the terminal
* Copy the file path
* Replace the expression in the brackets with the copied file path

In the end it should look similar to: 
```
activity = pd.read_csv("./Desktop/netflix-report/CONTENT_INTERACTION/ViewingActivity.csv")
```
```
billing = pd.read_csv("./Desktop/netflix-report/CONTENT_INTERACTION/BillingHistory.csv")
```
## Inspiration
This code is inspired by Dataquest: "Beginner Python Tutorial: Analyze Your Personal Netflix Data" 

```
https://www.dataquest.io/blog/python-tutorial-analyze-personal-netflix-data/
```
## Authors

#### Raphael Philipp Bosshart 
* Bachelor Student
* University of St.Gallen 

#### Joanna Maria Rogg 
* Bachelor Student
* University of St.Gallen

