from datetime import datetime

class Review():
    """
    Creates a review object that can be written to the database or displayed to the frontend.
    """

    def __init__(self, id: int = 0, text: str = "", diff: float = 0.0, hours: int = 0, date: str = "", cid: str = ""):
        """
        Instantiates a Review object with the given values: id, text, diff, hours, date. Otherwise, will use default values.

        :param id: The review's ID.
        :param text: The review's descriptive text.
        :param diff: The review's difficulty rating.
        :param hours: The review's hours per week recommendation.
        :param date: The date the review was created.
        """
        self.__reviewID = id
        self.__reviewText = text
        self.__difficulty = diff
        self.__recHours = hours
        self.__reviewDate = date
        self.__course = cid
    
    # Getter methods:
    def getID(self) -> int:
        return self.__reviewID
    
    def getText(self) -> str:
        return self.__reviewText

    def getDifficulty(self) -> float:
        return self.__difficulty

    def getHours(self) -> int:
        return self.__recHours
    
    def getDate(self) -> str:
        return self.__reviewDate
    
    def getCourse(self) -> str:
        return self.__course

    # Setter methods:
    def setID(self, id):
        self.__reviewID = id

    def setText(self, text):
        self.__reviewText = text

    def setDifficulty(self, diff):
        self.__difficulty = diff
    
    def setHours(self, hours):
        self.__recHours = hours
    
    def setDate(self, date):
        self.__reviewDate = date
        
    def setCourse(self, cid):
        self.__course = cid

    def createReview(self):
        """
        Creates a review object from the command line. (FOR DEVELOPMENT PURPOSES)

        Has several command line prompts and input fields asking the user for the review's difficulty, recommended hours, and descriptive text.
        """

        # Get difficulty section
        while True:
            try:
                diff = float(input("Enter a difficulty: "))
                if (diff >= 0.0 and diff <= 5.0):
                    self.setDifficulty(diff)
                    break
                else:
                    print("Invalid input: Difficulty must be between 0.0 and 5.0.")
            except ValueError:
                print("Value is of incorrect data type, try again.")
        
        # Get hours section
        while True:
            try:
                hours = int(input("Enter the recommended hours per week someone should spend on this course: "))
                if (hours > 0):
                    self.setHours(hours)
                    break
                else:
                    print("Invalid input: Hours cannot be negative.")
            except ValueError:
                print("Value is of incorrect data type, try again.")
        
        # Get text Section
        while True:
            text = str(input("Enter the text for your review: \n"))
            if (len(text) > 0 and len(text) <= 500):
                self.setText(text)
                break
            else:
                print("Text is an invalid character size, must be between 0 and 500 characters.")
        
        # Set the date to current day
        self.setDate(str(datetime.today().date()))

# Run this to create a review and see the object's values!
if __name__ == '__main__':
    r = Review()
    r.createReview()
    print("Difficulty:", r.getDifficulty(), "\nRecommended Hours:", r.getHours(), "\nReview Text:\n", r.getText(), "\nDate:", r.getDate())
