from company import add_company,show

def menu():
    while True:

        print("1: Add Company")
        print("2: Show Company")
        choice = input("Enter Choice")

        if choice == "1":
            name=input("enter company name: ")
            add_company(name)

        elif choice == "2":
            show()