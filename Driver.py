from Calculate_Data import CalculateData


class Driver:

    if __name__ == '__main__':
        user_input = input('Enter file name: ')
        calc = CalculateData(user_input)
        calc.analyse_workbook()
