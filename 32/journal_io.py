import os

FILENAME = 'journal.txt'

def load_journal_entry():
    """
    Loads journal entries
    :return: a list of previous journal entries
    """

    journal_data = []
    filename = get_full_pathname()

    if os.path.exists(filename):
        with open(filename, 'r') as fin:
            journal_data = fin.readlines()
            journal_data = [x.strip() for x in journal_data]  # clean up

        # list_journal_entry(journal_data)
        print('Finished loading journal')

    else:
        print('No previous journal found.')

    return journal_data


def save_journal_entry(journal_data):

    filename = get_full_pathname()

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')

        # fout.close()      Automatically done w/ with clause
        print('Finished saving journal')


def get_full_pathname():
    filename = os.path.abspath(os.path.join('./', FILENAME))
    return filename
