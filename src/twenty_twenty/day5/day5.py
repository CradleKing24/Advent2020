from src import custom_read_file as reader
from collections import Counter


def get_day_input():
    data = reader.return_reader_lines("./resources/twenty_twenty/day5.csv")
    return data


def split_list(local_list, front):
    half = len(local_list) // 2
    if front:
        return local_list[:half]
    else:
        return local_list[half:]


def get_column(commands):
    all_column = list(range(8))
    column = all_column.copy()
    for command in commands:
        if command == "L":
            column = split_list(column, True)
        elif command == "R":
            column = split_list(column, False)
    return column[0]


def get_row(commands):
    all_rows = list(range(128))
    row = all_rows.copy()
    for command in commands:
        if command == "F":
            row = split_list(row, True)
        elif command == "B":
            row = split_list(row, False)
    return row[0]


def get_seat_id(boarding_pass):
    row_commands = boarding_pass[:7]
    column_commands = boarding_pass[-3:]
    row = get_row(row_commands)
    column = get_column(column_commands)
    seat_id = row * 8 + column
    return seat_id


def get_seat_id_2(boarding_pass):
    row_commands = boarding_pass[:7]
    column_commands = boarding_pass[-3:]
    all_rows = list(range(128))
    taken_rows = []
    row = get_row(row_commands)
    taken_rows.append(row)
    column = get_column(column_commands)
    seat_id = row * 8 + column
    return seat_id


def run_part_1(data):
    seat_ids = []
    for each_boarding_pass in data:
        seat_ids.append(get_seat_id(each_boarding_pass))
    return seat_ids


def run_part_2(data):
    seat_ids = []
    taken_rows = []
    all_rows = list(range(128))
    for each_boarding_pass in data:
        row_commands = each_boarding_pass[:7]
        column_commands = each_boarding_pass[-3:]
        row = get_row(row_commands)
        taken_rows.append(row)
        column = get_column(column_commands)
        if row == 85:
            print("85 column taken: ", column)
        seat_id = row * 8 + column
        seat_ids.append(seat_id)
    taken_rows.sort()
    thing = Counter(taken_rows)
    print(thing)
    for element in all_rows:
        if element not in taken_rows:
            print(element)
    return seat_ids


if __name__ == '__main__':
    #total = run_part_1(get_day_input())
    total = run_part_2(get_day_input())
    total.sort()
    all_seats = list(range(32, 849))
    # for element in total:
    #     if element not in all_seats:
    #         print(element)
    print(total)
    print(max(total))
