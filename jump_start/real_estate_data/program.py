# list comprehesnions
# generator expressions
# data pipelinswith generators
import csv
import os

try:
    import statistics
except:
    import statistics_standin_for_py2 as statistics

from jump_start.real_estate_data.data_types import Purchase


def main():
    print_header()
    filename = get_data_file()
    data = load_file(filename)
    query_data(data)


def print_header():
    print('-------------------------------')
    print('  REAL ESTATE DATA MINING APP')
    print('-------------------------------')


def get_data_file():
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv')


def load_file(filename):
    # TODO: python 2 try except block to handle encoding
    # with open(filename, 'r')
    with open(filename, 'r', encoding='utf-8') as fin:
        reader = csv.DictReader(fin)
        purchases = []
        for row in reader:
            p = Purchase.create_from_dict(row)
            purchases.append(p)

        # print(purchases[0].__dict__)
        return purchases


# def load_file_basic(filename):
#     with open(filename, 'r', encoding='utf-8') as fin:
#         header = fin.readline()
#         print('Header: ' + header)
#
#         lines = []
#         for line in fin:
#             line_data = line.split(',')
#             bed_count = line_data[4]
#             lines.append(line_data)
#         print(lines[:5])
#
#
# def get_price(p):
#     return p.price

def query_data(data):  #: list[Purchase]):
    # data.sort(key=get_price)
    data.sort(key=lambda p: p.price)
    high_purchase = data[-1]
    # print(high_purchase.price)

    low_purchase = data[0]
    # print(low_purchase.price)

    print("The most expensive house is ${:,} with {} beds and {} baths".format(high_purchase.price, high_purchase.beds,
                                                                               high_purchase.baths))
    print("The least expensive house is ${:,} with {} beds and {} baths".format(low_purchase.price, low_purchase.beds,
                                                                                low_purchase.baths))

    # prices = []
    # for pur in data:
    #     prices.append(pur.price)
    # avg_price = statistics.mean(prices)

    # replace loop with list comprehension
    # prices = [

    # generator expression yield behavior replace list[] with ()
    # will process minimum to return first 5 2-bedroom homes
    two_bed_homes = (
        # (p.price, p.beds, p.city)
        # p.price # projcection or items
        p
        for p in data  # set to process
        if p.beds == 2  # test / condition / where clause
        if announce(p, 's-bedrooms, found {}'.format(p.beds)) and p.beds == 2
    )

    homes = []
    for h in two_bed_homes:
        if len(homes) > 5:
            break
        homes.append(h)
    # print(prices)
    # return

    # avg_price = statistics.mean(prices)
    # avg_price = statistics.mean([p.price for p in data if p.beds == 2])
    # avg_price = statistics.mean([p.price for p in two_bed_homes])
    # avg_baths = statistics.mean([p.baths for p in two_bed_homes])
    # avg_sqft = statistics.mean([p.sq__ft for p in two_bed_homes])

    # print('Average 2-bedroom home is ${:,}, baths={}, sq ft={:,}'
    #       .format(int(avg_price), avg_baths, 0 ))#, avg_sqft))

    # replace[] with generator() expression computes only pulled items out of sequence
    # list comprehension pulls all items into memory
    avg_price = statistics.mean((announce(p.price, 'price') for p in homes))
    avg_baths = statistics.mean((p.baths for p in homes))
    # avg_sqft = statistics.mean([p.sq__ft for p in homes])

    prices = []
    for pur in data:
        if pur.beds == 2:
            prices.append(pur.price)
    avg_price = statistics.mean(prices)
    # print('Average 2 bedroom price is ${:,}'.format(int(avg_price)))

    # Data pipelines + generators
    three_bedrooms = (
        # (tx.price, tx.beds, tx.city)
        tx
        for tx in data
        if tx.beds == 3
    )
    print(three_bedrooms)
    nearby = (
        (tx.price, tx.beds, tx.city)
        for tx in three_bedrooms
        if tx.city == 'LINCOLN'
    )

    interesting = []
    for h in nearby:
        interesting.append(h)
    print(interesting)


def announce(item, msg):
    print("Processing item {} for {}".format(item, msg))
    return item


if __name__ == '__main__':
    main()
