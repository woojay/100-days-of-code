import csv
import os

#py 2 remedy
try:
    import statistics
except:
    print('error')
    import statistics_standin_for_py2 as statistics

from data_types import Purchase

def main():
    print_header()
    data_file = get_data_file()
    data = load_file(data_file)
    query_data(data)


def query_data(data):

    # sort by price
    # print(type(data))
    data.sort(key = lambda p: p.price)

    # highest price
    highest = data[-1]
    print('The most expensive house is {:,} with {} beds and {} baths'
          .format(highest.price, highest.beds, highest.baths))

    #lowest price
    lowest = data[0]
    print('The most expensive house is {:,} with {} beds and {} baths'
          .format(lowest.price, lowest.beds, lowest.baths))

    #average house price
    # prices = []
    # for item in data:
    #     prices.append(item.price)

    # List w/ generator
    prices = [
        p.price         # projection or items
        for p in data   # The set to process
    ]

    avg_price = statistics.mean(prices)
    print('The average home price is ${:,}'.format(int(avg_price)))

    # List w/ generator expression
    # average price of 2 bedroom houses
    two_bed_homes = (
        p               # projection
        for p in data   # source data set
        # if p.beds == 2  # test condition
        if announce(p, '2-beds, found {}'.format(p.beds)) and p.beds==2 # new test
    )

    homes=[]
    for home in two_bed_homes:
        # if len(homes) > 5:
        #     break
        homes.append(home)

    # List comprehension
    avg_2_beds_price = statistics.mean((announce(p.price, 'price') for p in homes))
    avg_2_beds_baths = statistics.mean((p.baths for p in homes))
    avg_2_beds_sqrt  = statistics.mean((p.sq__ft for p in homes))

    print('The average price of two bedroom home is ${:,}, baths={:.1f}, sq ft={:,.0f}'
          .format(int(avg_2_beds_price), avg_2_beds_baths, avg_2_beds_sqrt))

def announce(item, msg):
    # print('Pulling item {} for {}'.format(item, msg))
    return item


def load_file(data_file):
    # with open(data_file, 'r', encoding='utf-8') as fin:
    with open(data_file, 'r') as fin:
        reader = csv.DictReader(fin)
        purchases = []

        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        # print(purchases[0].__dict__)

        # # Header Row
        # header = fin.readline().strip()
        # # Data Rows
        # reader = csv.reader(fin, delimiter=',')
        # for row in reader:
        #     print(row)
        #     print("Bed count: {}".format(row['beds']))

    return purchases


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data.csv')


def print_header():
    print('---------------------------')
    print('Real Estate Data Mining APP')
    print('---------------------------')
    print()


if __name__ == '__main__':
    main()