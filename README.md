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

Follow this link and download Python<br>
<a>https://www.python.org/ftp/python/3.6.4/python-3.6.4-amd64.exe/</a><br>
Click on downloaded .exe file to install<br><br>

# Setting Eenvironment Variable for Python

Environment Variables are set so that when we import libraries in our scripts; operating systems knows where to locate those libraries.
Right Click on My PC<br><br>
Select Properties<br><br>
Click on Advanced System Settings<br><br>
Click on Environment Variables<br><br>
Under System Variables click New<br><br>
Set variable name to PYTHON_HOME<br><br>
Locate python form C:\Users\hp\AppData\Local\Programs\Python\Python36\ replace "hp" with your username
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
  <li>Numpy</li>
  <li>Imaging (Optional)</li>
  <li>Matplotlib</li>
  <li>Pygraphviz(Optional)</li>
  <li>Javabridge</li>
  <li>Python Weka Wrapper</li>
</ul><br>
These packages come preinstalled in Python<br>
<ul>
  <li>Pip</li>
  <li>Numpy</li>
  <li>Matplotlib</li>
</ul><br>
These packages are to be installed by user<br>
<ul>
  <li>Javabridge</li>
  <li>Python-weka-wrapper</li>
</ul><br>

# Installing Required Setup Tools for Python

Press <b>Ctrl+R</b> write <b>cmd</b> and press <b>Enter</b> <br><br>
Run <b>python -m pip install --upgrade pip setuptools wheel</b><br><br>
PIP setup tools will be updated.

# Installing Javabridge on Windows

Press <b>Ctrl+R</b> write <b>cmd</b> and press <b>Enter</b> <br><br>
Run <b>python --verison</b> to check if python is properly installed<br><br>
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

For Python-2<br><br>
Run: python -m pip install python-weka-wrapper<br><br>
For this version of Python which we are using: Python-3.6.4<br><br>
Run: python -m pip install python-weka-wrapper3<br><br>
Weka Library and Python are now successfully installed<br><br>

# Setting Environment Variable MOOC_DATA on Windows 7

It is set just for understanding purpose, you can access files directly also.
Right Click on My PC<br><br>
Select Properties<br><br>
Click on Advanced System Settings<br><br>
Click on Environment Variables<br><br>
Under System Variables click New<br><br>
Set variable name to MOOC_DATA or whatever you want to use in your program<br><br>
Set variable value to the <b>full path of folder where you have stored weka datasets</b> e.g C:\Users\hp\Documents\WekaDatasets\ <br><br>
Click OK and OK and OK<br><br>
Now you can check if environment variable is set by running this command in CMD <b>echo %MOOC_DATA% </b><br><br>
<b>Everything is set and ready to be executed</b>

# Provided Helping Material 

As explained in WekaMOOCS Official channel's demonstaration<br><br>
https://www.youtube.com/watch?v=YT72KkkfD3w<br><br>
Jupyter Notebook Files of all codes used in this video are provided.<br><br>
Datasets used in this video are also provided.<br><br>

