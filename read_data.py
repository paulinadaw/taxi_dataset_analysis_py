import csv

class ReadData:
    def __init__(self, csv_file):
        self.data = self.read_data(csv_file)
        self.column_names = self.display_column_names()

    def read_data(self, csv_file):
        data = []
        with open(csv_file, "r") as csv_dataset:
            spreadsheet = csv.DictReader(csv_dataset)
            for row in spreadsheet:
                data.append(row)
        return data

    def display_column_names(self):
        column_names = list(self.data[0].keys())  # Pobranie nazw kolumn z pierwszego wiersza
        return column_names

    def display_column_data(self, column_name):
        column_data = []
        for row in self.data:
            if row[column_name] is None or row[column_name] == "":
                row[column_name] = "No value"
            column_data.append(row[column_name])
        return column_data
