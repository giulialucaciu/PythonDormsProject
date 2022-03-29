class Repo():
    # the list data will contain each application
    def __init__(self):
        self.__data = []

    def get_repo(self):
        return self.__data

    # add each application into the list, verifying every aspect
    def add_repo(self, application):
        dorm_list = ["Economica 1", "Economica 2", "Caminul 14", "Caminul 16"]
        if application.get_application_nr() < 0:
            raise AssertionError
        if not application.get_student():
            raise AssertionError
        if application.get_dorm() not in dorm_list:
            raise AssertionError
        self.__data.append(application)

    # function to display only the students that have an application nr greater than a predefined nr
    def greater_than(self, set_nr):
        # we choose a k number(initially 0),
        # that increases each time a student has their application nr greater than set_nr
        k = 0
        # a 'for' statement to go through each application in the data list
        for i in range(len(self.__data)):
            if self.__data[i].get_application_nr() > set_nr:
                k += 1
        if k == 0:
            return "no students have the application nr more than " + str(set_nr)
        else:
            return str(k) + " student(s) have their application nr greater than " + str(set_nr)

    # function to sort the students by their name, in alphabetical order
    def sort_student(self):
        # define an empthy list which will contain only the names of the students from the data list
        names = []
        for student in self.__data:
            names.append(student.get_student())
        # predefined function to sort the names
        names.sort()
        return "names of students, sorted by alphabetical order: " + str(names)


