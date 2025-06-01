from .Course import Course
from .Review import Review
from .CourseData import writeReview, getCourse, checkCourseID
from .ReviewData import getStuReview, updateReview
from datetime import datetime
import hashlib

class Student():
    def __init__(self, stuID: int = 0, username: str = "", password: str = ""):
        """
        Instantiates a Student user object with the given values: stuID, username, and password (hashed). Otherwise, will use default values.

        :param stuID: The student's unique ID.
        :param username: The student's account username.
        :param password: The student's encrypted password.
        """
        self.__stuID = stuID
        self.__username = username
        self.__password = password
        self.selectedCourses = []
    
    # Getter methods:
    def getID(self) -> int:
        return self.__stuID
    
    def getUsername(self) -> str:
        return self.__username
        
    def getPassword(self) -> str:
        return self.__password

    def getSelCourses(self) -> list:
        return self.selectedCourses

    # Setter methods:
    def setID(self, stuID: str):
        self.__stuID = stuID

    def setUsername(self, user: str):
        self.__username = user
    
    def setPassword(self, pWord: int):
        self.__password = pWord

    def calculateSemesterData(self):
        """
        Calculates the semester data from a student's selected courses list.
        
        Returns a 3-element list containing the selected courses, average difficulty, and total recommended hours per week.
        Index 0 is a list of Course objects, index 1 is the semester's average difficulty, index 2 is the total hours per week.
        :return: A list of the results in the format described above, named 'semesterData'.
        """
        dsum = 0.0
        semesterData = [[], 0.0, 0.0]

        for course in self.selectedCourses:
            dsum += course.getDifficulty()
            semesterData[2] += course.getHours()
            semesterData[0].append(course)
        
        semesterData[1] = dsum / len(self.selectedCourses)

        # Rounding to one decimal place.
        semesterData[1] = round(semesterData[1], 1)
        semesterData[2] = round(semesterData[2], 1)
        return semesterData

    def selectCourse(self): # In final version, cid will be a param
        """
        Selects a course to be stored in selected courses.
        
        Input a courseID, check that the courseID exists and then append the corresponding Course object with the given courseID to selectedCourses.
        """
        cid = input("What course do you want to add to your semester? ").upper()
        if checkCourseID(cid):
            for course in self.getSelCourses():
                if cid == course.getID():
                    print("You have already selected that course! Returning to main page.")
                    return
            self.selectedCourses.append(getCourse(cid))
            print(cid, "added to your semester!")

        else:
            print("Course doesn't exist within the database! Try again..")
            return
    
    def makeReview(self):
        """
        FOR TESTING PURPOSES ONLY: Allows student to input a course ID and write a review for the course.
        """
        # Get course section
        cid = input("What course is this review for (e.g. CSCI 260)? ").upper()
        
        if checkCourseID(cid) == False:
            print("Course doesn't exist within the database! Leaving review creator.")
            return
        
        if getStuReview(self.getID(), cid) is not None:
            print("You have already written a review for this course. Leaving review creator.")
            return

        # Make review section
        review = Review()
        review.createReview()
        writeReview(review, cid, self.getID())

    def editReview(self):
        """
        Allows a student to edit one of their existing reviews for a course.
        """
        cid = input("What course do you want to edit your review for? ").upper()

        r = getStuReview(self.getID(), cid)
        if r is None:
            print("You have not written a review for that course! Leaving review editor.")
            return
        print("===== OLD REVIEW =====")
        print("Course:", r.getCourse())
        print("Difficulty:", r.getDifficulty())
        print("Recommended hours per week", r.getHours())
        print("Review: \n" + r.getText())
        print("--------------------------------------------")

        command = -1
        while command != '0':
            command = input("""Review editor for your review of {course}: Type the following number to do the following action:
            0 - Leave the review editor
            1 - Edit the difficulty rating
            2 - Edit the recommended hours per week
            3 - Edit the review text
            """.format(course = cid))
            match command:
                case '0': # Leave the review editor
                    print("Leaving the review editor.")
                case '1':
                    try:
                        diff = float(input("Enter the new difficulty: "))
                        if (diff >= 0.0 and diff <= 5.0):
                            r.setDifficulty(diff)
                        else:
                            print("Invalid input: Difficulty must be between 0.0 and 5.0.")
                    except ValueError:
                        print("Value is of incorrect data type, try again.")
                case '2':
                    try:
                        hours = int(input("Enter the new recommended hours per week someone should spend on this course: "))
                        if (hours > 0):
                            r.setHours(hours)
                        else:
                            print("Invalid input: Hours cannot be negative.")
                    except ValueError:
                        print("Value is of incorrect data type, try again.")
                case '3':       
                    text = str(input("Enter the new text for your review: \n"))
                    if (len(text) > 0 and len(text) <= 500):
                        r.setText(text)
                    else:
                        print("Text is an invalid character size, must be between 0 and 500 characters.")
                case _: # Invalid command input
                    print("Invalid input, try again!")
        
        r.setDate(str(datetime.today().date()))

        updateReview(r, self.getID())
                
    def register(self):
        """
        Allows a student to input their username and password for account registration.
        """

        # Get the username
        while True:
            user = input("Enter a username between 1-20 characters: ")
            if len(user) == 0 or len(user) > 20:
                print("Username is not between 1-20 characters, please try again")
            else:
                self.__username = user
                break
        # Get the password        
        while True:
            pWord = input("Enter a password: ")
            if len(pWord) == 0:
                print("Password must be longer than 0 characters!")
            else:
                self.__password = hashlib.sha256(pWord.encode()).hexdigest()
                break
      