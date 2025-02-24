import time
import os

def write_username(username):
    """Writes the username to a .txt file for server.py to read."""
    with open("user_login.txt", "w") as outfile:
        outfile.write(username)
        outfile.close()


def read_response():
    """Reads the login streak response from response.txt."""
    while not os.path.exists("response.txt"):  # Wait for server.py to write response
        time.sleep(1)

    with open("response.txt", "r") as infile:
        response = infile.read().strip()
    return response


if __name__ == "__main__":
    username = input("Enter your username: ").strip()
    time.sleep(1)

    # write username to user_login.txt
    write_username(username)
    print("Username written. Waiting for server response...")
    time.sleep(5)

    # read response from response.txt
    response = read_response()
    print(response)
