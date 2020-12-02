from src import custom_read_file as reader
from src.day2 import funcs


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


if __name__ == '__main__':
    data = reader.return_reader_list("./resources/day2_1.csv")
    data = [int(i) for i in data[0]]
    data[1] = 12
    data[2] = 2
    index_1 = day_2_1(data)
    print(index_1)
