from src import custom_read_file as reader
from collections import Counter


def get_day_input():
    data = reader.return_data_day6("./resources/twenty_twenty/day6.csv")
    return data


def get_day_input_2():
    data = reader.return_data_day6_2("./resources/twenty_twenty/day6.csv")
    return data


def run_part_1(data):
    total_yes_count = 0

    for each_group in data:
        yes_list = []
        for each_question in each_group:
            if each_question not in yes_list:
                yes_list.append(each_question)
        total_yes_count += len(yes_list)
    return total_yes_count


def run_part_2(data):
    total_yes_count = 0
    for each_group in data:
        group_members = each_group.split(" ")
        yes_list = []
        for member in group_members:
            for answer in member:
                #not efficient def better way but too late
                yes_list.append(answer)
        member_count = len(group_members)
        #counter is a map
        counter = Counter(yes_list)
        for element in counter:
            if member_count == counter[element]:
                total_yes_count += 1
        # total_yes_count = len(yes_list)
    return total_yes_count

if __name__ == '__main__':
    #total = run_part_1(get_day_input())
    total = run_part_2(get_day_input_2())
    print(total)