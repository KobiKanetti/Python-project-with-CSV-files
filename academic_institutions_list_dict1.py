import csv
import academic_institutions

class Academic_institutions_dict(object):

    def __init__(self):
        self.academic_institutions = {}
        self.file_name = "academic_institutions_list(excel).csv"


    def load_data(self):
        file_obj = open(self.file_name, encoding="utf8")
        reader = csv.reader(file_obj, delimiter=',')
        for line in reader:
            dic_key = line[0]
            academic_id = line[0]
            academic_name = line[1]
            academic = academic_institutions.Academic_institutions(academic_id,academic_name)
            self.academic_institutions[dic_key] = academic
        file_obj.close()


    def save_data(self):
        file_obj = open(self.file_name,'w', newline='')
        data = csv.writer(file_obj, delimiter=',')
        for var in self.academic_institutions.values():
            lst = []
            lst.append(var.academic_id)
            lst.append(var.academic_name)
            data.writerow(lst)
        del data
        file_obj.close()

    def add(self,academic):
        for var in self.academic_institutions:
            if var == academic.academic_id:
                raise Exception("Academic exists")
        self.academic_institutions[academic.academic_id] = academic
        print("New academic eas added")


    def delete(self,id):
        for var in self.academic_institutions:
            if var == id:
                name = self.academic_institutions[var].academic_name
                self.academic_institutions.pop(var)
                print("Academic", name, "is deleted")
                return
        raise Exception("Academic not found")

    def search(self,id):
        for var in self.academic_institutions:
            if var == id:
                return self.academic_institutions[var]
        raise Exception("Academic not found")

    def update(self, academic):
        for var in self.academic_institutions:
            if var == academic.academic_id:
                self.academic_institutions[var] = academic
                print("Academic was updated")
                return
        raise Exception("Academic not found")



    def __str__(self):
        return("Academic institutions-------")
        for var in self.academic_institutions.values():
            print(var)
        print("")
