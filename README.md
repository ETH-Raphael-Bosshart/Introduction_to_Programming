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
* tabulate

In addition, you need an IDE working with Python. Please install the Anaconda Navigator to make sure the code runs correctly together with the jupyter notebook environment. You can download the Anaconda Navigator directly from the link below. 
```
https://www.anaconda.com/products/distribution
```
Jupyter Notebook comes pre-installed in Anaconda, meaning that you do not have to install it explicitly. All you need to install is Anaconda and Jupyter Notebook would already be displayed in the Navigator. If this is not the case, please go to Help!

If you're new to Python, it is most likely that some of the used libraries are not yet installed on your device. 
To make sure that you can later run the code successfully, please install the libraries by entering the commands below in your terminal seperately. If you are not new to Python, you can jump the installations and install only the missing libraries at a later term.
```
  pip install pandas
```
```
  pip install matplotlib
```
```
  pip install numpy
```
```
  pip install tabulate
```

Prior running the code, you have to download your user data from the Netflix website: <br /> If you want to use the sample files instead, go to the chapter "Executing the program with the sample files"
```
https://www.netflix.com/account/getmyinfo
```
After clicking on the link, you'll see a button: "Submit Request". After that, you are going to receive a link to verify the request. Some time later you are able to download the data directly from link above. Make sure you do this prior running the code and to save the file on your desktop! <br /> For the sake of time we added two example csv files you can use instead. If you want to use those files, please save a copy of them in a new file on your desktop.

### Executing the program with your data
In this example here, we'll work with Anaconda Navigator together with jupyter notebook.
To run the code successfully, follow the step-by-step instructions:
* Create a new folder on your desktop
* Save a copy of your "ViewingActivity.csv" and "BillingHistory.csv" in it
     * "ViewingActivity.csv" can be found in the folder "CONTENT_INTERACTION"
     * "BillingHistory.csv" can be found in the folder "PAYMENT_AND_BILLING"
* Open the Anaconda Navigator
* Launch jupyter Notebook
* Open the "Desktop" folder
* Open your just created folder
* Click on: "New"
* Click on: "Python 3 Notebook"
* Copy our code (Netflix.py) and paste it in your just created Notebook
* Click on: "Run"

Important: You have to save the Notebook directly in the same folder like both files ("ViewingActivity.csv" and "BillingHistory"). If for any reason Anaconda cannot find the file, check out the chapter "Help".  

### Executing the program with the sample files
In this example here, we'll also work with Anaconda Navigator together with jupyter notebook.
To run the code successfully, follow the step-by-step instructions:
* Create a new folder on your desktop
* Open the two sample files above ("ViewingActivity.csv" and "BillingHistory.csv") and save them in your just created folder by:
     * On Windows:
        * Click on each "Raw" button
        * Right click on the just opened page
        * Click on: "Save as"
        * Save it in your just created folder
     * On Mac:
        * Right click on the "Raw" button
        * Click on: "Download Linked File As..."
        * Save it in your just created folder
* Open the Anaconda Navigator
* Launch jupyter Notebook
* Open the "Desktop" folder
* Open your just created folder
* Click on: "New"
* Click on: "Python 3 Notebook"
* Copy our code (Netflix.py) and paste it in your just created Notebook
* Click on: "Run"

Important: You have to save the project directly in the same folder like both files ("ViewingActivity.csv" and "BillingHistory"). If for any reason your IDE cannot find the file, check out the chapter "Help".  

### Help

If the IDE should not be able to find the csv files, update the path of the files in the lines:

```
activity = pd.read_csv("ViewingActivity.csv")
```
```
billing = pd.read_csv("BillingHistory.csv")
```
#### On Windows 11:
* Right clicking on each of them ("ViewingActivity.csv" and "BillingHistory.csv")
* Click: “Copy as path”
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
billing = pd.read_csv("./Desktop/netflix-report/PAYMENT_AND_BILLING/BillingHistory.csv")
```
If Jupyter Notebook is not installed in your Anaconda Naviagator, you can download it directly by entering the command below in your terminal:
```
pip install notebook
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

