import csv
import student
import profession_list_dict


class Student_dict(object):

    def __init__(self):
        self.students = {}
        self.file_name = "students_list.csv"

    def load_data(self):
        file_obj = open(self.file_name, encoding="utf8")
        reader = csv.reader(file_obj, delimiter=',')
        #next(reader)
        for line in reader:
            dic_key = line[0]
            student_id = line[0]
            student_first_name = line[1]
            student_last_name = line[2]
            student_phone = line[3]
            student_profession = line[4]
            student_company = line[5]
            #prof = profession_list_dict.search(student_profession)
            stud = student.Student(student_id,student_first_name,student_last_name,
                                   student_phone,student_profession,
                                   student_company)
            self.students[dic_key] = stud
        file_obj.close()


    def save_data(self):
        file_obj = open(self.file_name,'w',newline='')
        data = csv.writer(file_obj,delimiter=',')
        for var in self.students.values():
            lst = []
            lst.append(var.student_id)
            lst.append(var.first_name)
            lst.append(var.last_name)
            lst.append(var.phone)
            lst.append(var.profession)
            lst.append(var.company)
            data.writerow(lst)
        del data
        file_obj.close()


    def add(self,student):
        for var in self.students:
            if var == student.student_id:
                raise Exception("Student exists")
        self.students[student.student_id] = student
        print("New student was added")


    def search(self,id):
        for var in self.students:
            if var == id:
                return self.students[var]
        raise Exception("Student not found")

    def delete(self,id):
        for var in self.students:
            if var == id:
                name = self.students[var].student_id
                self.students.pop(var)
                print("Student",name,"is deleted")
        raise Exception("Student not found")


    def update(self,student):
        for var in self.students:
            if var == student.student_id:
                self.students[var] = student
                print("Student was updated")
                return
        raise Exception("Student not found")



    def __str__(self):
        return("Students list------")
        for var in self.students.values():
            print(var)
        print("")


