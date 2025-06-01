from .Faculty import FacultyMember
from .db_queries import *
from .CoursesTaughtData import getCoursesTaught
import hashlib
import time

def registerFaculty():
    """
    Asks the faculty member for their username and password, hashes the password, gets the next available faculty ID, and stores it to the database.
    """
    print('===== REGISTER ACCOUNT =====')
    f = FacultyMember()
    f.register()

    f.setID(getNextID())

    sql = "insert into FacultyMembers values (?, ?, ?)"

    # FAKE IT UNTIL YOU MAKE IT
    facnum = input("Enter your faculty ID number: ")
    print("Waiting for", facnum, "to sign in to VIU faculty database...")
    time.sleep(5)
    print("Faculty member verified!")

    execute_query(sql, f.getID(), f.getUsername(), f.getPassword())
    print("Faculty member registered to database!")


def getNextID() -> int:
    """
    Finds the next facultyID to use in the database.

    The next facultyID will be 1 greater than the maximum ID value already existing within 
    the FacultyMembers table in the database.
    :return: The facultyID to be used for the next student.
    """
    sql = "select max(facultyID) from FacultyMembers"
    res = fetch_query(sql)[0]
    if res[0] == None:
        id = 1
    else:
        id = res[0] + 1

    return id

def loginFaculty() -> FacultyMember:
    """
    Interactive login for a faculty member. Prompts faculty member for their username and password. If faculty doesn't have a username in database, prompts them to register a new account.
    
    :return: The faculty member object of the logged in faculty member.
    """
    print("===== LOG IN =====")
    user = input("Enter your username: ")
    sql = "select * from FacultyMembers where username = ?"
    res = fetch_query(sql, user)

    if (len(res) == 0):
        print("An account with this username doesn't exist, want to register an account?")
        while True:
            ans = input("Y/N: ").upper()
            if ans == "Y":
                registerFaculty()
                return loginFaculty()
            elif ans == "N":
                return None
    
    # Get faculty information
    res = res[0]
    id = res[0]
    username = res[1]
    password = res[2]

    pWord = input("Enter your password: ")
    p = hashlib.sha256(pWord.encode()).hexdigest()
    
    if p != password:
        print("Incorrect password, login failed.")
        return None

    print("Login for", username, "successful!")
    f = FacultyMember(id, username, password, getCoursesTaught(id))
    
    return f

if __name__ =='__main__':
    loginFaculty()