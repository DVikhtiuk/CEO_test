from datetime import datetime, timedelta


class Functionality:
    def __init__(self, connection):
        self.db = connection
        self.cursor = connection.cursor()

    def create_table(self):
        cursor = self.db.cursor()
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS costs (User, Date, Category, Expense )")
        self.db.commit()

    @staticmethod
    def identify_user(login):
        try:
            with open("users.txt", mode='r') as f:
                users = f.readlines()
                list_of_users = [user.strip() for user in users]
            if login in list_of_users:
                print(f"Welcome back, {login}")
            else:
                with open("users.txt", mode='a') as f:
                    f.write(f"{login}\n")
                print(f"New user is registered - {login}")

        except FileNotFoundError:
            with open("users.txt", mode='w') as f:
                f.write(f"{login}\n")
            print(f"New user is registered - {login}")

    def add_expense(self, user, date):
        flag = True
        add_category = ''
        while flag:
            add_category = input("Category can't be empty or be a number. Insert category: ").lower().strip()
            if add_category != '' and not self.check_float(add_category):
                flag = False
        add_expense = input("Insert expense: ").strip()
        if self.check_float(add_expense):
            self.cursor.execute("INSERT INTO costs VALUES(?, ?, ?, ?)", (user, date, add_category,
                                                                         add_expense.replace("-", "")))
            self.db.commit()
            print(f"Thank You! Expense '{add_expense.replace('-', '')}' was added by category \
'{add_category}'")
        else:
            print("Invalid value for expense. Try again. P.S. '.' for real numbers.")
            self.add_expense(user, date)

    def get_stat(self):
        get_category = input("If you want to get statistics for all categories, insert 'all'.\
Insert category: ").lower().strip()
        if get_category != "all":
            get_stat_list = self.cursor.execute("SELECT SUM(Expense) FROM costs WHERE Category == ?",
                                                (get_category,)).fetchone()
            if get_stat_list[0] is None:
                result = '0'
            else:
                result = get_stat_list[0]
            print(f"Expenses: {result} hrn.")
        elif get_category == "all":
            uniq_categories_list = []
            all_categories = self.cursor.execute("SELECT Category FROM costs ").fetchall()
            for elem in all_categories:
                if elem[0] not in uniq_categories_list:
                    uniq_categories_list.append(elem[0])
            for category in uniq_categories_list:
                get_stat_list = self.cursor.execute("SELECT SUM(Expense) FROM costs WHERE Category == ?",
                                                    (category,)).fetchone()

                print(f"Category: {category}, Expenses: {get_stat_list[0]} hrn.")
            print("---------------------------------")
            all_expenses = self.cursor.execute("SELECT SUM(Expense) FROM costs").fetchone()
            if all_expenses[0] is None:
                result = '0'
            else:
                result = all_expenses[0]
            print(f"All Expenses: {result} hrn.")

    def clear_data(self):
        self.cursor.execute("DELETE FROM costs")
        self.db.commit()
        with open("users.txt", mode='w'):
            pass
        print("All data is deleted. Thank You!")

    def d_m_y_stat(self, choice):
        if choice == "day":
            day = input("insert the day in format 'y-m-d': ").strip()
            if self.check_date(day):
                stat_list = self.cursor.execute("SELECT SUM(Expense) FROM costs WHERE Date == ?", (day,)).fetchone()
                if stat_list[0] is None:
                    result = '0'
                else:
                    result = stat_list[0]
                print(f"Expense for {day}: {result} hrn.")

            else:
                print("Invalid date. Please, try again.")
                self.d_m_y_stat(choice)
        elif choice == "month":

            day = input("Choose the start-count day (in format 'y-m-d'): ").strip()
            if self.check_date(day):
                start = datetime.strptime(day, '%Y-%m-%d')
                delta = timedelta(30)
                end = start + delta

                month_after_date = datetime.strftime(end, '%Y-%m-%d')
                uniq_categories_list = []
                all_categories = self.cursor.execute("SELECT Category FROM costs WHERE Date \
                            BETWEEN '{}' AND '{}'".format(day, month_after_date)).fetchall()
                for elem in all_categories:
                    if elem[0] not in uniq_categories_list:
                        uniq_categories_list.append(elem[0])
                for category in uniq_categories_list:
                    get_stat_list = self.cursor.execute("SELECT SUM(Expense) FROM costs WHERE Category == ? AND Date \
                BETWEEN '{}' AND '{}'".format(day, month_after_date),
                                                        (category,)).fetchone()

                    print(f"Category: {category}, Expenses: {get_stat_list[0]} hrn.")
                print("---------------------------------")
                stat_list = self.cursor.execute("SELECT SUM(Expense) FROM costs WHERE Date \
                BETWEEN '{}' AND '{}'".format(day, month_after_date)).fetchone()
                if stat_list[0] is None:
                    result = '0'
                else:
                    result = stat_list[0]
                print(f"All expenses between {day} and {month_after_date}: {result} hrn.")
            else:
                print("Invalid date. Please, try again.")
                self.d_m_y_stat(choice)
        else:
            day = input("Choose the start-count day (in format 'y-m-d'): ").strip()
            if self.check_date(day):
                start = datetime.strptime(day, '%Y-%m-%d')
                dell = timedelta(365)
                end = start + dell
                year_after_date = datetime.strftime(end, '%Y-%m-%d')
                uniq_categories_list = []
                all_categories = self.cursor.execute("SELECT Category FROM costs WHERE Date \
                                        BETWEEN '{}' AND '{}'".format(day, year_after_date)).fetchall()
                for elem in all_categories:
                    if elem[0] not in uniq_categories_list:
                        uniq_categories_list.append(elem[0])
                for category in uniq_categories_list:
                    get_stat_list = self.cursor.execute("SELECT SUM(Expense) FROM costs WHERE Category == ? AND Date \
                                BETWEEN '{}' AND '{}'".format(day, year_after_date),
                                                        (category,)).fetchone()

                    print(f"Category: {category}, Expenses: {get_stat_list[0]} hrn.")
                print("---------------------------------")
                stat_list = self.cursor.execute("SELECT SUM(Expense) FROM costs WHERE Date \
                            BETWEEN '{}' AND '{}'".format(day, year_after_date)).fetchone()
                if stat_list[0] is None:
                    result = '0'
                else:
                    result = stat_list[0]
                print(f"All expenses between {day} and {year_after_date}: {result} hrn.")
            else:
                print("Invalid  date. Please, try again.")
                self.d_m_y_stat(choice)

    def add_with_date(self, user):
        add_date = input("insert date in format y-m-d: ").strip()
        if self.check_date(add_date):
            flag = True
            add_category = ''
            while flag:
                add_category = input("Category cannot be empty or be a number. Insert category: ").lower().strip()
                if add_category != '' and not self.check_float(add_category):
                    flag = False
            add_expense = input("Insert expense: ").strip()
            if self.check_float(add_expense):
                self.cursor.execute("INSERT INTO costs VALUES(?,?, ?, ?)", (user, add_date, add_category,
                                                                            add_expense.replace("-", "")))
                self.db.commit()
                print(f"Thank You! Expense '{add_expense.replace('-', '')}' was added by \
category '{add_category}' with date '{add_date}'")
            else:
                print("Incorrect value for expense. Please, try again")
                self.add_with_date(user)
        else:
            print("invalid date. Try again")
            self.add_with_date(user)

    @staticmethod
    def check_float(inp):
        try:
            float(inp)
            return True
        except ValueError:
            return False

    @staticmethod
    def check_date(date):
        try:
            datetime.strptime(date, '%Y-%m-%d')
            return True
        except ValueError:
            return False
