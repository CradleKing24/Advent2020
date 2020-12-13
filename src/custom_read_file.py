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


def sanitize_data(data):
    count = 0
    clean_batch_data = []
    full_data = []
    data_start_length = len(data)

    while count < data_start_length:
        pass_port = ""
        try:
            delimit_loc = data.index("\n")
        except ValueError:
            print("No more delimits found")
            count_temp = 0
            while count_temp < len(data):
                pass_port += data[count_temp].rstrip("\n") + " "
                count_temp += 1
            clean_batch_data.append(pass_port)
            break
        count_temp = 0
        while count_temp < delimit_loc:
            pass_port += data[0].rstrip("\n") + " "
            data.pop(0)
            count_temp += 1
        if data[0] == "\n":
            data.pop(0)
        clean_batch_data.append(pass_port)
        count += 1
    return clean_batch_data


def return_data_day4(file_name):
    data = open(file_name, mode="r")
    data_list = data.readlines()
    data.close()
    return sanitize_data(data_list)


def return_data_day6(file_name):
    data = open(file_name, mode="r")
    data_list = data.readlines()
    data.close()
    data_list = sanitize_data(data_list)
    full_data = []
    for i in data_list:
        i = i.replace(" ", "")
        full_data.append(i)
    return full_data

def return_data_day6_2(file_name):
    data = open(file_name, mode="r")
    data_list = data.readlines()
    data.close()
    data_list = sanitize_data(data_list)
    full_data = []
    for i in data_list:
        i = i.rstrip()
        full_data.append(i)
    return full_data


def return_reader_dictionary(file_name):
    with open(file_name, mode="r") as csv_file:
        reader = csv.DictReader(csv_file)
        csv_file.close()
        return dict(reader)
