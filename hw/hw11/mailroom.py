donors = [
    ('Homer', [25, 10, 20]),
    ('Marge', [100, 50, 75]),
    ('Bart', [5, 1, 2]),
    ('Lisa', [5, 10, 12, 6])]


def mailroom():
    print("Welcome to Mailroom Madness\nChoose from the following:")

    user_input = input("T - send a (T)hank You   R - create a (R)eport \nquit - Quit\
 the program \n")
    if user_input == 't':
            thanks()
    elif user_input == 'r':
            report()
    elif user_input == 'quit':
            return


def thanks():
    """Request prompt for name of donor. """
    donor_names = []  # list to sort through names in nested donors list
    user_input = input("\nPlease enter a name, or choose from the following: \nlist - Pr\
int a list of previous donors   quit - Return to main menu \n")

    for (names, donations) in donors:
        donor_names.append(names)
        """Adds names from 'donors' list to new list called 'donor_names'."""

    if user_input == 'list':
        for (names, donations) in donors:
            print(names, end=" ")
        thanks()
    elif user_input == 'quit':
        mailroom()
    elif user_input in donor_names:
        donation_amount(user_input)
    else:
        donors.append((user_input,[]))
        donation_amount(user_input)


def donation_amount(name):
    """Prompt for donation amount and update donor list and amount"""

    for (name, donations) in donors:
        donor_amount = donors[:]
    donation = input("Please enter a donation amount or 'quit':")
    if donation == "quit":
        return
    try:
        donation = int(donation)
        if int(donation) > 0:
            count = 0

            for list in donors:
                if list[0] == name:
                    donors[count][1].append(donation)
                count += 1

            print("\nDear " + name + ",\n\nThank you so much for your kind donation of $"\
+ str(donation) + ". We here at the Foundation for the Needy greatly appreciate it\
. Your money will go towards helping the needy.\n\nThanks again, \n\nJohn\nDire\
ctor, H.T.N.")
            mailroom()
    except ValueError:
            print("Not a valid entry.")
            donation_amount(name)


def report():

    print("Name "   "|" "Total" "|" "#" "|" "Average\n"
"___________________________________________\n")
    print(get_name() + total_donated())


def get_name():
    for (names, donations) in donors:
        print(names)


def total_donated():
    count = 0
    total = 0

    for list in donors:
        donations = donors[count][1]
        count += 1
        total = sum(donations)
    print (total)

def times_donated():


def avg_donation():


if __name__ == "__main__":