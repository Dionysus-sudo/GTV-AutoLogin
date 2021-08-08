
# GTV Auto-Login

This project is focused on the task of Automating Game.tv app(user login), testing various steps and test cases involved in the process.

I've used the Appium webdriver for automating the user login flow, involving identifying the login/home/landing, etc pages within the app.
These steps have been constituted as test cases and pytest(with html plugin) has been used to generate the final consolidated test report.






## Project Structure

This project contains a file with all the test cases and another file containing the automation script to login into the game.tv app.

  
## Install Depedencies

Targeted app: https://play.google.com/store/apps/details?id=tv.game

requirements.txt https://github.com/Dionysus-sudo/GTV-AutoLogin/edit/main/README.md

Install Appium using the below command

```bash
  pip install Appium-Python-Client
```

Install pytest(w/html plugin) using the below command

```bash
  pip install pytest
  pip install pytest-html
```



## Running Tests

To run tests, run the following command

```bash
  pytest mod_appium.py -s --html test_results.html --capture=tee-sys
```
The above command can be run directly from the terminal and targets all the test cases.
--html and -s argument is being given to generate the html results to file 'test_results.html' and stdout the logs respectively.




  
## Screenshots

[![test-results.png](https://i.postimg.cc/C13Cdhp7/test-results.png)](https://postimg.cc/JDQH2WnH)

  
