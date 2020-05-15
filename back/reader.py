import xlrd
import sys
import json

def read_xl_data(row_number):
    file_path = 'our_dataset_new_raw.xlsx'
    wb = xlrd.open_workbook(file_path)
    sheet = wb.sheet_by_index(0)

    # arr = []

    headers = sheet.row_values(0)

    elements = sheet.row_values(row_number)

    return {header : elem for header, elem in zip(headers, elements)}


def write_into_json(objct, filename="input.json"):
    with open(filename, 'w') as f:
        json.dump(objct, f)


def main(row_number):
    file_path = 'our_dataset_new_raw.xlsx'

    write_into_json(read_xl_data(row_number))


if __name__ == '__main__':
    main(int(sys.argv[1]))
    print('123123')
    sys.stdout.flush()

