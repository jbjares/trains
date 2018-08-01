from pht.train import Train, cmd_for_train
import sys

class SummaryTrain(Train):

    def print_next_departure_id(self):
        raise NotImplemented

    def run_algorithm(self):
        raise NotImplemented

    def print_summary(self):
        print("TEST_PRINT_SUMMARY_1")
    
    def check_requirements(self):
        sys.exit(1)

if __name__ == '__main__':
    cmd_for_train(SummaryTrain())

