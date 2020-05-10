# UI testing web framework example
# H&M UI testing
I have taken one e-commerce project [H&M online shop](https://www2.hm.com/en_gb/index.html "H&M Online") to test it with Python.

## Tech Stack used
• Python 3.7 - coding  
• PyTest - runner  
• Allure - test outcome reporter  
• Webdriver-Manager - selenium driver updater  
• Python Logging - logger (logging facility for Python)  

## Getting Started
Software to be pre-installed :  
• Python 3.5 or higher - version https://www.python.org/downloads/
```bash
note that python should be set to environment variables
```

## Installation
Use the package manager to install all the packages.

```python
pip freeze > requirements.txt
```

## Running autotests from command line or terminal

```python
python -m pytest [...]
```

## Framework Structure
• Programming language – Python 3.7  
• Test runner – Pytest 5.4.1  
• Page Object – Separate class for every web-page, that hold all functionality and members of that web-page using PageFactory pattern  
• Test base class: Deals with all the common functions used by all the pages, responsible for test launch, for reports,pre-cond post-cond, web-driver init, loading configs etc.  
• Packages: I have separate packages for Pages, Test steps and any other framework layer  
• Utility Functions: The code which is repetitive in nature such as waits, scroll actions, property loader, logging etc.  
• VCS: Git  

## Test Layers
• Pages(web-pages and elements)  
• Test steps(logic implementation)  
• Test launch(runners)  
• Test data(feature files)  

## Tests support cross-platform browser testing
○ Windows:  
 • Chrome  
 • FireFox  
○ MacOS:  
 • Chrome  
 • FireFox  
 
P.S. Didn't have a chance to configure and test Safari browser, however Chrome and Firefox are supported on both platforms

## Results Reporting
Will be added later

## Code Design
Project follows [Google Python](https://google.github.io/styleguide/pyguide.html) code style guide

For more detailed information about code design, please refer to in-code documentation


## License
[MIT](https://choosealicense.com/licenses/mit/)
