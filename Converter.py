import os
import csv
import openpyxl
from pathlib import Path


class Converter:

    def __init__(self, csv_file):
        os.chdir(os.path.expanduser('~/Downloads'))
        self.csv_file = csv_file
        pass

    def from_csv_to_workbook(self, new_file_name='NetflixHistory'):
        wb = openpyxl.Workbook()
        ws = wb.active

        with open(self.csv_file) as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                ws.append(row)

            self.delete_old_versions(new_file_name)
            wb.save(new_file_name + '.xlsx')
            return '{}.xlsx'.format(new_file_name)

    def delete_old_versions(self, old_file):
        file = Path(os.getcwd() + old_file + '.xlsx')

        if file.is_file():
            print('Old version found, deleting...')
            os.remove(old_file + '.xlsx')
