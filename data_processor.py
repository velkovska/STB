import csv

#Class that creates table with customer info
class Customer:
    def __init__(self, path_to_read,path_to_write):
        self.path_to_read = path_to_read
        self.path_to_write = path_to_write

    def create_csv(self):
        writefile = open(self.path_to_write, 'w')
        writefile_header = "Customer Code FirstName LastName\n"
        writefile.write(writefile_header)
        with open(self.path_to_read, 'r') as readfile:
            reader = csv.reader(readfile, delimiter=',')
            header = next(reader)
            for row in reader:
                customer_code = row[0]
                first_name = row[1]
                last_name = row[2]
                line = "{}  {}   {}\n".format(customer_code, first_name, last_name)
                writefile.write(line) 
        writefile.close()

x = Customer('customer.csv', 'customer_data.csv').create_csv()

#Class that creates table with invoices amount and date
class Invoice:
    def __init__(self, path_to_read,path_to_write):
        self.path_to_read = path_to_read
        self.path_to_write = path_to_write

    def create_csv(self):
        writefile = open(self.path_to_write, 'w')
        writefile_header = "CustomerCode    InvoiceCode Amount  Date\n"
        writefile.write(writefile_header)
        with open(self.path_to_read, 'r') as readfile:
            reader = csv.reader(readfile, delimiter=',')
            header = next(reader)
            for row in reader:
                customer_code = row[0]
                invoice_code = row[1]
                amount = row[2]
                date = row[3]
                line = "{}  {}   {}  {}\n".format(customer_code, invoice_code, amount, date)
                writefile.write(line) 
        writefile.close()

y = Invoice('invoice.csv', 'invoice_data.csv').create_csv()

#Class that creates table with invoices item amount code and quality
class Invoice_item:
    def __init__(self, path_to_read,path_to_write):
        self.path_to_read = path_to_read
        self.path_to_write = path_to_write

    def create_csv(self):       
        writefile = open(self.path_to_write, 'w')
        writefile_header = "InvoiceCode ItemCode Amount Quantity\n"
        writefile.write(writefile_header)
        with open(self.path_to_read, 'r') as readfile:
            reader = csv.reader(readfile, delimiter=',')
            header = next(reader)
            for row in reader:
                invoice_code = row[0]
                item_code = row[1]
                amount = row[2]
                quantity = row[3]
                line = "{}   {}    {}  {}\n".format(invoice_code, item_code, amount, quantity)
                writefile.write(line) 
        writefile.close()

z = Invoice_item('invoice_item.csv', 'invoice_item_data.csv').create_csv()