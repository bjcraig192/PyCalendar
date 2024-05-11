import GoogleAuthClass
import GoogleQueryClass

class GoogleHandler:
    
    googleAuth = None
    googleQuery = None

    def __init__(self):
        self.googleAuth = GoogleAuthClass.GoogleAuth()
        self.googleQuery = GoogleQueryClass.GoogleQuery(self.googleAuth)
        