import streamlit as st

from controllers.tables_controller import take_tables, release_tables, remove_tables, new_table_create
from views.AbstractPage import AbstractPage


def write_tables_list(tables):
    st.write("")
    col11, col12, _ = st.columns([0.05, 0.8, 0.15])
    for i, table in enumerate(tables):
        done = col11.checkbox("", table.checked, key=f"table{table.name}")
        if done:
            table.checked = True
        col12.markdown(f'{table.name} - Free {table.free_seats}', unsafe_allow_html=True)


class PageManagement(AbstractPage):

    def show_page(self):
        st.header("List of tables")
        st.text("You can choose one or several tables to make changes")

        # Show all tables.
        write_tables_list(st.session_state.tables)

        st.write("")
        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
        with col1:
            st.button("Take tables", on_click=take_tables, key="take_tables")
        with col2:
            st.button("Release tables", on_click=release_tables, key="release_tables")
        with col4:
            st.button("Remove tables", on_click=remove_tables, key="remove_tables")

        st.header("Add new table")
        st.text_input("Table name", key="new_table_name")
        st.number_input("Table seats", key="new_table_seats", min_value=1)
        st.button("Add table", on_click=new_table_create, key="new_table_create")
