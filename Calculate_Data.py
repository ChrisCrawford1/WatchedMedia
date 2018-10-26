from Converter import Converter
import openpyxl


class CalculateData:
    # I know...a global, not the greatest. FIXME later
    media = []

    def __init__(self, csv_file):
        self.csv_file = csv_file

    def get_workbook(self):
        convert = Converter(self.csv_file)
        return convert.from_csv_to_workbook()

    def analyse_workbook(self):
        workbook = openpyxl.load_workbook(self.get_workbook())
        active_sheet = workbook.worksheets[0]
        print('{} has {} columns and {} rows'.format(active_sheet, active_sheet.max_column, active_sheet.max_row))

        for i in range(2, active_sheet.max_row):
            value = str(active_sheet.cell(column=1, row=i).value)
            value = value.split(':')

            if len(value) > 1:
                media_type = {
                    'type': 'tv_show',
                    'name': value[0]
                }
                if media_type not in self.media:
                    self.media.append(media_type)
            else:
                media_type = {
                    'type': 'movie',
                    'name': value[0]
                }
                self.media.append(media_type)

        self.get_breakdown()

    def get_breakdown(self):
        tv_count = 0
        movie_count = 0
        for item in self.media:
            if item['type'] == 'tv_show':
                tv_count += 1
            else:
                movie_count += 1

        tv_percentage = round((tv_count / len(self.media)) * 100, 1)
        movie_percentage = round((movie_count / len(self.media)) * 100, 1)

        print('TV Shows Watched: {}({}%), Movies Watched:{}({}%)\nTotal Media Consumed: {}'
              .format(tv_count, tv_percentage, movie_count, movie_percentage, len(self.media)))
