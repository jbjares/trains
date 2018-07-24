import argparse
import socket
import os
import requests

MODELS_DIR = "/models"
RESULT_FILE = os.path.join(MODELS_DIR, "results")

CMD_RUN_ALGORITHM = 'run_algorithm'
CMD_PRINT_SUMMARY = 'print_summary'

DATA_ROUTE = 'http://data-storage-service/data'
NAME_ROUTE = 'http://data-storage-service/name'


def ensure_models_dir():
    if not os.path.exists(MODELS):
        os.mkdir(MODELS)


def run_algorithm():
    ensure_models_dir()
    # fetch station name
    name = requests.get(url=NAME_ROUTE)
    n_lines = len(requests.get(url=DATA_ROUTE).split('\n'))
    result_line = "{}: {}\n".format(name, n_lines)
    print(result_line)
    with open(file=RESULT_FILE, 'a') as f:
        f.write(result_line)

def print_summary():
    """
    Lists the result file
    """
    ensure_models_dir()
    if not os.path.exists(RESULT_FILE):
        return
    with open(RESULT_FILE, 'r') as f:
        for line in f:
            print(line.strip())


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
