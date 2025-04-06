import sqlite3

from Python.db_queries import fetch_query, execute_query
from Review import Review
    
def deleteReview(id: int): # deletes a review given an id
    """
    Deletes a review from the database given a reviewID

    :param id: The reviewID of the review to be deleted.
    """
    sql = "delete * from Reviews where reviewID = ?"
    execute_query(sql, id)

def getReview(id: int) -> Review:
    """
    Retrieves a review from the database given a reviewID

    This method finds a review from the database and then constructs a Review object to be displayed on the frontend.
    :param id: The reviewID of the review to be retrieved.
    :return: The retrieved review as a Review object.
    """
    sql = "select * from Reviews where reviewID = ?"
    print(fetch_query(sql, id))
    res = fetch_query(sql, id)[0] # first row of result set
    review = Review(res[0], res[1], res[2], res[3], res[4]) # first 5 column values
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

# [(None,)]
# []