class Dorms():
    def __init__(self, application_nr, student, dorm):
        dorm_list = ["Economica 1", "Economica 2", "Caminul 14", "Caminul 16"]
        self.__application_nr = application_nr
        self.__student = student
        if dorm in dorm_list:
            self.__dorm = dorm
        else:
            raise AssertionError

    # getters and setters for every element
    def get_application_nr(self):
        return self.__application_nr

    def get_student(self):
        return self.__student

    def get_dorm(self):
        return self.__dorm

    def set_application_nr(self, application_nr):
        self.__application_nr = application_nr

    def set_student(self,student):
        self.__student = student

    def set__dorm(self,dorm):
        dorm_list = ["Economica 1", "Economica 2", "Caminul 14", "Caminul 16"]
        if dorm in dorm_list:
            self.__dorm = dorm
        else:
            raise AssertionError

    # overrides the information into string
    def __str__(self):
        return "Application number: " + str(self.__application_nr) + " ,name of the student: " + str(self.__student) \
               + ", from the dorm: " + str(self.__dorm)


