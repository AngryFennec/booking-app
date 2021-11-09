import streamlit as st

from views.AbstractPage import AbstractPage


class PageStatus(AbstractPage):

    def show_page(self):
        """Implemented method for showing status page"""
        st.header("Status page")
        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
        with col1:
            st.write("Table name")
        with col2:
            st.write("Total seats")
        with col3:
            st.write("Free seats")
        with col4:
            st.write("Is free")
        for table in st.session_state.tables:
            with col1:
                st.write(table.name)
            with col2:
                st.write(table.seats)
            with col3:
                st.write(table.free_seats)
            with col4:
                st.write(table.seats == table.free_seats)

        st.write("")

        # Show number of free seats and free tables
        st.markdown(
            f"#### Number of free tables - {len(list(filter(lambda t: t.seats == t.free_seats, st.session_state.tables)))}")
        st.markdown(f"#### Number of free seats - {sum(t.free_seats for t in st.session_state.tables)}")
