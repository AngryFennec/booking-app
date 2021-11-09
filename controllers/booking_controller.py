import streamlit as st

from components.BookingItem import BookingItem
from utils import get_table_name_from_select, get_table_id_from_select


def submit_form():
    """Save booking to state"""
    if st.session_state.submit_form:
        booking_item = BookingItem(
            name=st.session_state.guest_name,
            phone=st.session_state.guest_phone,
            visit_date=st.session_state.visit_date,
            start_time=st.session_state.start_time,
            period=st.session_state.period,
            table=get_table_name_from_select(st.session_state.selected_table)
        )
        st.session_state.booking.append(booking_item)
        table_index = get_table_id_from_select(st.session_state.selected_table, st.session_state.tables)
        st.session_state.tables[table_index].free_seats = 0
