#Run command -> python .\task_2.py

import configparser
import requests

config = configparser.ConfigParser()
config.read('config.ini')

# Your Wolfram Alpha API key
API_KEY = config['DEFAULT']['API_KEY']

# Define the Wolfram Alpha API endpoint URL
API_URL = "http://api.wolframalpha.com/v1/result"

# Initialize an empty list to store the results
results = []

def evaluate_expressions():
    # Loop until the user types "end"
    while True:
        # Read in an expression from the user
        expression = input("Enter an expression (or type 'end' to finish): ")

        # Check if the user wants to exit
        if expression.lower() == "end":
            return results

        # Make the API request
        response = requests.get(
            API_URL, params={"appid": API_KEY, "i": expression})

        # Check if the API call was successful
        if response.status_code == 200:
            # Extract the result from the response and store it in the results list
            result = response.text.strip()
            results.append({"expression": expression, "result": result})
        else:
            # Handle the error
            print(f"Error: {response.status_code} - {response.text}")

def print_output(results):
    # Print the results for all expressions
    for i, result in enumerate(results):
        print(f"{i+1}. {result['expression']} => {result['result']}")

results = evaluate_expressions()
print_output(results)
