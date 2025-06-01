from .Review import Review
from .ReviewData import *

class Course():
    """
    Creates a course object that can be added to the database or displayed to the frontend.

    This object gets all reviews for a given class, calculates appropriate values, and stores them.
    """
    
    def __init__(self, id: str = "", name: str = "", desc: str = "", hours: float = 0.0, diff: float = 0.0, sections: str = "N/A", year: int = 0, term: str = "N/A" ):
        """
        Instantiates a Course object with the given values: id, name, desc, diff, hours, sections, year, term. Otherwise, will use default values.

        :param id: The course's ID.
        :param name: The course's name - E.g. 'CSCI 260'.
        :param desc: The course's description.
        :param diff: The course's difficulty rating.
        :param hours: The hours per week recommendation to be successful in this course.
        :param sections: The course's sections for the term and their schedules.
        :param year: The recommended year this course should be taken in.
        :param term: The term that the course is offered in ('Spring', 'Fall' or 'Both'). Note that CSCI classes aren't offered in the summer term.
        """
        self.__id = id
        self.__name = name
        self.__description = desc
        self.__recHours = hours
        self.__difficulty = diff
        self.__sections = sections
        self.__recYear = year
        self.__term = term

    # Getter methods:
    def getID(self) -> str:
        return self.__id
    
    def getName(self) -> str:
        return self.__name
  
    def getDescription(self) -> str:
        return self.__description
        
    def getHours(self) -> float:
        return self.__recHours
        
    def getDifficulty(self) -> float:
        return self.__difficulty
    
    def getSections(self) -> str:
        return self.__sections
    
    def getRecYear(self) -> int:
        return self.__recYear
    
    def getTerm(self) -> str:
        return self.__term
    
    # Setter methods:    
    def setID(self, cid: str):
        self.__id = cid

    def setName(self, name: str):
        self.__name = name
        
    def setDescription(self, desc: str):
        self.__description = desc
        
    def setHours(self, hours: float):
        self.__recHours = hours
        
    def setDifficulty(self, diff: float):
        self.__difficulty = diff

    def setSections(self, sections: str):
        self.__sections = sections
    
    def setRecYear(self, year: int):
        self.__recYear = year
    
    def setTerm(self, term: str):
        self.__term = term
            
    def calculateAverages(self, rs: list):
        """
        Calculates and updates a course's difficulty and recommended hours per week.
        
        Gets the average difficulty and recommendend hours from all reviews for a course.
        Updates the Course object's attributes with the newly calculated values.
        This function should be used when instantiating a course or whenever a review of the course is written.
        :param rs: The list of all reviews for a course.
        """
        
        if len(rs) == 0:
            return
        
        # Get difficulty
        dsum = 0.0
        for review in rs:
            dsum += review.getDifficulty()
        
        diff = dsum / len(rs)

        # Get hours
        hsum = 0.0
        for review in rs:
            hsum += review.getHours()
        
        hours = hsum / len(rs)

        self.setDifficulty(round(diff, 1))
        self.setHours(round(hours, 1))
        
    def createCourse(self):
        """TO BE USED FOR TESTING:
        
        A command line interface way of making courses where you are promptign to fill in each data field.
        """
        
        # Get course ID
        while True:
            cid = input("Enter a course ID (e.g. CSCI 260): ").upper()
            if len(cid) < 1 or len(cid) > 10:
                print("Course ID is not of the correct format.")
            else:
                self.setID(cid)
                break
        
        # Get course name
        while True:
            name = input("Enter the name of the course in full (e.g. Topics in Computer Science): ")
            if len(name) < 1 or len(name) > 50:
                print("Course name is empty or too long, please retry.")
            
            else:
                self.setName(name)
                break
        
        # Get course description      
        while True:
            desc = input("Enter a description of the course: ")
            if (len(cid) > 1000):
                print("Description is too long, description should be less than 1000 characters.")
            else:
                self.setDescription(desc)
                break  
        
        # Get course sections                
        while True:
            sections = input("Enter the sections and schedule of a course (E.g. S25N01 - Mo We 11:30-13:00): ")
            if (len(sections) < 1):
                print("You must enter atleast one section.")
            else:
                self.setSections(sections)
                break 

        # Get Recommended year
        while True:
            try:
                year = int(input("Enter the recommended year that this course be taken by students (1,2,3,4): "))
                if (year >= 1 or year <= 4):
                    self.setRecYear(year)
                    break
                else:
                    print("Invalid input, please enter a single digit number between 1-4.")
            except ValueError:
                print("Value is of incorrect data type, try again.")
        
        # Get course term                
        while True:
            try:
                term = int(input("""Enter the term this course is offered in:
                                1 - Fall
                                2 - Spring
                                3 - Both
                                """))
                match term:
                    case 1:
                        self.setTerm("Fall")
                        break   
                    case 2:
                        self.setTerm("Spring")
                        break   
                    case 3:
                        self.setTerm("Both") 
                        break   
                    case _:
                        print("Please select either 1, 2, or 3.")
            except ValueError:
                print("Value is of incorrect data type, try again.")
        
        print("Course creation successful!")
        