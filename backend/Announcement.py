from datetime import datetime
from .CourseData import checkCourseID

class Announcement():
    def __init__(self, id: int = 0, text: str = "", date: str = "", cid: str = "", reactions = 0):
        """
        Instantiates an Announcement object with the given values: id, text, date, cid, and reactions. Otherwise, will use default values.

        :param id: The announcement's unique ID.
        :param text: The text for the announcement.
        :param date: The announcement's posted date.
        :param cid: The ID of the course the announcement is for.
        :param reactions: The current reactions of the announcement, positive if more upvotes, negative if more downvotes.
        """
        self.__annID = id
        self.__annText = text
        self.__annDate = date
        self.__courseID = cid
        self.__reactions = reactions

    #Getter methods:
    def getAnnID(self) -> int:
        return self.__annID

    def getAnnText(self) -> str:
        return self.__annText

    def getAnnDate(self) -> str:
        return self.__annDate

    def getCourse(self) -> str:
        return self.__courseID
    
    def getReactions(self) -> int:
        return self.__reactions

    #Setter methods:
    def setAnnID(self, aid: str):
        self.__annID = aid

    def setAnnText(self, atext: str):
        self.__annText = atext

    def setAnnDate(self, adate: str):
        self.__annDate = adate
        
    def setCourse(self, course: str):
        self.__courseID = course

    def setReactions(self, reactions: int):
        self.__reactions = reactions

    def createAnnouncement(self, cid: str):
        """FOR TESTING PURPOSES ONLY: Creates an Announcement object

        Prompts user to enter a courseID for the course of the announcement, calls checkCourseID to ensure course exists in database,
        then prompts user to enter the announcement text,
        and then sets the announcement date to the current day
        """
        self.setCourse(cid)
        
        # Get text section
        while True:
            text = input("Enter the text to your announcement post, between 1-500 characters: ")
            if (len(text) < 1 or len(text) > 500):
                print("Announcement text size is not correct, please enter between 1-500 characters")
            else:
                self.setAnnText(text)
                break
        
        self.setAnnDate(str(datetime.today().date()))
