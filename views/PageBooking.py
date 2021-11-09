import streamlit as st

from controllers.booking_controller import submit_form
from views.AbstractPage import AbstractPage


class PageBooking(AbstractPage):
    """Class for booking page"""

    def show_page(self):
        """Implemented method for showing booking page"""

        # Show fields for creating new booking item
        st.subheader("Booking")
        st.text_input("Guest name", key="guest_name")
        st.text_input("Guest phone", key="guest_phone")

        time_col1, time_col2, time_col3 = st.columns([1, 1, 1])
        with time_col1:
            st.date_input("Visit date", key="visit_date")
        with time_col2:
            st.time_input("Start time", key="start_time")
        with time_col3:
            st.number_input('Booking period', key="period", min_value=1)

        st.selectbox("Table", options=[f'{table.name} - {table.seats} seats' for table in
                                       filter(lambda table: table.free_seats == table.seats,
                                              st.session_state.tables)], key="selected_table")
        st.button('Submit', on_click=submit_form, key="submit_form")

        # Show all free tables
        st.write("")
        st.subheader("List of free tables")
        for table in st.session_state.tables:
            if table.free_seats == table.seats:
                st.write(f'{table.name} - Free')

        # Show all booking items
        st.write("")
        st.subheader("List of booking")
        col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1, 1])
        with col1:
            st.write("Guest name")
        with col2:
            st.write("Guest phone")
        with col3:
            st.write("Date")
        with col4:
            st.write("Time")
        with col5:
            st.write("Period")
        with col6:
            st.write("Table")
        for booking_item in st.session_state.booking:
            with col1:
                st.write(booking_item.name)
            with col2:
                st.write(booking_item.phone)
            with col3:
                st.write(booking_item.visit_date)
            with col4:
                st.write(booking_item.start_time)
            with col5:
                st.write(booking_item.period)
            with col6:
                st.write(booking_item.table)
