import os
import csv
import openpyxl
from pathlib import Path


class Converter:

    def __init__(self):
        os.chdir(os.path.expanduser('~/Downloads'))
        pass

    def auto_discover_netflix_file(self):
        print("Attempting to auto-discover your Netflix history file...")
        for file in os.listdir('.'):
            if 'Netflix' in file and file.endswith('csv'):
                print("File Found! \n")
                return file

    def from_csv_to_workbook(self, new_file_name='NetflixHistory'):
        csv_file = self.auto_discover_netflix_file()
        wb = openpyxl.Workbook()
        ws = wb.active

        with open(csv_file) as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                ws.append(row)

            self.delete_old_versions(new_file_name)
            wb.save(new_file_name + '.xlsx')
            return '{}.xlsx'.format(new_file_name)

    def delete_old_versions(self, old_file):
        file = Path(os.getcwd() + '/' + old_file + '.xlsx')

        if file.is_file():
            os.remove(old_file + '.xlsx')
