import uuid


def get_table_name_from_select(option):
    return option.split(' - ')[0]


def get_table_id_from_select(option, lst):
    name = get_table_name_from_select(option)
    for i, table in enumerate(lst):
        if name == table.name:
            return i


def is_similar_table(name, lst):
    for i, table in enumerate(lst):
        if name == table.name:
            return True
    return False


def get_id():
    return uuid.uuid1()
