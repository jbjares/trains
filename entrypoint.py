import argparse
import socket

def print_traintype():
    print("PRINT_STDOUT")

def run_algorithm():
    print(socket.gethostname())

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('tool', choices = ['print_traintype', 'run_algorithm'])

    args = parser.parse_args()

    if args.tool == 'print_traintype':
        print_traintype()
    elif args.tool == 'run_algorithm':
        run_algorithm()

if __name__ == '__main__':
    main()
