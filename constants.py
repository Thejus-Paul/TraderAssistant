welcome_message = """Welcome  to the Trader Assistant
Programmed by <<Your Name>>"""

menu = """Please choose from  the options below 
1. Load trading data
2. Load current stock prices
3. Manually enter a new trade
4. View trading data
5. View current portfolio
6. Save trading data
7. Quit"""

date_format = "%Y-%m-%d"

errors = {
  "invalid_selection": "Invalid Selection",
  "something_went_wrong": "Something went wrong, Please try again!",
  "invalid_filename": "Please enter a valid filename.",
  "invalid_file_format": "Error with file format.",
  "invalid_file_format_expected_json": "Error with file format. Please provide a valid JSON file.",
  "invalid_file_format_expected_csv": "Error with file format. Please provide a valid CSV file.",
  "input_error": "Error in input",
  "field_blank": "Cannot be blank.",
  "invalid_file": "Invalid File",
  "value_unknown": "Current value unknown."
}

success_messages = {
  "thank_you": "Thanks for using the Trade Assistant",
  "trade_added": "Trade added to system"
}

input_messages = {
  "ticker": "Ticker:\t",
  "flag": "Buy or sell:\t",
  "quantity": "Quantity of stock:\t",
  "cost": "Total cost(including brokerage):\t",
  "date_of_trade": "Date:\t",
  "find_ticker": "Ticker (leave blank for all):\t",
  "sort_date": "Sort dates in reverse chronological order? (y/n)\t",
  "filename": "Enter filename:"
}

trade_related_constants = {
  "buy": "BUY",
  "sell": "SELL"
}