import pymongo

# Establish a connection to MongoDB
client = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
db = client["mydatabase"]
collection = db["employee"]

def create_record():
        emp_id = input("Enter EMPLOYEE_ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        address = input("Enter Address: ")
        designation = input("Enter Designstion: ")
        record = {"emp_id": emp_id, "name": name, "age": age, "address": address, "designation":designation}
        collection.insert_one(record)
        print("Record created successfully!")

def read_records():
        for record in collection.find():
            print(record)
        # for record in collection.find():
                # if 'emp_id' in record:
                        # emp_id = record['emp_id']
                # else:
                        # emp_id = "N/A"
# 
                # if 'name' in record:
                        # name = record['name']
                # else:
                        # name = "N/A"
# 
                # if 'age' in record:
                        # age = record['age']
                # else:
                        # age = "N/A"
# 
                # if 'address' in record:
                        # address = record['address']
                # else:
                        # address = "N/A"
# 
                # if 'designation' in record:
                        # designation = record['designation']
                # 
                # else:
                        # designation = "N/A"
# 
                # print(f"EMP_ID: {emp_id}, Name: {name}, Age: {age}, Address: {address}, Designation: {designation}")

def update_record():
        emp_to_update= input("Enter the Employee Id to update: ")
        print("\t")
        while True:
                print("\nSelect the Field to update:")
                print("1. Employee ID")
                print("2. name")
                print("3. age")
                print("4. address")
                print("5. designation")
                print("6. Exit")

                choice = input("Enter your choice: ")

                if choice == "1":
                        new_emp_id = input("Enter the new employee id: ")
                        collection.update_one({"emp_id": emp_to_update}, {"$set": {"emp_id": new_emp_id}})
                elif choice == "2":
                        new_name = input("Enter the new Name: ")
                        collection.update_one({"emp_id": emp_to_update}, {"$set": {"name": new_name}})

                elif choice == "3":
                        new_age = input("Enter the new Age: ")
                        collection.update_one({"usn": emp_to_update}, {"$set": {"age": new_age}})

                elif choice == "4":
                        new_address = input("Enter the new Address: ")
                        collection.update_one({"usn": emp_to_update}, {"$set": {"address": new_address}})

                elif choice == "5":
                        new_desig = input("Enter the new Designation: ")
                        collection.update_one({"emp_id": emp_to_update}, {"$set": {"designation": new_desig}})

                elif choice == "6":
                        break
                else:
                        print("Invalid choice")
        print("Successfully Updated")
def delete_record():
        emp_to_delete = input("Enter the Employee id to delete: ")
        collection.delete_one({"emp_id": emp_to_delete})
        print("Record deleted successfully!")

while True:
        print("\nMenu:")
        print("1. Create Record")
        print("2. Read Records")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
                create_record()
        elif choice == "2":
                read_records()
        elif choice == "3":
                update_record()
        elif choice == "4":
                delete_record()
        elif choice == "5":
                break
        else:
                print("Invalid choice.")
