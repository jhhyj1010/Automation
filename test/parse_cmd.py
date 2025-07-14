# parse parameters from the command line
import argparse

# Create the parser
parser = argparse.ArgumentParser(description="Process some integers.")

# Add the arguments
parser = argparse.ArgumentParser(description='Set or get custom properties for a GitHub repository.')
parser.add_argument('org', help='The organization that owns the repository.', nargs='?')
parser.add_argument('repo', help='The repository to set the property for.', nargs='?')
parser.add_argument('--mode', choices=['set', 'get', 'csv'], required=True, help='The mode to run the script in. " to set a custom property, "get" to get all custom properties, "csv" to process a csv file.')
parser.add_argument('--propertyname', help='The name of the property to set. Required if mode is "set".')
parser.add_argument('--value', help='The value to set the property to. Required if mode is "set".')
parser.add_argument('--file', help='The path to the csv file. Required if mode is "csv".')

# Parse the arguments
args = parser.parse_args()
import pdb;pdb.set_trace()

print(args.accumulate(args.integers))