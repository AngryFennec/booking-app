import streamlit as st

from components.BookingItem import BookingItem
from utils import get_table_name_from_select, get_table_id_from_select


def submit_form():
    """Save booking to state"""
    # check selected option too - if it's not select (maybe because of no free tables), don't take booking
    if st.session_state.submit_form and st.session_state.selected_table:
        name_value = st.session_state.guest_name if st.session_state.guest_name else "Noname"
        phone_value = st.session_state.guest_phone if st.session_state.guest_phone else "-"
        booking_item = BookingItem(
            name=name_value,
            phone=phone_value,
            visit_date=st.session_state.visit_date,
            start_time=st.session_state.start_time,
            period=st.session_state.period,
            table=get_table_name_from_select(st.session_state.selected_table)
        )
        st.session_state.booking.append(booking_item)
        table_index = get_table_id_from_select(st.session_state.selected_table, st.session_state.tables)
        st.session_state.tables[table_index].free_seats = 0
