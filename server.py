import pickle
import datetime
import os
import time

def load_user_db():
    """Loads user_db.txt file with user information."""
    if not os.path.exists("user_db.txt"):
        return {}  # if file does not exist, return empty dictionary

    try:
        with open("user_db.txt", "rb") as infile:
            return pickle.load(infile)
    except EOFError:
        return {}  # if file empty, return empty dictionary


def save_user_db(user_db):
    """Write new user information to user_db.txt file."""
    with open("user_db.txt", "wb") as outfile:
        pickle.dump(user_db, outfile)

def read_username():
    """Read username from user_login.txt file received from main program."""
    if not os.path.exists("user_login.txt"):
        return None  # no login attempt detected

    with open("user_login.txt", "r") as infile:
        username = infile.read().strip()
        infile.close()

    # remove login file
    os.remove("user_login.txt")

    if username:
        return username
    else:
        return None

def update_streak(username):
    """Calculates the user's current login streak."""
    user_db = load_user_db()
    today = datetime.date.today().strftime("%Y-%m-%d")

    if username in user_db:
        last_login = user_db[username]["last_login"]
        streak = user_db[username]["streak"]

        #check how long it's been since last login
        last_login_date = datetime.datetime.strptime(last_login, "%Y-%m-%d").date()
        todays_date = datetime.datetime.strptime(today, "%Y-%m-%d").date()
        days_difference = (todays_date - last_login_date).days

        if days_difference == 1:
            streak += 1  # increase streak if logins 1 day apart
        elif days_difference > 1:
            streak = 1  # reset streak if logins more than 1 day apart
    else:
        # initialize streak to 1 if new user
        streak = 1

    # update db
    user_db[username] = {"last_login": today, "streak": streak}
    save_user_db(user_db)

    return streak

def write_response(streak):
    """Writes streak to response file."""
    with open("response.txt", "w") as infile:
        if streak > 1:
            infile.write(f"Your current login streak is: {streak} days!")
            infile.close()
        elif streak == 1:
            infile.write(f"Your current login streak is: {streak} day!")
            infile.close()

if __name__ == "__main__":
    print("Server is running. Waiting for login attempts...")

    while True:
        username = read_username()
        if username:
            print(f"Processing login for: {username}")
            streak = update_streak(username)
            write_response(streak)
            print("Streak updated successfully!")

        time.sleep(1)
