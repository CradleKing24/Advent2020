import csv


def return_reader_list(file_name):
    with open(file_name, mode="r") as csv_file:
        reader = csv.reader(csv_file, delimiter=",")
        data = list(reader)
        csv_file.close()
        return data


def return_reader_lines(file_name):
    data = open(file_name, mode="r")
    data_list = data.read().splitlines()
    data.close()
    return data_list


def return_reader_dictionary(file_name):
    with open(file_name, mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        csv_file.close()
        return dict(reader)
