from src import custom_read_file as reader
import math


def get_day_input():
    data = reader.return_reader_lines("./resources/twenty_twenty/day3.csv")
    return data


def run_part_1(data):
    current_step = 1
    step_right = 3
    tree_count = 0
    while current_step < len(data):
        step_length = len(data[current_step])
        if step_length <= step_right:
            step_right = step_right - step_length

        obstacle = data[current_step][step_right]
        if obstacle == "#":
            tree_count += 1
        step_right += 3
        current_step += 1
    return tree_count


def run_part_2(data, init_step_right, step_down):
    current_step = step_down
    tree_count = 0
    step_right = init_step_right
    while current_step < len(data):
        step_length = len(data[current_step])
        if step_length <= step_right:
            step_right = step_right - step_length

        obstacle = data[current_step][step_right]
        if obstacle == "#":
            tree_count += 1
        step_right += init_step_right
        current_step += step_down
    return tree_count


if __name__ == '__main__':
    #total = run_part_1(get_day_input())
    total = []
    total.append(run_part_2(get_day_input(), 1, 1))
    total.append(run_part_2(get_day_input(), 3, 1))
    total.append(run_part_2(get_day_input(), 5, 1))
    total.append(run_part_2(get_day_input(), 7, 1))
    total.append(run_part_2(get_day_input(), 1, 2))
    total = math.prod(total)
    print(total)
