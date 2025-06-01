from .db_queries import fetch_query, execute_query
from .Review import Review
    
def deleteReview(id: int): # deletes a review given an id
    """
    Deletes a review from the database given a reviewID

    :param id: The reviewID of the review to be deleted.
    """
    sql = "delete * from Reviews where reviewID = ?"
    execute_query(sql, id)

def getStuReview(stuID: int, cid: str) -> Review:
    """
    Retrieves a review from the database given a studentID and courseID.

    This method finds a review from the database and then constructs a Review object to be displayed on the frontend.
    :param stuID: The studentID of the student who made the review.
    :param cid: The courseID of the course the review was made for.
    :return: A Review object containing all of the review's information.
    """
    sql = "select * from Reviews where studentID = ? and courseID = ?"
    res = fetch_query(sql, stuID, cid)
    if len(res) == 0:
        return None
    res = res[0]
    review = Review(res[0], res[1], res[2], res[3], res[4], res[5])
    return review

def getReview(rID: int) -> Review:
    """
    Retrieves a review from the database with the given reviewID.

    This method finds a review from the database and then constructs a Review object to be displayed on the frontend.
    :param rID: The studentID of the student who made the review.
    :return: A Review object containing all of the review's information.
    """
    sql = "select * from Reviews where reviewID = ?"
    res = fetch_query(sql, rID)
    if len(res) == 0:
        return None
    res = res[0]
    review = Review(res[0], res[1], res[2], res[3], res[4], res[5])
    return review

def findNextID() -> int:
    """
    Finds the next reviewID to use in the database.

    The next reviewID will be 1 greater than the maximum ID value already existing within 
    the Reviews table in the database.
    :return: The reviewID to be used for the next review.
    """
    sql = "select max(reviewID) from Reviews"
    res = fetch_query(sql)[0]
    if res[0] == None:
        id = 1
    else:
        id = res[0] + 1

    return id

def updateReview(r: Review, stuID: int):
    """
    Updates a review in the database with a given review object and studentID

    :param r: The Review object containing the updated review data.
    :param stuID: The studentID of the student who wrote and updated the review.
    :return: The courseID of the course the review was made for.
    """
    sql = """update Reviews 
    set reviewText = ?,
    difficulty = ?,
    recommendedHours = ?,
    reviewDate = ?,
    courseID = ?,
    studentID = ?
    where reviewID = ?
    """
    execute_query(sql, r.getText(), r.getDifficulty(), r.getHours(), r.getDate(), r.getCourse(), stuID, r.getID())
    print("Review updated!")