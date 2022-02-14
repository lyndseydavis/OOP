class Student:
    def __init__(self, ID, Name, DOB, Class):
        self.__StudentID = ID
        self.__Name = Name
        self.__DateofBirth = DOB
        self.__Classification = Class

    def set_ID(self,ID):
        self.__StudentID = str(ID)
    
    def set_Name(self,Name):
        self.__Name = str(Name)
    
    def set_Class (self,Class):
        self.__Classifcation = str(Class)

    def register_date(self, Class):
        if self.__Classification ==  "Sr":
            print("11/1 thru 11/3")
        elif self.__Classification == "Jr":
            print("11/4 thru 11/6")
        elif self.__Classification == "S":
            print("11/7 thru 11/9")
        elif self.__Classification == "F":
            print("11/10 thru 11/12")
        else:
            print("Student Classification not found.")
    
    def get_age (self, DOB):
       year = self.__DateofBirth.split(2)

    def get_ID (self, ID):
        
        
