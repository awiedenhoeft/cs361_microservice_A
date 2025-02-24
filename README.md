# CS361 Microservice A: Daily Login Tracker
A. The main program REQUESTs data from the microservice using .txt files. First, the main program writes the username, as entered by the user, to a .txt file. The microservice then reads the .txt file and either finds the user information in a user database file or, if the user is new, adds the user information to the user database file. The microservice then updates the user's current streak.<br>
Example call:
  
B. The main program will RECEIVE data from the microservice using .txt files. After the microservice has processed the user information and determined the streak, it writes a message stating the user's current streak to a response.txt file. The main program receives its data from this file.<br>
Example call:

C. ![alt text]([http://url/to/img.png](https://i.imgur.com/AbXunGQ.png))
