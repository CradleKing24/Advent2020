from src import custom_read_file as reader


def get_day_input():
    data = reader.return_reader_lines("./resources/twenty_twenty/day7.csv")
    return data


def run_part_1(data):
    #f recursion
    # recurse_bags_1(data)
    bag_has_bag_with_gold = []
    bags_contain_gold = []
    prev_bags = 0
    done = False
    for bags in data:
        if bags.find("shiny gold bag") > -1:
            #this bag either has gold or is gold
            if bags.find("shiny gold bag") > 0:
                # this bag has gold and is not gold
                loc = bags.split("s contain", 1)[0]
                #bags that contain gold directly
                bags_contain_gold.append(loc)
    bag_has_bag_with_gold = bags_contain_gold.copy()
    while not done:
        for bags in data:
            for gold_bags in bag_has_bag_with_gold:
                if bags.find(gold_bags) > -1:
                    loc = bags.split("s contain", 1)[0]
                    if loc not in bag_has_bag_with_gold:
                        bag_has_bag_with_gold.append(loc)
        if len(bag_has_bag_with_gold) != prev_bags:
            prev_bags = len(bag_has_bag_with_gold)
        else:
            done = True

    return len(bag_has_bag_with_gold)


def run_part_2(data):
    gold_bag_has_bags = []
    prev_bags = 0
    done = False
    for bags in data:
        if bags.find("shiny gold bag") == 0:
            #this is the gold bag
            init_bags = bags[bags.find("contain")+len("contain "):]
            bag_count = init_bags.split(" ", 1)
            bag_count[1] = bag_count[1].replace("bags", "bag")
            gold_bag_has_bags.append(bags)

    print(gold_bag_has_bags)
    return 0


if __name__ == '__main__':
    total = run_part_1(get_day_input())
    # total = run_part_2(get_day_input())
    # total.sort()
    # all_seats = list(range(32, 849))
    # for element in total:
    #     if element not in all_seats:
    #         print(element)
    print(total)