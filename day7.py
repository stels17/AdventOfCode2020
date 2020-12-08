# light red bags contain 1 bright white bag, 2 muted yellow bags.

# 1. Create light_red Bag. Add it to 'all_bags' array
# 2. Create bright_white Bag, add to 'all_bags', and assign parent = light_red(1)
# 3. Create muted_yellow Bag, add to 'all_bag', and assign parent = light_red(2)

# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.

# 4. We already have muted_yellow: checked with 'all_bags' array
# 5. We may already have shiny_gold - check with 'all_bags'. If it is there, than take it. Otherwise, create it and add to 'all_bags'. Set parent and quantity

# if 'no other bags' - ignore it completely


# individual bag managing:
class Bag:
    name = None
    parents = None
    children = None

    def __init__(self, title):
        self.name = title
        self.parents = []
        self.children = []

    def assign_parent(self, parent_bag, how_many):
        self.parents.append({'pointer': parent_bag, 'how_many': how_many})

    def assign_child(self, child_bag, how_many):
        self.children.append({'pointer': child_bag, 'how_many': how_many})

    def get_all_parents(self, acc=set()):
        for parent in self.parents:
            acc.add(parent['pointer'])
            if parent['pointer'].parents != []:
                acc.union(parent['pointer'].get_all_parents())
        return acc

    def count_children(self, acc=0):
        for child in self.children:
            acc += child['how_many']  # bag itself
            if child['pointer'].children:
                # bag's children, muiltiplied by 'parental' bag number
                acc += child['how_many'] * child['pointer'].count_children()
        return acc


# all bags collection managing:
def get_or_create_bag(bag_name, all_created_bugs):
    # checks if bag with a specif name is already in our list. If yes,
    # returns pointer to that bag (bag object). Otherwise creates one
    if bag_name not in all_created_bugs.keys():
        bag_object = Bag(bag_name)
        all_created_bugs[bag_name] = bag_object
    else:
        bag_object = all_created_bugs[bag_name]
    return bag_object


def exercise():
    f = open("ex7.txt", "rt")
    lines = f.read().splitlines()
    f.close()

    all_possible_bags = dict()  # {'light_red': pointer_to_bag}

    for line in lines:
        if line[-14:] == 'no other bags.': continue

        parent_and_children = line.split(" bags contain ")
        parent_bag_name, children = parent_and_children
        children = children.split(", ")

        parent_bag_object = get_or_create_bag(parent_bag_name,
                                              all_possible_bags)

        for child in children:
            child_bag_data = child.split(' bag')[0]
            bags_count, bag_name = child_bag_data.split(" ", 1)

            child_bag_object = get_or_create_bag(bag_name, all_possible_bags)

            child_bag_object.assign_parent(parent_bag_object, bags_count)

            parent_bag_object.assign_child(child_bag_object, int(bags_count))

    our_bag = all_possible_bags['shiny gold']
    print("1. Number of kind of bags that may contain our bag:",
          len(our_bag.get_all_parents()))
    print("2. Our poor bag must contain:", our_bag.count_children())


exercise()
