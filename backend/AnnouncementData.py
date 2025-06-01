from .Announcement import Announcement
from .db_queries import *
from datetime import datetime

def postAnnouncement(ann: Announcement, facID: int):
    """
    Given an Announcement object and a faculty ID, adds the announcement to the database.

    :param ann: The Announcement object to write to the database.
    :param facID: The faculty ID of the faculty member who made the announcement.
    """
    aid = getNextID()
    text = ann.getAnnText()
    date = ann.getAnnDate()
    cid = ann.getCourse()
    
    sql = "insert into Announcements values (?, ?, ?, ?, ?)"
    execute_query(sql, aid, text, date, cid, facID)
    print("Announcement for", cid, "posted to database!")


def getAnnouncement(annID: int) -> Announcement:
    """
    Gets all data for the course given a announcement ID, retrieves it from the database, and constructs an Announcement object.

    :param annID: The announcement ID of the announcement to construct.
    :return: The constructed Announcement class object.
    """
    sql = "select * from Announcements where AnnouncementID = ?"
    res = fetch_query(sql, annID)
    if len(res) == 0:
        print("Announcement with ID", annID, "doesn't exist")
        return None

    res = res[0]
    reactions = getReactions(annID)
    
    a = Announcement(res[0], res[1], res[2], res[3], reactions)
    return a
     

def getReactions(annID: int) -> int:
    """
    Gets the reaction state of an announcement as an int.

    Positive if there are more upvotes than downvotes, negative if vice versa.
    Gets all data from querying AnnouncementReactions table.
    Should be called when an announcement is being retried, or when someone has reacted to it since it was constructed.
    :return: The reaction state of the announcement (total upvotes - total downvotes).
    """
    usql = """select count(*) 
        from AnnouncementReactions 
        where AnnouncementID = ? and reaction = 1
        """
    
    dsql = """select count(*) 
        from AnnouncementReactions 
        where AnnouncementID = ? and reaction = 0
        """

    upvotes = fetch_query(usql, annID)
    downvotes = fetch_query(dsql, annID)

    reactions = upvotes[0][0] - downvotes[0][0]
    
    return reactions

def getNextID() -> int:
    """
    Finds the next announcementID to use in the database.

    The next announcementID will be 1 greater than the maximum ID value already existing within 
    the Announcements table in the database.
    :return: The announcementID to be used for the next announcement.
    """
    sql = "select max(announcementID) from Announcements"
    res = fetch_query(sql)[0]
    if res[0] == None:
        id = 1
    else:
        id = res[0] + 1

    return id

def updateEditHistory(facID: int, cid: str):
    """
    Updates the CourseEditHistory after a course has been edited by a faculty announcement. Also automatically makes and postsan announcement with the course change description.
    

    Note - if the course ID was changed, the old course ID is passed to this function, not the new one.
    :param facID: The ID of the faculty member who edited the course.
    :param cid: The ID of the course that was edited.
    """
    desc = input("Edit the description of your changes to the course: ")
    editDate = str(datetime.today().date())
    
    sql = "insert into CourseEditHistory values (?, ?, ?, ?)"
    execute_query(sql, cid, facID, editDate, desc)
    a = Announcement(getNextID(), desc, editDate, cid)
    postAnnouncement(a, facID)

def getAnnouncementBoard() -> list[Announcement]:
    sql = "select announcementID from Announcements order by AnnouncementDate desc, announcementID desc"
    res = fetch_query(sql)

    if len(res) == 0:
        print("No announcements on the announcement board at this time.")

    annBoard = []
    i = 0
    while i < 3 and i < len(res):
        annBoard.append(getAnnouncement(res[i][0]))
        i += 1
    return annBoard

def getCourseAnnouncements(cid: str) -> list[Announcement]:
    courseAnns = []
    sql = "select announcementID from Announcements where courseID = ?"
    res = fetch_query(sql, cid)
    if len(res) == 0:
        print("Course has no announcements.")
        return courseAnns

    for a in res:
        courseAnns.append(getAnnouncement(a[0]))
    return courseAnns