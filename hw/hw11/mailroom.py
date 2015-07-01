donors = {
    'Homer': [25, 10, 20],
    'Marge': [100, 50, 75],
    'Bart': [5, 1, 2],
    'Lisa': [5, 10, 12, 6]}


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
    user_input = input("\nPlease enter a name, or choose from the following: \nlist - Pr\
int a list of previous donors   quit - Return to main menu \n")

    if user_input == 'list':
        for key in donors:
            print(key,)
        thanks()
    elif user_input == 'quit':
        mailroom()
    elif user_input in donors:
        donation_amount(user_input)
    else:
        donors[user_input] = donation_amount(user_input)


def donation_amount(name):
    """Prompt for donation amount and update donor list and amount"""

    donation = input("Please enter a donation amount or 'quit':")
    if donation == "quit":
        return
    try:
        donation = int(donation)
        if int(donation) > 0:
            donors[name] = [donation]
            print(donors)

            print("\nDear " + name + ",\n\nThank you so much for your kind \
donation of $" + str(donation) + ". We here at the Foundation for \
the Needy greatly appreciate it. Your money will go towards hel\
ping the needy.\n\nThanks again, \n\nThe Needy\n")

            mailroom()
    except ValueError:
            print("Not a valid entry.")
            donation_amount(name)


def report():
    print("Name\t\t" "|" "Total\t" "|" "#" "|"  "  Average\t "
          "\n""_____________________________________________\n")

    for (names, donations) in donors.items():
        name = names
        total_donated = sum(donations)
        times_donated = len(donations)
        avg_donation = total_donated / times_donated

        print("%s\t\t | %i \t | %i | %i" % (name, total_donated, times_donated,
              avg_donation))

if __name__ == "__main__":
    mailroom()
