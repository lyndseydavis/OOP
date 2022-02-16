class Student:
    def __init__(self, ID, Name, DOB, Class):
        self.__StudentID = ID
        self.__Name = Name
        self.__DateofBirth = DOB
        self.__Classification = Class

    def set_ID(self, ID):
        self.__StudentID = str(ID)

    def set_Name(self, Name):
        self.__Name = str(Name)

    def set_Class(self, Class):
        self.__Classifcation = str(Class)

    def set_DOB(self, DOB):
        self.__DateofBirth = str(DOB)

    def register(self):
        if self.__Classification == "Sr":
            return "11/1 thru 11/3"
        elif self.__Classification == "Jr":
            return "11/4 thru 11/6"
        elif self.__Classification == "S":
            return "11/7 thru 11/9"
        elif self.__Classification == "F":
            return "11/10 thru 11/12"
        else:
            return "Student Classification not found."

    def age(self):
        ls = self.__DateofBirth.split("/")
        dob_year = int(ls[2])
        current = int(2022)
        age = current - dob_year
        return age

    def get_ID(self):
        return self.__StudentID

    def get_Name(self):
        return self.__Name
