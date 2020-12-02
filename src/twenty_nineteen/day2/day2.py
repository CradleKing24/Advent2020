from src import custom_read_file as reader
from src.twenty_nineteen.day2 import funcs


def day_2_1(csv_reader):
    i = 0
    while i < len(csv_reader):
        opcode_init = csv_reader[i]
        if opcode_init == 99:
            break
        opcode_ind_f = csv_reader[i+1]
        opcode_ind_s = csv_reader[i+2]
        val_to_use = funcs.check_opcode(opcode_init, csv_reader[opcode_ind_f], csv_reader[opcode_ind_s])
        opcode_ind_r = csv_reader[i+3]
        csv_reader[opcode_ind_r] = val_to_use
        i += 4
    return csv_reader


def day_2_2(csv_reader):
    i = 0
    while i < len(csv_reader):
        opcode_init = csv_reader[i]
        if opcode_init == 99:
            break
        opcode_ind_f = csv_reader[i+1]
        opcode_ind_s = csv_reader[i+2]
        val_to_use = funcs.check_opcode(opcode_init, csv_reader[opcode_ind_f], csv_reader[opcode_ind_s])
        opcode_ind_r = csv_reader[i+3]
        csv_reader[opcode_ind_r] = val_to_use
        i += 4
    return csv_reader


def run_day_2_1():
    data = reader.return_reader_list("./resources/day2_1.csv")
    data = [int(i) for i in data[0]]
    data[1] = 12
    data[2] = 2
    index_1 = day_2_1(data)
    print(index_1)


def run_day_2_2():
    data = reader.return_reader_list("./resources/day2_1.csv")
    data = [int(i) for i in data[0]]
    gold_list = data.copy()
    result = []
    noun_count = 0
    verb_count = 0
    while noun_count < 100:
        while verb_count < 100:
            data[1] = noun_count
            data[2] = verb_count
            returned_list = day_2_2(data)
            if returned_list[0] == 19690720:
                result = returned_list
                break
            data = gold_list.copy()
            verb_count += 1
        if result and result[0] == 19690720:
            break
        verb_count = 0
        noun_count += 1
    print(result)


if __name__ == '__main__':
    run_day_2_1()
    run_day_2_2()
