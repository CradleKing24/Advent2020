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
    prev_bags = 0
    done = False
    map_of_bags = {}
    map_of_all_bag_indecies = {}
    for i, bags in enumerate(data):
        bags = bags.replace(".", "").replace("bags", "bag")
        if bags.find("shiny gold bag") == 0:
            #this is the gold bag, get all bags after current
            init_bags = bags[bags.find("contain")+len("contain "):]
            bag_count = init_bags.split(",")
            for each_bag in bag_count:
                num_of_bag = each_bag.split(" ", 1)
                map_of_bags.update({num_of_bag[1]: num_of_bag[0]})
        else:
            #loop through all rules 1 time and get index for all the bag rules attempt as efficiency..
            first_bag_rule = bags[:bags.find("contain")]
            map_of_all_bag_indecies.update({first_bag_rule: i})

    print(map_of_all_bag_indecies)
    print(map_of_bags)
    return 0


if __name__ == '__main__':
    total = run_part_1(get_day_input())
    # total = run_part_2(get_day_input())
    print(total)