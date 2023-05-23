# ReactTestProject
## API

### Getting Started
1. To get started you will need to install the most current and stable version of Python(3.11.2).
2. Confirm you have installed correctly by running the command "python -V" in git bash which should return "Python 3.11.2".
3. Create a virtual environment to install your necessary packages using your git bash terminal:
    1. Make sure you are creating a virtual environment at an easy access point for example your C drive on Windows you can get to this level by using the command "cd /c".
    2. Once you're in the correct directory, run the command "python venv =m {Insert your environment name here i.e: reactAPI}"
4. Now that the directory is created you can activate your virtual environment with the command "source {virtual environment name}/Scripts/activate" you should see your virtual environment name encased in parenthesis above each command line. For example: (reactAPI)
5. Now that the virtual environment is activated you need to install the necessary packages:
    1. For windows:
        1. Go back to the project directory for the API and run the command "pip install -r requirements.txt"
    2. For Mac/Linux run the folllowing commands:
        1. pip install numpy
        2. pip install pandas
        3. pip install Flask
        4. pip install flask-restful
6. To run the code type python main.py within the API's project folder, setup is now complete.
