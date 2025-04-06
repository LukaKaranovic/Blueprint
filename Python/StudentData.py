from Student import Student
from Python.db_queries import fetch_query, execute_query
from ReviewData import getReview

def registerStudent():
    """
    Asks the student for their username and password, hashes the password, gets the next available student ID, and stores it to the database.
    """
    s = Student()
    s.register()

    s.setID(getNextID())

    sql = "insert into Students values (?, ?, ?)"

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
        stuReviews.append(getReview(review))

    return stuReviews

def getNextID() -> int:
    """
    Finds the next studentID to use in the database.

    The next studentID will be 1 greater than the maximum ID value already existing within 
    the Students table in the database.
    :return: The studentID to be used for the next student.
    """
    sql = "select max(studentID) from Students:
    res = fetch_query(sql)[0]
    if res[0] == None:
        id = 1
    else:
        id = res[0] + 1

    return id

def checkIfReacted(stuID: int, aid: int) -> int:
    """
    Checks if a student has already reacted to an announcement.

    :return: -1 if the student hasn't reacted to the announcement, 0 if they reacted with a downvote, 1 if they reacted with an upvote.
    """
    sql = "select reaction from AnnouncementReactions where studentID = ? and announcementID = ?"
    res = fetch_query(sql, stuID, aid)
    if (len(res) == 0):
        return -1
    
    return res[0]
