import csv
import json
from utils import read_file, print_trade_details, append_to_trading_data, add_or_reduce_stocks
from badrequest import BadRequest
from validators import format_date, buy_or_sell, test_stock_details, test_valid_file_name_and_extension
from constants import errors, success_messages, input_messages

def load_trading_data(trading_data):
    flag = 0
    while flag != 1:
        try:
            file = read_file()
            csvreader = csv.reader(file)
            for ticker, flag, quantity, cost, date_of_trade in csvreader:
                append_to_trading_data(trading_data, [
                    format_date(date_of_trade), ticker,
                    buy_or_sell(flag),
                    test_stock_details(quantity, int),
                    test_stock_details(cost, float)
                ])
            print(trading_data)
            flag = 1
        except FileNotFoundError:
            print(errors["invalid_filename"])
        except BadRequest as Error:
            print(Error)


def load_stock_prices(stock_prices):
    flag = 0
    while flag != 1:
        try:
            file = read_file()
            data = json.load(file)
            for key in data:
                stock_prices[key] = data[key]
            print(stock_prices)
            flag = 1
        except BadRequest as Error:
            print(Error)
        except:
            print(errors["invalid_file_format_expected_json"])


def manually_enter_trade(trading_data):
    try:
        ticker = input(input_messages["ticker"])
        flag = buy_or_sell(input(input_messages["flag"]))
        quantity = test_stock_details(input(input_messages["quantity"]), int)
        cost = test_stock_details(input(input_messages["cost"]),
                                  float)
        date_of_trade = format_date(input(input_messages["date_of_trade"]))
        append_to_trading_data(trading_data,
                               [date_of_trade, ticker, flag, quantity, cost])
        print_trade_details(date_of_trade, ticker, flag, quantity, cost)
        print(success_messages["trade_added"])
    except:
        print(errors["input_error"])


def view_trading_data(trading_data):
    sorted_data = trading_data.copy()
    ticker = input(input_messages["find_ticker"])
    sort_date = input(input_messages["sort_date"])
    if sort_date == "y":
        sorted_data.sort(key=lambda trading_data: trading_data[0],
                         reverse=True)
    if ticker:
        sorted_data = [
            filtered_data for filtered_data in sorted_data
            if ticker in filtered_data
        ]
    for [date_of_trade, ticker, flag, quantity, cost] in sorted_data:
        print_trade_details(date_of_trade, ticker, flag, quantity, cost)

def view_current_portfolio(trading_data, stock_prices):
    portfolio = {}
    for stock in trading_data:
        data_of_trade, ticker, flag, quantity, cost = stock
        is_stock_price_available = ticker in stock_prices
        if ticker in portfolio:
            portfolio[ticker]["units"] = add_or_reduce_stocks(
                flag, portfolio[ticker]["units"], quantity)
            if is_stock_price_available:
                portfolio[ticker]["value"] = round(
                    float(portfolio[ticker]["units"] * stock_prices[ticker]),
                    2)
        else:
            units = add_or_reduce_stocks(flag, 0, quantity)
            value = round(
                float(units * stock_prices[ticker]),
                2) if is_stock_price_available else errors["value_unknown"]
            portfolio[ticker] = {"units": units, "value": value}

    for key in sorted(portfolio.keys()):
        print("{0}\nTotal units:\t{1}\nTotal value: $\t{2}\n".format(
            key, portfolio[key]["units"], portfolio[key]["value"]))


def save_trading_data(trading_data):
    flag = 0
    while flag != 1:
        try:
            filename = input(input_messages["filename"])
            if not filename.strip():
                raise BadRequest(errors["field_blank"])
            test_valid_file_name_and_extension(filename, "csv")
            with open(filename, 'w', encoding='UTF8') as file:
                writer = csv.writer(file)
                for row in trading_data:
                    writer.writerow(row)
            print("Data save to {0}.".format(filename))
            flag = 1
        except BadRequest as Error:
            print(Error)


def thank_you():
    print(success_messages["thank_you"])

def menu_actions(trading_data, stock_price):
  actions = {
        1: lambda: load_trading_data(trading_data),
        2: lambda: load_stock_prices(stock_price),
        3: lambda: manually_enter_trade(trading_data),
        4: lambda: view_trading_data(trading_data),
        5: lambda: view_current_portfolio(trading_data, stock_price),
        6: lambda: save_trading_data(trading_data),
        7: lambda: thank_you()
    }
  return actions