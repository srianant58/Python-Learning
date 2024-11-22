import json

def add_person():
    name = input("Name :")
    age = input("Age :")
    email = input("Email :")    

    person = {'name':name , 'age':age ,'email':email}

    return person

def display_person(people):
    for i,person in enumerate(people):
        print(f'{i+1} | {person["name"]} | {person["age"]} | {person["email"]}')

def delete_person(people):
    display_person(people)
    
    while True:
        number = input("Enter the Number to delete: ")
        try:
            number = int(number)

            if number <=0 or number > len(people):
                print("Invalid Number, Out of range")
            else:
                break
        except:
            print("Invalid Number")
    
    people.pop(number-1)
    print("Person Deleted")


def search_person(people):
    search_name = input("Enter the name to search: ").lower()
    result=[]

    for person in people:
        name = person["name"]
        if search_name in name:
            result.append(person)

    display_person(result)

print("Hi, Welcome to the Contact Management System")
print()

with open("contacts.json","r") as f:
    people = json.load(f)["contacts"]

while True:
    print()
    print(f"Contact List Size : {len(people)}")
    command = input("You can 'Add','Delete', \"Search' or 'Q' for Quit: ").lower()

    if command == "add":
        person = add_person()
        people.append(person)
        print("Person Added")
    elif command == "delete":
        delete_person(people)
    elif command == "search":
        search_person(people)
    elif command == 'q':
        break
    else:
        print("Invalid Command")

with open("contacts.json","w") as f:
    json.dump({"contacts":people},f)
# print(people)
