# CS361 Microservice A: Daily Login Tracker
# HOW TO REQUEST DATA
At the time of user login, the main program will send the user information to the microservice by writing to a text file. The microservice then reads the text file and uses it to process the user information. If the user is loggin in for the first time, the microservice saves the username, date of last login, and streak (defaulted to 1 day) to a user database file. If the user has logged in previously, the microservices finds the user's information in the user database file and updates the current streak.<br>
Example call:
```
# user enters "admin" as username
# call write_username("admin")
def write_username(username):
  with open("user_login.txt", "w") as outfile:
    outfile.write(username)
    outfile.close()
```

# HOW TO RECEIVE DATA
The main program will RECEIVE data from the microservice using text files. After the microservice has processed the user information and determined the streak, it sends a response back to the main program via a text file containing the current streak.<br>
Example call:
```
def read_response():
  """Reads the login streak response from user_login.txt."""
  while not os.path.exists("response.txt"):  # Wait for server.py to write response
      time.sleep(1)

  with open("response.txt", "r") as infile:
      response = infile.read().strip()
  return response
```

# UML DIAGRAM
![alt text](https://i.imgur.com/AbXunGQ.png)
