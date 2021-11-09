import uuid


def get_table_name_from_select(option):
    """Helper function for getting table name"""
    return option.split(' - ')[0]


def get_table_id_from_select(option, lst):
    """Helper function for computing table index by name"""
    name = get_table_name_from_select(option)
    for i, table in enumerate(lst):
        if name == table.name:
            return i


def is_similar_table(name, lst):
    """Check new table name to be unique"""
    for i, table in enumerate(lst):
        if name == table.name:
            return True
    return False


def get_id():
    """Generate id for table"""
    return uuid.uuid1()
