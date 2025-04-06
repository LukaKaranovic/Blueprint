from Python.db_queries import fetch_query, execute_query
from Review import Review
from ReviewData import getReview, findNextID
from Course import Course

def writeReview(r: Review, cid: str, stuID: int):
    """
    Writes a review to the database given a Review object and a valid course ID. Also updates course values.

    First checks if the course ID is for an existing course. If the course exists, then it inserts the review into the database.
    After database insertion, the course's difficulty and hours values are updated and written to the database as well.
    :param r: The review to be written to the database.
    :param cid" The course ID of the review.
    """
    if checkCourseID(cid) == False:
        print("Course with the given ID doesn't exist in the database.")
        return

    id = findNextID()
    difficulty = r.getDifficulty()
    hours = r.getHours()
    date = r.getDate()
    text = r.getText()

    sql = "insert into Reviews values (?, ?, ?, ?, ?, ?, ?)" 
    execute_query(sql, id, text, difficulty, hours, date, cid, stuID)
    print("Review for", cid, "submitted succesfully with ID", id)

    # After review has been inserted, update course difficulty and hours values:
    updateCourse(cid)

def updateCourse(cid: str):
    """
    Given a course ID, all current values of the course object will be written to the database.

    This method should be called when:
    1. A faculty member edits information about an existing course.
    2. A new review of the course has been submitted by a student (changes to the average difficulty and hours).
    :param cid: The course ID of the course to be updated
    """
    c = getCourse(cid)

    sql = """update Courses 
    set courseName = ?,
    description = ?,
    recommendedHours = ?,
    courseDifficulty = ?,
    sections = ?,
    recommendedYear = ?,
    term = ?
    where courseID = ?"""
    
    c.calculateAverages(getReviewData(cid)) # Updates hours and difficulty

    execute_query(sql, c.getName(), c.getDescription(), c.getHours(), c.getDifficulty(), c.getSections(), c.getRecYear(), c.getTerm(), cid)
    print("Course information updated in database successfully!")

def addCourse(c: Course):
    """
    Given a Course object, adds the course to the database.

    :param c: The Course object to write to the database.
    """
    cid = c.getID()
    if checkCourseID(cid) == True:
        print("Course with ID", cid, "already exists within the database, can't add it.")
        print("Please use updateCourse() instead.")
        return
    
    sql = "insert into Courses values (?, ?, ?, ?, ?, ?, ?, ?)"
    try:
        execute_query(sql, cid, c.getName(), c.getDescription(), c.getHours(), c.getDifficulty(), c.getSections(), c.getRecYear(), c.getTerm())
        print(cid, "written to the database successfully!")
    except Exception as e:
        print("Error writing", cid, "to the database.")
        print(e)

def getReviewData(cid: str) -> list[Review]:
    """
    Gets all the reviews for a course given the course ID (cid).

    First it queries for all review IDs under a given course, retrieving a list of those review IDs.
    Then for each review ID, it calls getReview() to query the review from the Reviews table and turns it into a Review class object.
    Afterwards, appends it to a list of Review class objects to be returned to the course.

    :param cid: The course ID for the course to get review data for.
    :return: A list of Review objects, where each item in the list is a review for the course.
    """
    sql = "select reviewID from Reviews where courseID = ?"
    courseReviews = fetch_query(sql, cid)
    reviewList = []
    for review in courseReviews:
        reviewList.append(getReview(review[0]))
        
    return reviewList 
    
def getCourse(cid: str) -> Course:
    """
    Gets all data for the course given a course ID, retrieves it from the database, and constructs a Course object.

    :param cid: The course ID of the course to construct.
    :return: The constructed Course class object.
    """
    
    sql = "select * from Courses where courseID = ?"
    data = fetch_query(sql, cid)[0] # There should only be one course with an ID.
    c = Course(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7])
    return c
    
def checkCourseID(cid: str) -> bool:
    """
    Checks if a given course ID already exists within the database.

    :param cid: The given course ID to check
    :return: True if the course ID already exists within the database, false if it does not.
    """
    sql = "select * from Courses where courseID = ?"
    res = fetch_query(sql, cid)
    print(res)

    if len(res) == 0: # If list is empty
        return False
    
    return True

if __name__ == '__main__':
    course = Course()
    course.createCourse()
    addCourse(course)

    r = Review()
    r.createReview()

    writeReview(r, course.getID())

    print(course)