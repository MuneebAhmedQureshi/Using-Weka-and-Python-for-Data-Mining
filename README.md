# Using Weka and Python for Data Mining
# Integration of Python and Python-weka-wrapper
Sample Code with explanation for generation and graphical representation of <br>
<ul>
  <li>Confusion Matrix of ZeroR</li>
  <li>Classifier Errors of Linear Regression</li>
  <li>ROC Curve of Naive Bayes</li>
</ul>
<br>is given in: <br><br>
<ul>
  <li>weka-from-moocs.py</li>
  <li>weka-from-moocs-graphs.py</li>
  <li>weka-from-moocs-curves.py</li>
</ul>

# Installing Python IDE

Follow this link, go to the end of page and download Python for 32 or 64 bit as per your Windows Version<br>
<a>https://www.python.org/downloads/release/python-364/</a><br>
Click on downloaded .exe file to install<br><br>

# Setting Environment Variable for Python

Environment Variables are set so that when we import libraries in our scripts; operating system knows where to locate those libraries.<br><br>
Right Click on My PC<br><br>
Select Properties<br><br>
Click on Advanced System Settings<br><br>
Click on Environment Variables<br><br>
Under System Variables click New<br><br>
Set variable name to PYTHON_HOME<br><br>
Locate python form C:\Users\hp\AppData\Local\Programs\Python\Python36\ replace "hp" with your username<br><br>
Set variable value to the <b>full path of Python36 folder</b><br><br>
Now locate: variable named "path" under system variables<br><br>
Click "Edit" and at the end of Variable Value add ";%PYTHON_HOME%/"<br><br>
Make sure you added semi-colon before PYTHON_HOME<br><br>
Click OK and OK and OK<br><br>
Now you can check if environment variable is set by running this command in CMD <b>echo %PYTHON_HOME% </b><br><br>
Now run: python --version to validate new environment settings.

# Required Packages

To invoke Weka from Python these packages are required<br>
<ul>
  <li>Pip</li>
  <li>Numpy (comes preinstalled)</li>
  <li>Imaging</li>
  <li>Matplotlib</li>
  <li>Pygraphviz</li>
  <li>Javabridge</li>
  <li>Python Weka Wrapper</li>
</ul><br>

# Installing Required PIP Setup Tools for Python

Press <b>WINDOW+R</b> write <b>cmd</b> and press <b>Enter</b> <br><br>
Run <b>python --verison</b> to check if python is properly installed<br><br>
Now,<br><br>
Run <b>python -m pip install --upgrade pip setuptools wheel</b><br><br>
PIP setup tools will be updated.

# Installing Imaging
Run <b>python -m pip install pillow</b><br><br>

# Installing Matplotlib
Run <b>python -m pip install matplotlib</b><br><br>

# Installing Pygraphviz
Errors not resolved yet

# Installing Javabridge

Run <b>python -m pip install javabridge</b><br><br>
If it returns error:<br><br>
<ul>
<li>Microsoft Visual C++ Version 14.0.0 is required.</li><br>
<b>-->></b>Open control panel click <b>Uninsall A Program</b> and uninstall all instances of Visual Studio and Microsoft Visual C++ you can find. Then, follow <a href="https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community&rel=15#" style="margin: 0px !important">this</a> link it will download the required version of Microsoft Visual C++<br><br>
<li>Could not find a version that satisfies the requirement <package name> (from versions: ) No matching distribution found for <package name> You are using pip version <n>, however version <n++> is available. You should consider upgrading via the 'python -m pip install --upgrade pip' command</li>
<br><b>-->></b>Run and keep running this command <b>python -m pip install --upgrade pip</b> in Anaconda Prompt until this error is resolved. Pip is sometime upgraded in a few steps.<br><br>
</ul>
Now try installing javabridge again, hopefully it will be installed.<br><br>

# Installing Python Weka Wrapper

For Python Versions 2.* and below<br><br>
Run <b>python -m pip install python-weka-wrapper</b><br><br>
For Python Versions 3.* and above (e.g we are using Python Version 3.6.4)<br><br>
Run <b>python -m pip install python-weka-wrapper3</b><br><br>
Weka Library is now successfully installed<br><br>

# Downloading and Running Provided Scripts

Click the green colored <b>Clone or download</b> button on top right corner of this page<br><br>
Click <b>Download Zip</b><br><br>
Extract the downloaded .zip file<br><br>
Navigate to the extracted folder<br><br>
Press Shift and Right Click simultaneously<br><br>
Select <b>Open command window here</b><br><br>
Write <b>python weka-from-moocs-curves.py</b> and press enter<br><br>
Wait till it loads the libraries: It will output the ROC curve in a new window<br><br>
Similarly, you can run and check output of other files by writing <b>python filename.py</b>

# Provided Helping Material 

As explained in WekaMOOCS Official channel's demonstaration<br><br>
https://www.youtube.com/watch?v=YT72KkkfD3w<br><br>
Python codes used in this video are provided.<br><br>
Datasets used in this video are also provided.<br><br>

# Copyright Statement

These scripts are just for learning purposes. Kindly don't copy and paste same code and files in your assignment as you won't be the only genius.
