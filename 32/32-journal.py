import journal_io as jio
def print_header():

    print('---------------------------')
    print('       Journal APP')
    print('---------------------------')
    print()


def get_menu_option():
    selection = input('What do you want to do? [L]ist [A]dd E[x]it ')
    return selection


def list_journal_entry(journal_data):

    print('Your', len(journal_data), 'journal entries')

    newest_first = reversed(journal_data)
    for i, entry in enumerate(newest_first):
        print(i+1, ':', entry)
    print()


def add_journal_entry(journal_data):

    new_entry = input('Enter a new journal entry:\n')
    journal_data.append(new_entry)
    list_journal_entry(journal_data)


def run_loop():

    selection = get_menu_option()
    selection = selection.lower().strip()

    journal_data = jio.load_journal_entry()
    # journal_data = []

    while (selection != 'x'):
        if selection == 'a':
            print('Add Entry\n')
            add_journal_entry(journal_data)

        elif selection == 'l':
            print('List Entries\n')
            list_journal_entry(journal_data)

        selection = get_menu_option()

    jio.save_journal_entry(journal_data)
    print('Exiting\n')


def main():

    print_header()
    run_loop()


if __name__ == '__main__':
    main()



