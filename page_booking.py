import streamlit as st

from utils import get_table_name_from_select, get_table_id_from_select


def page():
    def submit_form():
        if st.session_state.submit_form:
            st.session_state.booking.append({
                "name": st.session_state.guest_name,
                "phone": st.session_state.guest_phone,
                "start_time": st.session_state.start_time,
                "period": st.session_state.period,
                "table:": get_table_name_from_select(st.session_state.selected_table)
            })
            table_index = get_table_id_from_select(st.session_state.selected_table, st.session_state.tables)
            st.session_state.tables[table_index]["free_seats"] = 0

    st.subheader("Booking")
    st.text_input("Guest name", key="guest_name")
    st.text_input("Guest phone", key="guest_phone")

    time_col1, time_col2 = st.columns([1, 1])
    with time_col1:
        st.selectbox("Start time", options=['12:00', '13:00', '14:00', '15:00'], key="start_time")
    with time_col2:
        st.number_input('Booking period', key="period", min_value=0)

    st.selectbox("Table", options=[f'{table["name"]} - {table["seats"]} seats' for table in
                                   filter(lambda table: table["free_seats"] == table["seats"],
                                          st.session_state.tables)], key="selected_table")
    st.button('Submit', on_click=submit_form, key="submit_form")

    # Show all free tables.
    st.write("")
    st.subheader("List of free tables")
    for table in st.session_state.tables:
        if table["free_seats"] == table["seats"]:
            st.write(f'{table["name"]} - Free')
