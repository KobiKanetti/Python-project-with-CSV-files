import csv
import professions_in_academic

class Professions_in_academic(object):

    def __init__(self):
        self.professions_in_academic = {}
        self.file_name = "professions_in_academy_list(excel).csv"

    def load_data(self):
        file_obj = open(self.file_name,encoding="utf8")
        reader = csv.reader(file_obj, delimiter = ',')
        for line in reader:
            dic_key = line[0]
            profession_id = line[0]
            academic_id = line[1]
            organization_size = line[2]
            prof_in_academic = professions_in_academic.Professions_in_academic(profession_id,academic_id,organization_size)
            self.professions_in_academic[dic_key] = prof_in_academic
        file_obj.close()


    def save_data(self):
        file_obj = open(self.file_name, 'w',newline='')
        data = csv.writer(file_obj, delimiter=',')
        for var in self.professions_in_academic.values():
            lst = []
            lst.append(var.profession_id)
            lst.append(var.academic_id)
            lst.append(var.organization_size)
            data.writerow(lst)
        del data
        file_obj.close()


    def add(self,profession):
        for var in self.professions_in_academic:
            if var == profession.profession_id:
                raise Exception("Already exists")
        self.professions_in_academic[profession.profession_id] = profession
        print("New profession in academic wa added")


    def delete(self,id):
        for var in self.professions_in_academic:
            if var == id:
                name = self.professions_in_academic[var].profession_id
                self.professions_in_academic.pop(var)
                print("Profession", name, "is deleted")
        raise Exception("Profession not found")

    def search(self,id):
        for var in self.professions_in_academic:
            if var == id:
                return self.professions_in_academic[var]
        raise Exception("Profession not found")

    def update(self, profession):
        for var in self.professions_in_academic:
            if var == profession.profession_id:
                self.professions_in_academic[var] = profession
                print("Profession in academic was updated")
                return
        raise Exception("Academic not found")

    def choose(self,profession,size):
        for var in self.professions_in_academic:
            if var == profession:
               print("1")
               for i in self.professions_in_academic.values:
                   if i == size:
                        print("2")
                        return self.professions_in_academic[var.academic_id]
        raise Exception ("Wrong values")

    def __str__(self):
        return("profession in academic----------")
        for var in self.professions_in_academic.values():
            print(var)
        return ""