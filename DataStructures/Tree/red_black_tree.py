from DataStructures.Tree import rbt_node
from DataStructures.List import array_list as al


def default_compare(key, element):
    element_key = rbt_node.get_key(element)
    comparison = 0
    if key < element_key:
        comparison = -1
    elif key > element_key:
        comparison = 1
    return comparison


def size_tree(node):
    size = 0
    if node is not None:
        size = node["size"]
    return size


def is_red(node):
    red = False
    if node is not None:
        if node["color"] == rbt_node.RED:
            red = True
    return red


def flip_node_color(node):
    if node is not None:
        if is_red(node):
            node["color"] = rbt_node.BLACK
        else:
            node["color"] = rbt_node.RED


def flip_colors(node):
    if node is not None:
        if node["left"] is not None and node["right"] is not None:
            flip_node_color(node)
            flip_node_color(node["left"])
            flip_node_color(node["right"])


def rotate_left(node):
    child = node["right"]
    if child is None:
        return node
    node["right"] = child["left"]
    child["left"] = node
    child["color"] = node["color"]
    node["color"] = rbt_node.RED
    child["size"] = node["size"]
    node["size"] = 1 + size_tree(node["left"]) + size_tree(node["right"])
    return child


def rotate_right(node):
    child = node["left"]
    if child is None:
        return node
    node["left"] = child["right"]
    child["right"] = node
    child["color"] = node["color"]
    node["color"] = rbt_node.RED
    child["size"] = node["size"]
    node["size"] = 1 + size_tree(node["left"]) + size_tree(node["right"])
    return child


def insert_node(node, key, value):
    if node is None:
        new_node = rbt_node.new_node(key, value, rbt_node.RED)
        node = new_node
    else:
        comparison = default_compare(key, node)
        if comparison < 0:
            node["left"] = insert_node(node["left"], key, value)
        elif comparison > 0:
            node["right"] = insert_node(node["right"], key, value)
        else:
            node["value"] = value
        if is_red(node["right"]) and not is_red(node["left"]):
            node = rotate_left(node)
        if is_red(node["left"]) and is_red(node["left"]["left"]):
            node = rotate_right(node)
        if is_red(node["left"]) and is_red(node["right"]):
            flip_colors(node)
        node["size"] = 1 + size_tree(node["left"]) + size_tree(node["right"])
    return node


def new_map():
    return {"root": None, "type": "RBT", "size": 0}


def put(my_map, key, value):
    if "size" not in my_map:
        my_map["size"] = size_tree(my_map.get("root"))
    old_node = get_node(my_map["root"], key)
    my_map["root"] = insert_node(my_map["root"], key, value)
    my_map["root"]["color"] = rbt_node.BLACK
    if old_node is None:
        my_map["size"] += 1
    return my_map


def get_node(node, key):
    found_node = None
    if node is not None:
        comparison = default_compare(key, node)
        if comparison < 0:
            found_node = get_node(node["left"], key)
        elif comparison > 0:
            found_node = get_node(node["right"], key)
        else:
            found_node = node
    return found_node


def get(my_map, key):
    node = get_node(my_map["root"], key)
    value = None
    if node is not None:
        value = node["value"]
    return value


def size(my_map):
    return size_tree(my_map["root"])

def is_empty(my_map):
    state = size(my_map)
    if state == 0:
        return True
    return False

def contains(my_map, key):
    state = get(my_map, key)
    if state == None:
        return False
    return True


def key_set(my_map):
    keys = al.new_list()
    keys = key_set_tree(my_map["root"], keys)
    return keys


def key_set_tree(node, key_list):
    if node is not None:
        key_set_tree(node["left"], key_list)
        al.add_last(key_list, node["key"])
        key_set_tree(node["right"], key_list)
    return key_list


def value_set(my_rbt):
    return value_set_tree(my_rbt["root"], al.new_list())


def value_set_tree(node, value_list):
    if node is not None:
        value_set_tree(node["left"], value_list)
        al.add_last(value_list, node["value"])
        value_set_tree(node["right"], value_list)
    return value_list


def get_min_node(node):
    if node is None or node["left"] is None:
        return node
    return get_min_node(node["left"])


def get_min(my_rbt):
    node = get_min_node(my_rbt["root"])
    return None if node is None else node["key"]


def get_max_node(node):
    if node is None or node["right"] is None:
        return node
    return get_max_node(node["right"])


def get_max(my_rbt):
    node = get_max_node(my_rbt["root"])
    return None if node is None else node["key"]


def height_tree(node):
    if node is None:
        return 0
    return 1 + max(height_tree(node["left"]), height_tree(node["right"]))


def height(my_rbt):
    return height_tree(my_rbt["root"])


def keys_range(node, key_lo, key_hi, key_list):
    if node is not None:
        if key_lo < node["key"]:
            keys_range(node["left"], key_lo, key_hi, key_list)
        if key_lo <= node["key"] <= key_hi:
            al.add_last(key_list, node["key"])
        if node["key"] < key_hi:
            keys_range(node["right"], key_lo, key_hi, key_list)
    return key_list


def keys(my_rbt, key_initial, key_final):
    return keys_range(my_rbt["root"], key_initial, key_final, al.new_list())


def values_range(node, key_lo, key_hi, value_list):
    if node is not None:
        if key_lo < node["key"]:
            values_range(node["left"], key_lo, key_hi, value_list)
        if key_lo <= node["key"] <= key_hi:
            al.add_last(value_list, node["value"])
        if node["key"] < key_hi:
            values_range(node["right"], key_lo, key_hi, value_list)
    return value_list


def values(my_rbt, key_initial, key_final):
    return values_range(my_rbt["root"], key_initial, key_final, al.new_list())