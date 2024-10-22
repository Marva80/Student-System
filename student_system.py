students = [
    {"name": "Tobias Fors", "email": "tobias.fors@yh.nackademin.se", "age": 30,  "student_id": 11230, "grades": {"Pythonprogrammering 1": 1, "Databasteknik": 4}},
    {"name": "Karin Börjell", "email": "karin.borjell@yh.nackademin.se", "age": 32,  "student_id": 11231, "grades": {"Pythonprogrammering 1": 1, "Pythonprogrammering 2": 3}},
    {"name": "Daniel Eliasson", "age": 29,  "email": "daniel.eliasson@yh.nackademin.se", "student_id": 11233, "grades": {"Pythonprogrammering 1": 1, "Affärsmannaskap": 2}},
    {"name": "Magdalena Andersson", "age": 50,  "email": "magdalena.andersson@yh.nackademin.se", "student_id": 11234, "grades": {"Pythonprogrammering 1": 1, "Webbramverk inom python": 5}},
]

def main_menu():
    while True:
        choice = (input("""
            Welcome to the greatest student system in the world.
            What would you like to do?
            \tq. Close 
            \t0. List all students with namne and student-id.
            \t1. Add a student with studentID and namne
            \t2. Remove a student
                        
            Enter your choice here : """))
        if choice not in ["q","0","1","2"]:
            print("Invalid choice")
        
        if choice == "q":
            break
        elif choice =="0":
            Students_menu()
        elif choice == "1":
            ny_student = {"name": "Maryam Marzban", "email": "marmar@gmail.com", "age": 40, "student_id": 11235, "grades": {"Pythonprogrammering 1": 1, "Databasteknik": 4}}
            add_student(students=students, ny_student=ny_student)
            print("new student added to list")
        elif choice == "2":
            name = input("Which student do you want to remove from the list? ")
            name = name.capitalize()
            try:
                remove_student(students=students,name=name)
            except ValueError as e:
                print(e)


def add_student(students:list[dict], ny_student:str):
    students.append(ny_student)

def remove_student(students:list[dict], name:str):
    for s in students:
        if s["name"] == name:
            students.remove(s)
            print(f"The student{name} is removed")
    raise ValueError(f"The student{name} doesn't exists in the dictionary ")

def student_info(students:list[dict], name:str):
    while True:
        print(f"\t\tWelcome {name}, What would you like to do?")
        choice = (input("""
                [q]. Go back
                [0]. Show summary of grades
                [1]. List personal information
                
                Enter your choice: """) )
        if choice not in["q","0","1","2","3"]:
            print("Invalid choice")
        if choice == "q":
            Students_menu()
        elif choice == "0":
            summery_list = []
            print(f"\t\tSummary of grades for {name}")
            for s in students:
                if s["name"] == name:
                        #summery_list.append(s["grades"])
                        print(f"\t\t{s['grades']}")
                        input("\t\tPress enter to continue")
        
        elif choice == "1":
            list_student_info(students=students,name=name)
            input("\t\tPress enter to continue")

def list_students(students:list[dict]):
    
        #i =0
        for i,value in enumerate(students):
            
            print(f"\t\t[{i}] ID: {value['student_id']} - {value['name']}")
            #i=i+1

def Students_menu():
    
    while True:
            print("\t\tChoose a student or go back to the previous menu: ")
            print(" \t\t[q]. Go back")
            list_students(students=students)
            choice = input("\t\tEnter your choice: ")
            if choice not in["q","0","1","2","3"]:
                print("Invalid choice")
            if choice == "q":
                main_menu()
           
            else:
                choice = int(choice)
                #for index,value in enumerate(students):
                if 0<= choice < len(students):
                        name = students[choice]['name']
                        
                student_info(students=students, name=name)
            
def list_student_info(students:list[dict],name:str):
    for key,value in enumerate(students):
         if value["name"] == name:
              print(f"\n\t\tName: {name}\n \t\tID: {value['student_id']}\n \t\tEmail: {value['email']}\n\t\tAge: {value['age']}")
        
         

if __name__ == "__main__":
    main_menu()
