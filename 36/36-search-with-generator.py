import os
import collections

SearchResult = collections.namedtuple('SearchResult', 'file, line, text')

def main():

    print_header()

    folder = get_folder_name()
    if not folder:
        print("Error w/ search location")
        return

    text = get_search_text()
    if not folder:
        print("Can't search empty text")
        return

    matches = search_folder(folder, text)
    match_count = 0
    for match in matches:
        match_count += 1
        print('----------------------------------')
        print('file:  ' + match.file)
        print('line:  {}'.format(match.line))
        print('match: ' + match.text.strip())
        print()

    print()
    print('Matches found: {:,}'.format(match_count))

def print_header():
    print('---------------------------')
    print('     Text Search APP')
    print('---------------------------')
    print()


def get_folder_name():
    folder_name = input('Enter a directory to search: ')

    if not folder_name or not folder_name.strip():
        return None

    if not os.path.isdir(folder_name):
        return None

    return os.path.abspath(folder_name)


def get_search_text():
    search_text = input('Enter a text to search for: ')

    return search_text.lower()


def search_folder(folder, text):
    print('Searching for {} in {} folder.'.format(text, folder))

    # all_matches = []

    items = os.listdir(folder)

    for item in items:
        full_item = os.path.join(folder, item)

        if os.path.isdir(full_item):
            # matches = search_folder(full_item,text)
            # if matches:
                # all_matches.extend(matches)

                # for m in matches:
                #     yield m

                # yield from matches

            # OR
            yield from search_folder(full_item, text)

        else:
            # matches = search_file( full_item, text )

            # if matches:
                # all_matches.extend(matches)

                # for m in matches:
                #     yield m

            yield from search_file(full_item, text)

    # return all_matches


def search_file(filename, search_text):

    # matches = []
    if filename.find('.png') < 0 and filename.find('.pyc') < 0:

        print('Searching {} in {}'.format(search_text, filename))
        with open(filename, 'r', encoding='utf-8') as fin:

            line_num = 0

            for line in fin:
                line_num += 1

                if line.lower().find(search_text) >= 0:
                    m = SearchResult(text=line, file=filename, line=line_num)
                    # matches.append(match)
                    yield m

    # return matches


if __name__ == '__main__':
    main()
