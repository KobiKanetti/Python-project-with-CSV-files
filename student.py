

class Student(object):

    def __init__(self,student_id,first_name,last_name,phone,profession,company):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.profession = profession
        self.company = company

    def __str__(self):
        print("ID: "+self.student_id+", First name: "+self.first_name+", Last name: "+self.last_name+
                ", Phone: "+self.phone+", Profession: "+self.profession+
                ", Company: "+self.company)