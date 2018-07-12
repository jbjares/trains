import argparse
import socket
import os

MODELS = '/models'

CMD_RUN_ALGORITHM = 'run_algorithm'
CMD_PRINT_SUMMARY = 'print_summary'

def ensure_models_dir():
    if not os.path.exists(MODELS):
        os.mkdir(MODELS)

def run_algorithm():
    ensure_models_dir()
    hostname = socket.gethostname()
    with open(os.path.join(MODELS, hostname), 'w') as f:
        f.write(hostname)

def print_summary():
    ensure_models_dir()
    names = os.listdir(MODELS)
    for name in names:
        print(name)

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

