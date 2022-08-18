import sqlite3
from datetime import datetime
from functionality import Functionality


def default_date():
    now = datetime.now()
    return datetime.strftime(now, "%Y-%m-%d")


def main():
    flag = True
    choice = ''
    func = Functionality(db)
    func.create_table()
    print("Hello!")
    login = input("Enter your login: ").strip()
    func.identify_user(login)
    action = input("Choose action, please: (add, get stat, clear, d/m/y, awd) ").lower().strip()

    if action == "add":
        func.add_expense(user=login, date=default_date())

    elif action == "get stat":
        func.get_stat()
    elif action == "clear":
        func.clear_data()
    elif action == "d/m/y":
        while flag:
            choice = input("Please, enter 'day', 'month' or 'year' to get statistics: ").lower().strip()
            if choice == 'day' or choice == 'month' or choice == 'year':
                flag = False

        func.d_m_y_stat(choice)
    elif action == "awd":
        func.add_with_date(user=login)
    else:
        print("Incorrect command. Please, try again.")
        main()


if __name__ == '__main__':
    db = sqlite3.connect("cost-control.db")
    main()
    db.close()
