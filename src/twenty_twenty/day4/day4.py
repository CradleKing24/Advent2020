from src import custom_read_file as reader
import re


def get_day_input():
    data = reader.return_data_day4("./resources/twenty_twenty/day4.csv")
    return data


def sanitize_data(data):
    count = 0
    clean_batch_data = []
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


def run_part_1(data):
    clean_input = sanitize_data(data)

    valid_ports = 0

    for each_passport in clean_input:
        port = each_passport.rstrip().split()
        criteria_count = 0
        for each_attribute in port:
            if each_attribute.find("byr") > -1:
                criteria_count += 1
            if each_attribute.find("iyr") > -1:
                criteria_count += 1
            if each_attribute.find("eyr") > -1:
                criteria_count += 1
            if each_attribute.find("hgt") > -1:
                criteria_count += 1
            if each_attribute.find("hcl") > -1:
                criteria_count += 1
            if each_attribute.find("ecl") > -1:
                criteria_count += 1
            if each_attribute.find("pid") > -1:
                criteria_count += 1
        if criteria_count == 7:
            valid_ports += 1
    return valid_ports


def check_years(value, low, high):
    if_value_passed = False
    if low <= value <= high:
        if_value_passed = True
    return if_value_passed


def check_regex(regex, value):
    if_value_passed = False
    pattern = re.compile(regex)
    if pattern.match(value):
        if_value_passed = True
    return if_value_passed

def run_part_2(data):
    clean_input = sanitize_data(data)

    valid_ports = 0

    for each_passport in clean_input:
        port = each_passport.rstrip().split()
        criteria_count = 0
        for each_attribute in port:
            if each_attribute.find("byr") > -1:
                attribute_val = each_attribute.split(":")
                if check_years(int(attribute_val[1]), 1920, 2002):
                    criteria_count += 1
            if each_attribute.find("iyr") > -1:
                attribute_val = each_attribute.split(":")
                if check_years(int(attribute_val[1]), 2010, 2020):
                    criteria_count += 1
            if each_attribute.find("eyr") > -1:
                attribute_val = each_attribute.split(":")
                if check_years(int(attribute_val[1]), 2020, 2030):
                    criteria_count += 1
            if each_attribute.find("hgt") > -1:
                attribute_val = each_attribute.split(":")
                if attribute_val[1].find("cm") > -1:
                    if check_regex("^[0-9]{3}cm$", attribute_val[1]):
                        criteria_count += 1
                elif attribute_val[1].find("in") > -1:
                    if check_regex("^[0-9]{2}in$", attribute_val[1]):
                        criteria_count += 1

                criteria_count += 1
            if each_attribute.find("hcl") > -1:
                attribute_val = each_attribute.split(":")
                pattern = re.compile("^#[a-f0-9]{6}$")
                if pattern.match(attribute_val[1]):
                    criteria_count += 1
            if each_attribute.find("ecl") > -1:
                criteria_count += 1
            if each_attribute.find("pid") > -1:
                criteria_count += 1
        if criteria_count == 7:
            valid_ports += 1
    return valid_ports


if __name__ == '__main__':
    total = run_part_1(get_day_input())
    #total.append(run_part_2(get_day_input(), 1, 1))
    print(total)
