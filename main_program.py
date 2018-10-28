import csv
#
import students_list_dict
import student
import profession_list_dict
import professions
import academic_institutions
import academic_institutions_list_dict1
import professions_in_academic
import professions_in_academic_list_dict
#


#read data from CSV file into a dictionaty.
def read_data_from_csv(csv_name,dic):
    try:
        file_obj = open(csv_name)
        reader = csv.reader(file_obj, delimiter=',')
        #skip the first line which is a title
        #next(reader)
        for line in reader:
            dic_key=line[0]
            value=line[1:]
            dic[dic_key]=value
          #  print(line)
        file_obj.close()
    except Exception:
        print("One file or more do not exists")


#######################



#show students list data.  extract the data from the dictionary.
def show_students(student_dic):
    try:
        print("\n\nList of Students")
        print("**************************************************")
        print("ID         First name      Last name       Phone        profession id     size of company desire")
        for k in student_dic:
           student_id = k
           student_data=student_dic[k]
           student_first_name=student_data[0]
           studunt_last_name=student_data[1]
           student_phone = student_data[2]
           student_profession = student_data[3]
           student_company = student_data[4]

           print("{:10s}".format(student_id),"{:15s}".format(student_first_name),"{:15s}".format(studunt_last_name),"{:12s}".format(student_phone),"{:17s}".format(student_profession),"{:10s}".format(student_company))
    except Exception:
        print("file not found/exists")
    print("**************************************************")
    print("\n\n")


#main
#This program reads data from students.csv into a dictionary
student_dic={}
read_data_from_csv("students_list.csv",student_dic)


#######################

#show academic list.  extract the data from the dictionary.
def show_academic_dic(student_dic):
    try:
        print("\n\nList of Academic institution")
        print("**************************************************")
        print("ID         Academic institution name")
        for k in student_dic:
           academic_id = k
           academic_data=academic_dic[k]
           academic_name=academic_data[0]



           print("{:10s}".format(academic_id),"{:40s}".format(academic_name))
        print("**************************************************")
        print("\n\n")
    except Exception:
        print("file not found/exists")

#main
#This program reads data from academic_institutions_list.csv into a dictionary
academic_dic={}
read_data_from_csv("academic_institutions_list(excel).csv",academic_dic)


#######################




#show professions_list data.  extract the data from the dictionary.
def show_professions_list(professions_list_dic):
        print("\n\nList of professions")
        print("**************************************************")
        print("Profession ID      Profession name")
        for k in professions_list_dic:
           profession_id = k
           profession_data=professions_list_dic[k]
           profession_name=profession_data[0]


           print("{:18s}".format(profession_id),"{:15s}".format(profession_name))
        print("**************************************************")
        print("\n\n")



#main
#This program reads data from professions_list.csv into a dictionary
professions_list_dic={}
read_data_from_csv("professions_list(excel).csv",professions_list_dic)


#######################


#show professions_in_academy_list data.  extract the data from the dictionary.
def show_professions_in_academy_list(professions_in_academy_list):
    try:
        print("\n\nList of professions in academy")
        print("**************************************************")
        print("Profession ID         Academic ID       organization size")
        for k in professions_in_academy_list:
           professions_id = k
           professions_data = professions_in_academy_list[k]
           academic_id = professions_data[0]
           size_of_company = professions_data[1]


           print("{:21s}".format(professions_id),"{:17s}".format(academic_id),"{:10s}".format(size_of_company))
        print("**************************************************")
        print("\n\n")
    except Exception:
        print("file not found/exists")


#main
#This program reads data from professions_in_academy_list.csv into a dictionary

try:
    professions_in_academy_list_dic = {}
    read_data_from_csv("professions_in_academy_list(excel).csv",professions_in_academy_list_dic)
except Exception:
    print("file not found/exists")


#######################







