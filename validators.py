from badrequest import BadRequest
from constants import errors, date_format, trade_related_constants
import time as datetime

def buy_or_sell(flag):
    if (flag == "b"):
        return trade_related_constants["buy"]
    elif (flag == "s"):
        return trade_related_constants["sell"]
    raise BadRequest(errors["invalid_file_format_expected_csv"])


def format_date(date):
    try:
        datetime.strptime(date, date_format)
        return date
    except:
        raise BadRequest(errors["invalid_file_format_expected_csv"])


def test_stock_details(value, datatype):
    if (datatype(value) > 0):
        return datatype(value)
    raise BadRequest(errors["invalid_file_format_expected_csv"])

def test_valid_file_name_and_extension(filename, extension):
    if filename.split(".")[1:] in [[
            extension
    ]] and filename[0].isalpha() and sum(c.isdigit() for c in filename) < 4:
        return True
    else:
        raise BadRequest(errors["invalid_file"])