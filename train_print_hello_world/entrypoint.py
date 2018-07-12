import argparse
import socket
import os

CMD_RUN_ALGORITHM = 'run_algorithm'
CMD_PRINT_SUMMARY = 'print_summary'


def run_algorithm():
    pass


def print_summary():
    print("Hello World")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('tool', choices = [ CMD_RUN_ALGORITHM, CMD_PRINT_SUMMARY])

    args = parser.parse_args()
    if args.tool == CMD_RUN_ALGORITHM:
        run_algorithm()
    elif args.tool == CMD_PRINT_SUMMARY:
        print_summary()

if __name__ == '__main__':
    main()

