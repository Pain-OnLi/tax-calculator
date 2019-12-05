# tax-calculator
Simple application to calculate tax based upon a few input parameters

### How to run
- Follow the instructions on how to download python here https://www.python.org/downloads/ - version 3.5 or greater
- The installation of python 3.5 or greater should give you the pip command to be used in the testing stage 
- If you cannot run the "python" command in command line, follow these instructions on how to add the required python environment variables to run the "python" command https://geek-university.com/python/add-python-to-the-windows-path/ for windows and https://www.tutorialspoint.com/python/python_environment.htm for linux based systems.
- In the command line, change the directory to the "src" directory and run "python Execution.py."

### How to run tests

- Assuming you have gotten the above command line commands to work, run this command "pip install -U pytest" to install pytest.
- Check that pytest is installed by running pytest --version. You should get a response that does not correspond to some kind of error.
- Using the command line, change the directory to the "tests" directory.
- You can directly run a "pytest" command in this directory to see the tests pass.
- For a more detailed overview of what tests were ran, run "pip install pytest-html" in the command line. Once this commmand is finished, run "pytest --html=report.html."
- You should receive a file called report.html that you can view in your browser that details the tests that were ran.