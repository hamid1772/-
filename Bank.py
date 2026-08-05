import json

try:
    with open("contacts.json", "r") as file:
        con = json.load(file)
except FileNotFoundError:
    con = []


def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(con, file)


def add_contact():
    account_number = input("what is your account_number: ")

    a = {
        "name": input("what is your name: "),
        "phone": input("what is your phone: "),
        "account_number": account_number,
        "balance": int(input("enter balance: "))
    }

    found = False

    for x in con:
        if account_number == x["account_number"]:
            found = True
            break

    if found:
        print("شماره حساب تکراری است")
    else:
        con.append(a)
        save_contacts()
        print("حساب اضافه شد")


def show_contact():
    for account in con:
        print(account)


def search_contact():
    newlist = []
    t = input("what is your name: ")

    for x in con:
        if t == x["name"]:
            newlist.append(x)

    if len(newlist) == 0:
        print("کاربر پیدا نشد")
    else:
        print(newlist)


def delete_contact():
    d = input("what is your name is delete: ")

    for x in con:
        if d == x["name"]:
            con.remove(x)
            save_contacts()
            print("انجام شد")
            print(con)
            break


def edit_contact():
    name = input("what is your name: ")

    for x in con:
        if name == x["name"]:
            phone = input("what is your new phone: ")
            account_number = input("what is your new account_number: ")
            balance = int(input("what is your new balance: "))

            x["phone"] = phone
            x["account_number"] = account_number
            x["balance"] = balance

            save_contacts()

            print("ویرایش انجام شد")
            break


def deposit():
    account_number = input("Enter account number: ")
    amount = int(input("Enter amount: "))

    for x in con:
        if account_number == x["account_number"]:
            if amount <= 0:
                print("مبلغ باید بزرگ‌تر از صفر باشد")
                return

            x["balance"] += amount
            save_contacts()

            print("واریز انجام شد")
            print("موجودی جدید:", x["balance"])
            return

    print("حساب یافت نشد")


def withdraw():
    source = None

    account_number = input("Enter account number: ")
    amount = int(input("Enter amount: "))

    for x in con:
        if account_number == x["account_number"]:
            source = x
            break

    if source is not None:

        if amount <= 0:
            print("مبلغ باید بزرگ‌تر از صفر باشد")
            return

        if source["balance"] < amount:
            print("مبلغ برداشت بیشتر از موجودی است")
            return

        source["balance"] -= amount
        save_contacts()

        print("برداشت انجام شد")
        print("موجودی جدید:", source["balance"])

    else:
        print("حساب یافت نشد")


def transfer():
    source = None
    destination = None

    account_number_mabdah = input("Enter source account: ")
    account_number_maghsad = input("Enter destination account: ")
    amount = int(input("Enter amount: "))

    if account_number_mabdah == account_number_maghsad:
        print("حساب مبدأ و مقصد نباید یکسان باشند")
        return

    for x in con:
        if account_number_mabdah == x["account_number"]:
            source = x
            break

    for x in con:
        if account_number_maghsad == x["account_number"]:
            destination = x
            break

    if source is None:
        print("حساب مبدأ پیدا نشد")
        return

    if destination is None:
        print("حساب مقصد پیدا نشد")
        return

    if amount <= 0:
        print("مبلغ باید بزرگ‌تر از صفر باشد")
        return

    if source["balance"] < amount:
        print("موجودی کافی نیست")
        return

    source["balance"] -= amount
    destination["balance"] += amount

    save_contacts()

    print("انتقال با موفقیت انجام شد")
    print("موجودی جدید:", source["balance"])


while True:
    input_1 = int(input("""
1. افزودن حساب
2. نمایش حساب
3. جستجوی حساب
4. حذف حساب
5. ویرایش حساب
6. خروج
7. انتقال وجه
8. برداشت وجه
9. واریز وجه
"""))

    if input_1 == 6:
        break
    elif input_1 == 1:
        add_contact()
    elif input_1 == 2:
        show_contact()
    elif input_1 == 3:
        search_contact()
    elif input_1 == 4:
        delete_contact()
    elif input_1 == 5:
        edit_contact()
    elif input_1 == 7:
        transfer()
    elif input_1 == 8:
        withdraw()
    elif input_1 == 9:
        deposit()
