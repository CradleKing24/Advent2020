def add_opcodes(index_f, index_l):
    return index_f + index_l


def multiply_opcodes(index_f, index_l):
    return index_f * index_l


def check_opcode(code, index_f, index_l):
    if code == 1:
        return add_opcodes(index_f, index_l)
    elif code == 2:
        return multiply_opcodes(index_f, index_l)
    else:
        pass
