import random
from collections import Counter
from collections import namedtuple
from datetime import date
from time import perf_counter

import numpy as np
from faker import Faker


def data_analysis_using_tuples():
    """
    Use Faker library to get 10000 random profiles. Using namedtuple, calculate the largest blood type,
    mean-current_location, oldest_person_age and average age (add proper doc-strings)
    :return: None
    """
    fake = Faker()
    Profile = namedtuple('Profile', fake.profile().keys())
    data = [Profile(**fake.profile()) for _ in range(10000)]

    start_time = perf_counter()
    blood_group_count = dict(Counter([x.blood_group for x in data]))
    print('\nBlood group distribution: ', blood_group_count)
    result = max(blood_group_count, key=blood_group_count.get)
    end_time = perf_counter()
    print(f'The most frequent blood group is: {result}')
    print(f'Finding the most frequent blood_group took {end_time - start_time} sec')

    print('\nDetermining mean current location')
    start_time = perf_counter()
    current_locations = [x.current_location for x in data]
    result = np.mean(current_locations, axis=0)
    end_time = perf_counter()
    print(f'Mean location is: {result}')
    print(f'Finding mean location took {end_time - start_time} sec')

    print('\nDetermining mean and max age in days')
    start_time = perf_counter()
    age = [(date.today() - x.birthdate).days for x in data]
    result1 = np.mean(age)
    result2 = np.max(age)
    end_time = perf_counter()
    print(f'Mean age is: {result1} days')
    print(f'Max age is: {result2} days')
    print(f'Determining mean and max age took {end_time - start_time} sec')


def data_analysis_using_dict():
    """
    Do the same thing above using a dictionary. Prove that namedtuple is faster
    :return: None
    """
    fake = Faker()
    data = [fake.profile() for _ in range(10000)]

    start_time = perf_counter()
    blood_group_count = dict(Counter([x['blood_group'] for x in data]))
    print('\nBlood group distribution: ', blood_group_count)
    max_bg = max(blood_group_count, key=blood_group_count.get)
    end_time = perf_counter()
    print(f'The most frequent blood group is: {max_bg}')
    print(f'Finding the most frequent blood_group took {end_time - start_time} sec')

    print('\nDetermining mean current location')
    start_time = perf_counter()
    current_locations = [x['current_location'] for x in data]
    result = np.mean(current_locations, axis=0)
    end_time = perf_counter()
    print(f'Mean location is: {result}')
    print(f'Finding mean location took {end_time - start_time} sec')

    print('\nDetermining mean and max age in days')
    start_time = perf_counter()
    age = [(date.today() - x['birthdate']).days for x in data]
    result1 = np.mean(age)
    result2 = np.max(age)
    end_time = perf_counter()
    print(f'Mean age is: {result1} days')
    print(f'Max age is: {result2} days')
    print(f'Determining mean and max age took {end_time - start_time} sec')


def imaginary_stock_exchange():
    """
    Create a fake data (you can use Faker for company names) for imaginary stock exchange for top 100 companies
    (name, symbol, open, high, close). Assign a random weight to all the companies. Calculate and show what value
    stock market started at, what was the highest value during the day and where did it end. Make sure your
    open, high, close are not totally random. You can only use namedtuple.
    :return: None
    """
    fake = Faker()
    StockExchangeRecord = namedtuple('StockExchangeRecord', 'name symbol, open, high, close')

    # Creating 100 random companies, with unique company code (three non-whitespace characters)
    StocksSnapshot = namedtuple('StocksSnapshot', ['company' + str(x) for x in range(100)])
    company_symbols = set()
    companies = []
    while len(company_symbols) != 100:
        profile = fake.profile()
        symbol = profile['name'][:3].upper()
        if symbol not in company_symbols and len(symbol.strip()) == 3:
            name = profile['name']
            open_val = random.uniform(25, 600)
            high_val = open_val * random.uniform(1, 1.25)
            close_val = high_val * random.uniform(0.6, 0.99)
            companies.append(StockExchangeRecord(name, symbol, open_val, high_val, close_val))
            company_symbols.add(symbol)

    todays_stock = StocksSnapshot(*companies)
    company_weights = np.random.uniform(low=0.25, high=1.25, size=100)
    starting_stock_price = np.dot(company_weights, [x.open for x in todays_stock])
    high_stock_price = np.dot(company_weights, [x.high for x in todays_stock])
    close_stock_price = np.dot(company_weights, [x.close for x in todays_stock])

    print(f'Starting StockMarket Index : {starting_stock_price}')
    print(f'Day-high StockMarket Index : {high_stock_price}')
    print(f'Closing StockMarket Index : {close_stock_price}')
