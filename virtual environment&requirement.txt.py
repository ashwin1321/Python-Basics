# To create a virtual seperate environment for python
# to know more go to https://www.geeksforgeeks.org/python-virtual-environment/
# To setup you can check https://www.youtube.com/watch?v=Lah7WGW6exg&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME&index=44

# --> Download virtualenv goto( -> cmd -> pip install virtualenv )
# --> to create virtual environment (cmd --> virtualenv foldername)

# A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them. 
# Imagine a scenario where you are working on two web based python projects and one of them uses a Django 1.9 and the other uses Django 1.10 and so on. In such situations virtual environment can be really useful to maintain dependencies of both the projects.
# To solve this problem, we just need to create two separate virtual environments for both the projects.
# Virtual Environment should be used whenever you work on any Python based project. It is generally good to have one new virtual environment for every Python based project you work on. So the dependencies of every project are isolated from the system and each other.



# For requriement.txt
# --> go to folder and open powershell (shift+right click) and type (pip freeze > requirement.txt)