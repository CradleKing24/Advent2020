import re

def check_range(value, low, high):
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


def check_height(attribute_val):
    if attribute_val.find("cm") > -1:
        if check_regex("^[0-9]{3}cm$", attribute_val):
            return check_range(attribute_val[:-2], 150, 193)
    elif attribute_val.find("in") > -1:
        if check_regex("^[0-9]{2}in$", attribute_val):
            return check_range(attribute_val[:-2], 59, 76)


def check_hair_color(attribute_val):
    return check_regex("^#[a-f0-9]{6}$", attribute_val)


def check_eye_color(attribute_val):
    return check_regex("^amb|blu|brn|gry|grn|hzl|oth$", attribute_val)


def check_pass_id(attribute_val):
    return check_regex("^[0-9]{9}$", attribute_val)
