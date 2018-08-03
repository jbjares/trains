from pht.train import Train, cmd_for_train
from pht.station import StationClient
import sys
import tempfile
import os


def count_lines_in_file(filename):
    with open(filename, 'r') as f:
        return len(list(f))


class CountRowsTrain(Train):

    def __init__(self, hostname):
        self.client = StationClient(hostname)
        self.model = "/model"

    def print_next_departure_id(self):
        print(self.client.request_name())

    def run_algorithm(self):
        data_file = tempfile.mkstemp()[1]
        self.client.request_data(data_file)
        n_lines = count_lines_in_file(data_file)
        name = self.client.request_name()
        with open(self.model, 'w') as f:
            f.write(name + '\t' + n_lines + '\n')

    def print_summary(self):
        if not os.path.exists(self.model):
            return
        with open(self.model, 'r') as f:
            for line in f:
                line = line.strip()
                print(line)
    
    def check_requirements(self):
        sys.exit(0)

if __name__ == '__main__':
    train = CountRowsTrain("station")
    cmd_for_train(train)

