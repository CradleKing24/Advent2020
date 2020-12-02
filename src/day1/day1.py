from src import custom_read_file as reader


def loop_input_part_2(data_in):
    for expense in data_in:
        for nextExpense in data_in:
            for lastExpense in data_in:
                if expense == nextExpense and expense == lastExpense and nextExpense == lastExpense:
                    pass
                else:
                    result = expense + nextExpense + lastExpense
                    if result == 2020:
                        return expense * nextExpense * lastExpense


def loop_input(data_in):
    for expense in data_in:
        for nextExpense in data_in:
            if expense == nextExpense:
                pass
            else:
                result = expense + nextExpense
                if result == 2020:
                    return expense * nextExpense


if __name__ == '__main__':
    data_input = reader.return_reader_lines("./resources/day1.csv")
    data_input = [int(i) for i in data_input]
    answer = loop_input_part_2(data_input)
    print(answer)
