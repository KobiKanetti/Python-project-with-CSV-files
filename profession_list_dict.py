import csv
import professions

class Profession_dict(object):

    def __init__(self):
        self.professions = {}
        self.file_name = "professions_list(excel).csv"


    def load_data(self):
        file_obj = open(self.file_name, encoding="utf8")
        reader = csv.reader(file_obj, delimiter=',')
        #next(reader)
        for line in reader:
            dic_key = line[0]
            profession_id = line[0]
            profession_name = line[1]
            prof = professions.Professions(profession_id,profession_name)
            self.professions[dic_key] = prof
        file_obj.close()


    def save_data(self):
        file_obj = open(self.file_name, 'w', newline='')
        data = csv.writer(file_obj, delimiter=',')
        for var in self.professions.values():
            lst = []
            lst.append(var.profession_id)
            lst.append(var.profession_name)
            data.writerow(lst)
        del data
        file_obj.close()


    def add(self,profession):
        for var in self.professions:
            if var == profession.profession_id:
                raise Exception("Profession exists")
        self.professions[profession.profession_id] = profession
        print("New profession was added")


    def delete(self,id):
        for var in self.professions:
            if var == id:
                name = self.professions[var].profession_name
                self.professions.pop(var)
                print("Profession",name,"is deleted")
                return
        raise Exception("Profession not found")


    def update(self,profession):
        for var in self.professions:
            if var == profession.profession_id:
                self.professions[var] = profession
                print("Profession was updated")
                return
        raise Exception("Profession not found")


    def search(self,id):
        for var in self.professions:
            if var == id:
                return self.professions[var]
        raise Exception("Profession not found")


    def __str__(self):
        return ("professions------")
        for var in self.professions.values():
            print(var)
        print("")