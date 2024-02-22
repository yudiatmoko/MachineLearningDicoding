import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-o', '--output', action='store_true', help='show output')
args = parser.parse_args()

if args.output:
    print('Hello, this is output from parser_processing_.py')