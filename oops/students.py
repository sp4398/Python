from gettext import lngettext


class Students:
    def __init__(self,firstName,lastName,rollNumber):
        self.firstName=firstName
        self.lastName=lastName
        self.rollNumber=rollNumber
    
    def coding(self):
        print ("Coding")

    def studyings(self):
        print ("Studying")

def main():
    s1=Students("Saurav","Pandey",19)
    print(s1.firstName)
    print(s1.lastName)
    print(s1.rollNumber)
    s1.coding()
    s1.studyings()

    s2=Students("Haripriya","Yadav",20)
    print(s2.firstName)
    print(s2.lastName)
    print(s2.rollNumber)
    s2.coding()
    s2.studyings()


if __name__ == "__main__":
    main()