#MAIN
# FIRST MENU
while True:
    print("----------------------------------")
    print("Find a college by ....\n")
    print("1.  For search/add/delete/update (press 1)\n")
    print("2.  Show all information (press 2)\n")
    print("3.  To choose your academic institution (press 3)\n")
    print("----------------------------------")

    option = input("Type the option number or 0 to exit\n")

    if option == '0':
        break
    elif option == '1': # MENU OF OPTIONS
        print("----------------------------------")
        print("1. Press 1 - to search\n")
        print("2. Press 2 - to add\n")
        print("3. Press 3 - to delete\n")
        print("4. Press 4 - to update\n")
        print("----------------------------------")

        action_option = input("Type the option number or 0 to exit \n")
        if action_option == '0':
            break
        elif action_option == '1':
            print("----------------------------------")
            print("1. Press 1 - to search in students\n")
            print("2. Press 2 - to search in profession\n")
            print("3. Press 3 - to search in academic institution\n")
            print("4. Press 4 - to search in professions in academic\n")
            print("----------------------------------")

            serach_option = input("Type the option number or 0 to exit \n")
            if serach_option == '0':
                break
            elif serach_option == '1':
                show_students(student_dic)
                def search_student(student_dict):
                    try:
                        student_id = input("Enter student id:\n")
                        print(student_dict.search(student_id))
                    except Exception as err:
                        print(str(err))

                student_dict = students_list_dict.Student_dict()
                student_dict.load_data()
                search_student(student_dict)
                student_dict.save_data()

            elif serach_option == '2':
                show_professions_list(professions_list_dic)
                def search_profession(profession_dict):
                    try:
                        profession_id = input("Enter profession id:\n")
                        print(profession_dict.search(profession_id))
                    except Exception as err:
                        print(str(err))

                profession_dict = profession_list_dict.Profession_dict()
                profession_dict.load_data()
                search_profession(profession_dict)
                profession_dict.save_data()

            elif serach_option == '3':
                show_academic_dic(academic_dic)
                def search_academic(academic_dict):
                    try:
                        academic_id = input("Enter student id:\n")
                        print(academic_dict.search(academic_id))
                    except Exception as err:
                        print(str(err))

                academic_dict = academic_institutions_list_dict1.Academic_institutions_dict()
                academic_dict.load_data()
                search_academic(academic_dict)
                academic_dict.save_data()

            elif serach_option == '4':
                show_professions_in_academy_list(professions_in_academy_list_dic)
                def search_profession_in_academic(professions_in_academic_dict):
                    try:
                        profession_id = input("Enter profession id(+'(#1/2/3)':\n")
                        print(professions_in_academic_dict.search(profession_id))
                    except Exception as err:
                        print(str(err))


                professions_in_academic_dict = professions_in_academic_list_dict.Professions_in_academic()
                professions_in_academic_dict.load_data()
                search_profession_in_academic(professions_in_academic_dict)
                professions_in_academic_dict.save_data()

        elif action_option == '2':
            print("----------------------------------")
            print("1. Press 1 - to add students\n")
            print("2. Press 2 - to add profession\n")
            print("3. Press 3 - to add academic institution\n")
            print("4. Press 4 - to add professions in academic\n")
            print("----------------------------------")

            add_option = input("Type the option number or 0 to exit \n")
            if add_option == '0':
                break
            elif add_option == '1':
                show_students(student_dic)
                def add_student(student_dict):
                    try:
                        student_id = input("Enter student id: \n")
                        student_first_name = input("Enter student first name: \n")
                        student_last_name = input("Enter student last name: \n")
                        student_phone = input("Enter student phone:\n")
                        student_profession = input("Enter student profession id:\n")
                        student_company = input("Enter student company (small,medium,big):\n")
                        stud = student.Student(student_id, student_first_name, student_last_name, student_phone,
                                               student_profession, student_company)
                        student_dict.add(stud)
                    except Exception as err:
                        print(str(err))

                student_dict = students_list_dict.Student_dict()
                student_dict.load_data()
                add_student(student_dict)
                student_dict.save_data()


            elif add_option == '2':
                show_professions_list(professions_list_dic)
                def add_profession(profession_dict):
                    try:
                        profession_id = input("Enter profession id: \n")
                        profession_name = input("Enter profession name:\n")
                        profession = professions.Professions(profession_id, profession_name)
                        profession_dict.add(profession)
                    except Exception as err:
                        print(str(err))


                profession_dict = profession_list_dict.Profession_dict()
                profession_dict.load_data()
                add_profession(profession_dict)
                profession_dict.save_data()


            elif add_option == '3':
                show_academic_dic(academic_dic)
                def add_academic(academic_dict):
                    try:
                        academic_id = input("Enter academic id: \n")
                        academic_name = input("Enter academic name:\n")
                        academic = academic_institutions.Academic_institutions(academic_id, academic_name)
                        academic_dict.add(academic)
                    except Exception as err:
                        print(str(err))


                academic_dict = academic_institutions_list_dict1.Academic_institutions_dict()
                academic_dict.load_data()
                add_academic(academic_dict)
                academic_dict.save_data()


            elif add_option == '4':
                show_professions_in_academy_list(professions_in_academy_list_dic)


                def add_profession_in_academic(professions_in_academic_dict):
                    try:
                        profession_id = input("Enter profession id(+'(#1/2/3)':\n")
                        academic_id = input("Enter academic id: \n")
                        organization_size = input("Enter organization size (small/medium/big):\n")
                        p_i_a = professions_in_academic.Professions_in_academic(profession_id, academic_id,
                                                                                organization_size)
                        professions_in_academic_dict.add(p_i_a)
                    except Exception as err:
                        print(str(err))


                professions_in_academic_dict = professions_in_academic_list_dict.Professions_in_academic()
                professions_in_academic_dict.load_data()
                add_profession_in_academic(professions_in_academic_dict)
                professions_in_academic_dict.save_data()


        elif action_option == '3':
            print("----------------------------------")
            print("1. Press 1 - to delete students\n")
            print("2. Press 2 - to delete profession\n")
            print("3. Press 3 - to delete academic institution\n")
            print("4. Press 4 - to delete professions in academic\n")
            print("----------------------------------")

            delete_option = input("Type the option number or 0 to exit \n")
            if delete_option == '0':
                break
            elif delete_option == '1':
                show_students(student_dic)
                def delete_student(student_dict):
                    try:
                        student_id = input("Enter student id: \n")
                        student_dict.delete(student_id)
                    except Exception as err:
                        print(str(err))

                student_dict = students_list_dict.Student_dict()
                student_dict.load_data()
                delete_student(student_dict)
                student_dict.save_data()


            elif delete_option == '2':
                show_professions_list(professions_list_dic)
                def delete_profession(profession_dict):
                    try:
                        profession_id = input("Enter profession id: \n")
                        profession_dict.delete(profession_id)
                    except Exception as err:
                        print(str(err))

                profession_dict = profession_list_dict.Profession_dict()
                profession_dict.load_data()
                delete_profession(profession_dict)
                profession_dict.save_data()

            elif delete_option == '3':
                show_academic_dic(academic_dic)
                def delete_academic(academic_dict):
                    try:
                        academic_id = input("Enter academic id: \n")
                        academic_dict.delete(academic_id)
                    except Exception as err:
                        print(str(err))


                academic_dict = academic_institutions_list_dict1.Academic_institutions_dict()
                academic_dict.load_data()
                delete_academic(academic_dict)
                academic_dict.save_data()


            elif delete_option == '4':
                show_professions_in_academy_list(professions_in_academy_list_dic)


                def delete_profession_in_academic(professions_in_academic_dict):
                    try:
                        profession_id = input("Enter profession id(+'(#1/2/3)':\n")
                        professions_in_academic_dict.delete(profession_id)
                    except Exception as err:
                        print(str(err))


                professions_in_academic_dict = professions_in_academic_list_dict.Professions_in_academic()
                professions_in_academic_dict.load_data()
                delete_profession_in_academic(professions_in_academic_dict)
                professions_in_academic_dict.save_data()


        elif action_option == '4':
            print("----------------------------------")
            print("1. Press 1 - to update students\n")
            print("2. Press 2 - to update profession\n")
            print("3. Press 3 - to update academic institution\n")
            print("4. Press 4 - to update professions in academic\n")
            print("----------------------------------")

            update_option = input("Type the option number or 0 to exit \n")
            if update_option == '0':
                break
            elif update_option == '1':
                show_students(student_dic)
                def update_student(student_dict):
                    try:
                        student_id = input("Enter student id: \n")
                        student_first_name = input("Enter student first name: \n")
                        student_last_name = input("Enter student last name: \n")
                        student_phone = input("Enter student phone:\n")
                        student_profession = input("Enter student profession id:\n")
                        student_company = input("Enter student company (small,medium,big):\n")
                        stud = student.Student(student_id, student_first_name, student_last_name, student_phone,
                                               student_profession, student_company)
                        student_dict.update(stud)
                    except Exception as err:
                        print(str(err))


                student_dict = students_list_dict.Student_dict()
                student_dict.load_data()
                update_student(student_dict)
                student_dict.save_data()

            elif update_option == '2':
                show_professions_list(professions_list_dic)
                def update_profession(profession_dict):
                    try:
                        profession_id = input("Enter profession id: \n")
                        profession_name = input("Enter profession name:\n")
                        profession = professions.Professions(profession_id, profession_name)
                        profession_dict.update(profession)
                    except Exception as err:
                        print(str(err))


                profession_dict = profession_list_dict.Profession_dict()
                profession_dict.load_data()
                update_profession(profession_dict)
                profession_dict.save_data()

            elif update_option == '3':
                show_academic_dic(academic_dic)
                def update_academic(academic_dict):
                    try:
                        academic_id = input("Enter academic id: \n")
                        academic_name = input("Enter academic name:\n")
                        academic = academic_institutions.Academic_institutions(academic_id, academic_name)
                        academic_dict.update(academic)
                    except Exception as err:
                        print(str(err))


                academic_dict = academic_institutions_list_dict1.Academic_institutions_dict()
                academic_dict.load_data()
                update_academic(academic_dict)
                academic_dict.save_data()

            elif update_option == '4':
                show_professions_in_academy_list(professions_in_academy_list_dic)
                def update_profession_in_academic(professions_in_academic_dict):
                    try:
                        profession_id = input("Enter profession id(+'(#1/2/3)':\n")
                        academic_id = input("Enter academic id: \n")
                        organization_size = input("Enter organization size (small/medium/big):\n")
                        p_i_a = professions_in_academic.Professions_in_academic(profession_id, academic_id,
                                                                                organization_size)
                        professions_in_academic_dict.update(p_i_a)
                    except Exception as err:
                        print(str(err))

                professions_in_academic_dict = professions_in_academic_list_dict.Professions_in_academic()
                professions_in_academic_dict.load_data()
                update_profession_in_academic(professions_in_academic_dict)
                professions_in_academic_dict.save_data()




    elif option == '2': # MENU OF LISTS
        print("----------------------------------")
        print("1. Press 1 - for list of student\n")
        print("2. Press 2 - for academic institutions list\n")
        print("3. Press 3 - for professions list\n")
        print("4. Press 4 - for professions in_academy list\n")

        print("----------------------------------")

        lists_option = input("Type the option number or 0 to exit \n")
        if lists_option == "0":
            break
        elif lists_option == '1':
            try:
                show_students(student_dic)
            except Exception:
                print("file not found/exists")
            #break
        elif lists_option == '2':
            try:
                show_academic_dic(academic_dic)
            except Exception:
                print("file not found/exists")
            #break
        elif lists_option == '3':
            show_professions_list(professions_list_dic)
            #break
        elif lists_option == '4':
            show_professions_in_academy_list(professions_in_academy_list_dic)
            #break
        else:
            print("Wrong number. try again")

    elif option == '3':
        show_professions_list(professions_list_dic)

        def choose(professions_in_academic_dict):
           try:
            choose = input("choose your desire id profession from the list:\n")
            size = input("choose your organization desire size(small/medium/big):\n")
            professions_in_academic_dict.choose(choose,size)
           except Exception as err:
               print(str(err))

        professions_in_academic_dict = professions_in_academic_list_dict.Professions_in_academic()
        professions_in_academic_dict.load_data()
        choose(professions_in_academic_dict)
        professions_in_academic_dict.save_data()

    else:
        print("Wrong number. try again")