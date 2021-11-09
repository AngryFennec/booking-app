import streamlit as st

from components.Table import Table
from utils import is_similar_table


def release_tables():
    """Make all seats of selected tables free"""
    if st.session_state.release_tables:
        for i, table in enumerate(st.session_state.tables):
            if st.session_state[f"table{table.id}"]:
                st.session_state.tables[i].free_seats = table.seats
        clear_select()


def remove_tables():
    """Remove selected tables from tables list"""
    if st.session_state.remove_tables:
        to_remove = []
        for table in st.session_state.tables:
            if st.session_state[f"table{table.id}"]:
                to_remove.append(table)
        # needs helper array to_remove, because when delete table by index, the other indexes decrease
        for t in to_remove:
            st.session_state.tables.remove(t)
            del st.session_state[f"table{t.id}"]
        clear_select()


def take_tables():
    """Make selected tables busy (for guests, who came without booking)"""
    if st.session_state.take_tables:
        for i, table in enumerate(st.session_state.tables):
            if st.session_state[f"table{table.id}"]:
                st.session_state.tables[i].free_seats = 0
        clear_select()


def new_table_create():
    """Create new table"""
    if st.session_state.new_table_create:
        name_value = st.session_state.new_table_name if st.session_state.new_table_name else "Table"
        # do not allow to create tables with similar names
        if not is_similar_table(name_value, st.session_state.tables):
            st.session_state.is_similar_tables = False
            new_table = Table(
                name=name_value,
                seats=st.session_state.new_table_seats,
                free_seats=st.session_state.new_table_seats,
                checked=False
            )
            st.session_state.tables.append(new_table)
            clear_select()
        else:
            st.session_state.is_similar_tables = True


def clear_select():
    """Clear all selected checkboxes after finishing action with tables"""
    for table in st.session_state.tables:
        table.checked = False
        st.session_state[f"table{table.id}"] = False
