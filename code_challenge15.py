import os
import json
 
os.system('cls') 
print("Student information System")
print('-------------------')

list_record = {}

while True:
    print("Select from the following options: ")
    print("A - adding student record: ")
    print("B - search student: ")
    print("C - edit student record: ")
    print("D - delete student record: ")
    print("E - print all record: ")
    print("F - export data: ")
    print("G - exit system: ")

    elite = input("enter here: ").lower().strip()

    if elite == 'a':
        os.system('cls')
        print("ADD STUDENT RECORD")
        student_id = input("Input student ID number: ")
        first_name = input("Input student First Name: ").upper()
        last_name = input("Input student last name: ").upper()
        course = input("Input student course: ").upper()
        section = input("Input student section: ").upper()
        gmail = input("Input student gmail: ")

        list_record[student_id] = [first_name, last_name, course, section, gmail ]
        print("DATA SAVED SUCCESSFULLY")
        
        continue

    elif elite == 'b':
        os.system('cls')
        print("SEARCH STUDENT")
        
        print("PRINTING STUDENT RECORD")
        print("-----------------------------")
        
        for id, info in list_record.items():
            print(f"STUDENT ID {id} - RECOND -{info}")
            
        continue

    elif elite == 'c':
        os.system('cls')
        print("EDIT STUDENT RECORD")
        
        search_id = input("INPUT STUDENT ID: ").lower()
        
        for each_student in list_record.keys():
            if search_id in list_record.keys():
                print(f"\n\nRECORD FOUND for {search_id}")
                print("----------------------")
                for id in list_record[search_id]:
                    print(f" --{id} ")
                    
                print("------------------------")
            else:
                print("NO RECORD FOUND")
            break
        continue

    elif elite == 'd':
        os.system('cls')
        print("DELETE STUDENT RECORD")
        
        search_id = input("INPUT RECORD ID: ").lower()
        
        for each_student in list_record.keys():
            if search_id in list_record.keys():
                print(f"\n\nRECORD FOUMD for {search_id}")
                print("-------------------------")
                for id in list_record[search_id]:
                    print(f" --{id} ")
                    
                print("----------------------")
                list_record.pop(search_id)
                print("RECORD DELETED")
            else:
                print("NO RECORD FOUND")
            break
        continue

    elif elite == 'e':
        os.system('cls')
        print("PRINT ALL RECORD")
        
        search_id = input("INPUT STUDENT ID: ").lower()
        
        for each_student in list_record.keys():
            if search_id in list_record.keys():
                print(f"\n\nRECOND FOUMD for {search_id}")
                print("-------------------------")
                for id in list_record[search_id]:
                    print(f" --{id} ")
                    
                print("----------------------")
                
                first_name = input("Input new student First Name: ").upper()
                last_name = input("Input new student last name: ").upper()
                course = input("Input new student course: ").upper()
                ection = input("Input new student section: ").upper()
                gmail = input("Input new student gmail: ")
                
                list_record[search_id][0] = first_name
                list_record[search_id][0] = last_name
                list_record[search_id][0] = course
                list_record[search_id][0] = section
                list_record[search_id][0] = gmail
                print("DATA UPDATED SUCCESSFULLY")
                
            else:
                print("NO UPDATED SUCCESSFULLY")
            break
        continue

    elif elite == 'f':
        print("EXPORT DATA")
        
        with open('list_record.json','w') as new_file:
            json.dump(list_record, new_file, indent=4)
            
        print("DATA EXPORTED SUCCESSFULLY")
        continue

    elif elite == 'g':
        print("EXIT SYSTEM")
        break
    else:
        print("Invalid Choice, Re-enter code ")
        continue
