from src import custom_read_file as reader


def get_day_input():
    data = reader.return_reader_lines("./resources/twenty_twenty/day2.csv")
    return data


def run_part_1(data):
    total_good_passwords = 0
    for index in data:
        split_ind = index.replace(" ", "").split(":")
        min_times = 0
        max_times = 0
        search_letter = ""
        search_text = ""
        for half in split_ind:
            if half.find("-") > 0:
                min_max_key = half.split("-")
                min_times = int(min_max_key[0])
                search_letter = min_max_key[1][-1]
                max_times = int(min_max_key[1][:-1])
            else:
                search_text = half

        letter_count = 0
        for letter in search_text:
            if letter == search_letter:
                letter_count += 1

        if min_times <= letter_count <= max_times:
            total_good_passwords += 1
    return total_good_passwords


def run_part_2(data):
    total_good_passwords = 0
    for index in data:
        split_ind = index.replace(" ", "").split(":")
        first_position = 0
        next_position = 0
        search_letter = ""
        search_text = ""
        for half in split_ind:
            if half.find("-") > 0:
                min_max_key = half.split("-")
                first_position = int(min_max_key[0])
                search_letter = min_max_key[1][-1]
                next_position = int(min_max_key[1][:-1])
            else:
                search_text = half

        i = 0
        letter_exists_count = 0
        for letter in search_text:
            i += 1
            if letter == search_letter and i == first_position:
                letter_exists_count += 1
            elif letter == search_letter and i == next_position:
                letter_exists_count += 1
        if letter_exists_count == 1:
            total_good_passwords += 1
    return total_good_passwords


if __name__ == '__main__':
    # total = run_part_1(get_day_input())
    total = run_part_2(get_day_input())
    print(total)
