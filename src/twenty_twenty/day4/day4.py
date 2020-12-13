from src import custom_read_file as reader
import re
from src.twenty_twenty.day4 import validator as valid


def get_day_input():
    data = reader.return_data_day4("./resources/twenty_twenty/day4.csv")
    return data


def run_part_1(data):
    clean_input = data

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


def check_regex(regex, value):
    if_value_passed = False
    pattern = re.compile(regex)
    if pattern.match(value):
        if_value_passed = True
    return if_value_passed


def run_part_2(data):
    clean_input = data

    valid_ports = 0

    for each_passport in clean_input:
        port = each_passport.rstrip().split()
        criteria_count = 0
        for each_attribute in port:
            if each_attribute.find("byr") > -1:
                attribute_val = each_attribute.split(":")
                if valid.check_range(int(attribute_val[1]), 1920, 2002):
                    criteria_count += 1
            if each_attribute.find("iyr") > -1:
                attribute_val = each_attribute.split(":")
                if valid.check_range(int(attribute_val[1]), 2010, 2020):
                    criteria_count += 1
            if each_attribute.find("eyr") > -1:
                attribute_val = each_attribute.split(":")
                if valid.check_range(int(attribute_val[1]), 2020, 2030):
                    criteria_count += 1
            if each_attribute.find("hgt") > -1:
                attribute_val = each_attribute.split(":")
                if valid.check_height(attribute_val[1]):
                    criteria_count += 1
            if each_attribute.find("hcl") > -1:
                attribute_val = each_attribute.split(":")
                if valid.check_hair_color(attribute_val[1]):
                    criteria_count += 1
            if each_attribute.find("ecl") > -1:
                attribute_val = each_attribute.split(":")
                if valid.check_eye_color(attribute_val[1]):
                    criteria_count += 1
            if each_attribute.find("pid") > -1:
                attribute_val = each_attribute.split(":")
                if valid.check_pass_id(attribute_val[1]):
                    criteria_count += 1
        if criteria_count == 7:
            valid_ports += 1
    return valid_ports


if __name__ == '__main__':
    #total = run_part_1(get_day_input())
    total = run_part_2(get_day_input())
    print(total)
