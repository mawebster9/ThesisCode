# ThesisCode
This project will build off of the work of Sarah Miller and will delve into the Adjudicative Guidelines and the security clearance appeals cases. This particular body of work will try to take case input data and try to determine if the case should be denied or granted a security clearance.

There are 13 adjudicative guidelines:
* A: Allegiance to the U.S.
* B: Foreing Influence
* C: Foreing Preference
* D: Sexual Behavior
* E: Personal Conduct
* F: Financial Considerations
* G: Alcohol Consumption
* H: Drug Involvement
* I: Psychological Conditions
* J: Criminal Conduct
* K: Handling Protected Information
* L: Outside Activities
* M: Use of Information Technology


### Requirements:
* Jupyter Notebooks
* git bash
* python
* pip
* scikit-learn

------------------------------------------------------------
SOFTWARE INSTALLS
------------------------------------------------------------
Before you begin, you need to install certain packages and applications in order to create machine learning solutions and visuals. The tools that will be used include Jupyter Notebooks for visualizing and interacting with code and displaying results, Scikit-Learn for machine learning functions, matplotlib for creating different graphs and visuals, and pandas to interact with our data. Let's start by installing everything we need.

1. Install Python
	Download the correct Python version (python2 or python3) for your machine. Follow the command prompts on the installer.

	https://www.python.org/downloads/

2. Open up Powershell
	In your search bar in your bottom home ribbon, type "Powershell" and select the "Windows Powershell" application. This will open up a blue window where you can type in basic commands.

3. Find the python folder
	Locate where your newly downloaded python folder is located. You can do this by opening up your file explorer and searching for "python". Once it is found, copy the file path of the newly downloaded python folder. 
	In the powershell command prompt, type 

		cd [insert your file path here - do not include it in brackets]

	and hit enter. The file path will look somewhat similar to this (note: it may have more things in between C:\Users\ and \Python\Python37-32   ***   the numbers at the end of the last part (37-32) is specific to the version of python you downloaded):

		cd C:\Users\jdoe\Programs\Python\Python37-32

	To ensure that python is installed correctly, type 

		python --version

	it will display the version you have installed or an error if you don't have it installed/your file path you provided is incorrect.

4. Install pip
	Pip is a tool that allows you to install all kinds of python packages.
	Navigate to https://bootstrap.pypa.io/get-pip.py and copy the contents to a text file on your local machine (use notepad - paste the contents into here). Save the file as "get-pip.py" and save the file inside of you python folder. Return back to your powershell prompt and type 

		python get-pip.py

	This will install the pip package which includes some other important files. To ensure it installed correctly, type "pip --version". Update the pip package by typing "python -m pip install -U pip".

5. Install common ML packages
	In the powershell prompt type the following commands, ensuring that they successfully install before you type the next command:
		
		pip install numpy
		pip install scipy
		pip install matplotlib
		pip install statsmodels
		pip install pandas
		pip install jupyter

6. Install Git Bash
	In your internet browser, navigate to https://gitforwindows.org/ to download git bash for windows.



------------------------------------------------------------
CLONING THE GITHUB REPOSITORY
------------------------------------------------------------
Now that you have everything installed, it's time to clone the github repository. Add a new folder to your desired location and give it a descriptive name. Go into your newly created folder and copy the file path. Now open up git bash and type 

	git clone https://github.com/mawebster9/ThesisCode

and hit enter. This will pull a copy of the repository onto your machine. It is recommended to copy the repo into your python folder.



------------------------------------------------------------
RUNNING JUPYTER NOTEBOOKS
------------------------------------------------------------
Now that you have everything installed, it's time to run the Jupyter Notebooks application. The most important part of this step is to not exit/close out of the powershell window - this will stop the notebook. You can minimize this window but do not close it. As you make changes to the notebook in your browser window, code will be populated in the powershell window but you can ignore this for now.

In the powershell command prompt, type 

	jupyter notebooks

You will see output that resembles this:

	[I 10:52:50.055 NotebookApp] The Jupyter Notebook is running at:
	[I 10:52:50.057 NotebookApp] http://localhost:8888/?token=a59f01953665fe6bb67a64e21ff20d395a8be1ab582813ea
	[I 10:52:50.057 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
	[C 10:52:50.169 NotebookApp]

This command may automatically open your browser - if it does not, open up a browser and in the website bar type "http://localhose:8888" and hit enter. It will either open directly to the files available to you but if it does not, copy the remaining line after the "token=" and paste it into the token box on the webpage and hit enter.

Now you have an instance of Jupyter Notebooks on your computer!

To start a new Notebook, select the "New" option at the top and under the "Notebook:" option, select "Python 3". This will open up a new notebook for you. If you wish to access already existing Notebooks, simply click on the notebook you wish to open.


