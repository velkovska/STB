from prettytable import from_csv

class Csv_data_printer:
    def __init__(self, file_path):
        self.file_path = file_path

    def print(self):
        csv_file=open(self.file_path) 
        read_the_file = from_csv(csv_file)
        print(read_the_file)
        

csm = Csv_data_printer("invoice.csv").print()
csm1 = Csv_data_printer("customer.csv").print()
csm2 = Csv_data_printer("invoice_item.csv").print()

