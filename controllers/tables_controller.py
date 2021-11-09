import streamlit as st

from components.Table import Table


def release_tables():
    """Make all seats of selected tables free"""
    if st.session_state.release_tables:
        for i, table in enumerate(st.session_state.tables):
            if st.session_state[f"table{table.name}"]:
                st.session_state.tables[i].free_seats = table.seats
        clear_select()


def remove_tables():
    """Remove selected tables from tables list"""
    if st.session_state.remove_tables:
        to_remove = []
        for table in st.session_state.tables:
            if st.session_state[f"table{table.name}"]:
                to_remove.append(table)
        for t in to_remove:
            st.session_state.tables.remove(t)
            del st.session_state[f"table{t.name}"]
        clear_select()


def take_tables():
    """Make selected tables busy (for guests, who came without booking)"""
    if st.session_state.take_tables:
        for i, table in enumerate(st.session_state.tables):
            if st.session_state[f"table{table.name}"]:
                st.session_state.tables[i].free_seats = 0
        clear_select()


def new_table_create():
    """Create new table"""
    if st.session_state.new_table_create:
        new_table = Table(
            name=st.session_state.new_table_name,
            seats=st.session_state.new_table_seats,
            free_seats=st.session_state.new_table_seats,
            free=True,
            checked=False
        )
        st.session_state.tables.append(new_table)
        clear_select()


def clear_select():
    """Clear all selected checkboxes after finishing action with tables"""
    for table in st.session_state.tables:
        table.checked = False
        st.session_state[f"table{table.name}"] = False
