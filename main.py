# import sys
# sys.path.append("./show_main_menu")
# sys.path.append("/arithmetic_handler")
from menus.menu import show_main_menu
from basic.basic_handler import arithmetic_handler
from algebra.algebra_handler  import algebra_handler


def main():
    while True:
        show_main_menu()
        choice = input("Enter your option number: ")
        if choice == "1":
            arithmetic_handler()
        elif choice == "2":
            algebra_handler()
        elif choice == "3":
            print("\nNew Features in Progress...")
        elif choice == "4":
            print("\nNew Features in Progress...")
        else:
            print("Invalid choice, try again")
if __name__ == "__main__":
    main()
            
