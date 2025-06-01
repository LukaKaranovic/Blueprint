from .Student import Student
from .db_queries import *
from .ReviewData import getReview
from .Review import Review
from .AnnouncementData import getReactions, getAnnouncement
import hashlib
import time

def registerStudent():
    """
    Asks the student for their username and password, hashes the password, gets the next available student ID, and stores it to the database.
    """
    print('===== REGISTER ACCOUNT =====')
    s = Student()
    s.register()

    s.setID(getNextID())

    sql = "insert into Students values (?, ?, ?)"

    # FAKE IT UNTIL YOU MAKE IT
    stunum = input("Enter your student number: ")
    print("Waiting for", stunum, "to sign in to VIU student database...")
    time.sleep(5)
    print("Student verified!")

    execute_query(sql, s.getID(), s.getUsername(), s.getPassword())
    print("Student registered to database!")

def getReviews(stuID: int) -> list[Review]:
    """
    Returns a list of all the Review objects a student has written.

    :param stuID: The ID of the student whose reviews are being retrieved.
    """
    sql = "select reviewID from Reviews where studentID = ?"
    reviews = fetch_query(sql, stuID)
    stuReviews = []
    for review in reviews:
        stuReviews.append(getReview(review[0]))

    return stuReviews

def getNextID() -> int:
    """
    Finds the next studentID to use in the database.

    The next studentID will be 1 greater than the maximum ID value already existing within 
    the Students table in the database.
    :return: The studentID to be used for the next student.
    """
    sql = "select max(studentID) from Students"
    res = fetch_query(sql)[0]
    if res[0] == None:
        id = 1
    else:
        id = res[0] + 1

    return id

def checkIfReacted(stuID: int, annID: int) -> int:
    """
    Checks if a student has already reacted to an announcement.

    :return: -1 if the student hasn't reacted to the announcement. 0 if they downvoted, 1 if they upvoted the announcement.
    """
    sql = "select reaction from AnnouncementReactions where studentID = ? and announcementID = ?"
    res = fetch_query(sql, stuID, annID)
    if (len(res) == 0):
        return -1
    
    return res[0][0]

def updateReaction(stuID: int, annID: int, reaction: int):
    """
    Allows a student to react to an announcement and updates their reaction to that specific announcement.

    If they have already reacted with an upvote/downvote, reacting the same way again will unreact them.
    When unreacting, student's reaction record is removed from the AnnouncementReactions table. 
    When reacting, student's reaction record is added to the AnnouncementReactions table, or if they are already in the table, their reaction has changed.
    Each time this function is called, the relevant announcement is retrieved and their reactions are updated.
    :param stuID:
    :param annID:
    :param reaction:
    """
    status = checkIfReacted(stuID, annID)
    
    unreactSQL = "delete from AnnouncementReactions where studentID = ? and AnnouncementID = ?"
    reactSQL = "update AnnouncementReactions set reaction = ? where studentID = ? and AnnouncementID = ?"
    insertSQL = "insert into AnnouncementReactions values (?, ?, ?)"
    
    # If reacted wth downvote before.
    if status == 0:
        if reaction == 0:
            execute_query(unreactSQL, stuID, annID)
        elif reaction == 1:
            execute_query(reactSQL, reaction, stuID, annID)
    # If reacted with upvote before.
    elif status == 1:
        if reaction == 0:
            execute_query(reactSQL, reaction, stuID, annID)
        elif reaction == 1:
            execute_query(unreactSQL, stuID, annID)
    # If haven't reacted before.
    else:
        execute_query(insertSQL, annID, stuID, reaction)

    # Update announcement's reactions by reconstructing the object.
    a = getAnnouncement(annID)
     
def loginStudent() -> Student:
    """
    Interactive login for a student. Prompts student for their username and password. If student doesn't have a username in database, prompts them to register a new account.
    
    :return s: The student object of the logged in student.
    """
    print("===== LOG IN =====")
    user = input("Enter your username: ")
    sql = "select * from Students where username = ?"
    res = fetch_query(sql, user)

    if (len(res) == 0):
        print("An account with this username doesn't exist, want to register an account?")
        while True:
            ans = input("Y/N: ").upper()
            if ans == "Y":
                registerStudent()
                return loginStudent()
            elif ans == "N":
                return None
    
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
    s = Student(id, username, password)
    
    return s

if __name__ == '__main__':
    loginStudent()