import streamlit as st


def page():
    def new_table_create():
        if st.session_state.new_table_create:
            st.session_state.tables.append(
                {
                    "name": st.session_state.new_table_name,
                    "seats": st.session_state.new_table_seats,
                    "free_seats": st.session_state.new_table_seats,
                    "free": True,
                    "checked": False,
                }
            )
            clear_select()

    def take_tables():
        if st.session_state.take_tables:
            for i, table in enumerate(st.session_state.tables):
                if st.session_state[f"table{table['name']}"]:
                    st.session_state.tables[i]["free_seats"] = 0
            clear_select()

    def release_tables():
        if st.session_state.release_tables:
            for i, table in enumerate(st.session_state.tables):
                if st.session_state[f"table{table['name']}"]:
                    st.session_state.tables[i]["free_seats"] = table["seats"]
            clear_select()

    def remove_tables():
        if st.session_state.remove_tables:
            to_remove = []
            for table in st.session_state.tables:
                if st.session_state[f"table{table['name']}"]:
                    to_remove.append(table)
            for t in to_remove:
                st.session_state.tables.remove(t)
                del st.session_state[f"table{t['name']}"]
            clear_select()

    st.header("Add new table")

    # Show all tables.
    write_todo_list(st.session_state.tables)

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


def write_todo_list(tables):
    st.write("")
    col11, col12, _ = st.columns([0.05, 0.8, 0.15])
    for i, table in enumerate(tables):
        done = col11.checkbox("", table["checked"], key=f"table{table['name']}")
        if done:
            table["checked"] = True
        col12.markdown(
            f'{table["name"]} - Free {table["free_seats"]}',
            unsafe_allow_html=True,
        )


def clear_select():
    for table in st.session_state.tables:
        table["checked"] = False
