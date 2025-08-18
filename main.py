from data_module import *
def main_menu():
    print("=== Data Viewer Interface ===")
    while True:
        print("\n1. View dataset")
        print("2. View visualisation")
        print("3. Search or filter data")
        print("4. Exit program")

        choice = input("\nSelect an option (1-4): ")

        if choice == "1":
            display_dataset()
        elif choice == "2":
            pass
        elif choice == "3":
            pass
        elif choice == "4":
            print("\nExiting program...")
            break
        else:
            print("\nInvalid input. Please input a number 1-4.")

if __name__ == "__main__":
    main_menu()