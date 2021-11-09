import streamlit as st

from components.Table import Table
from views.PageBooking import PageBooking
from views.PageManagement import PageManagement
from views.PageStatus import PageStatus

st.title('Table booking app')

# Define initial state
if "tables" not in st.session_state:
    table1 = Table(name="Table1", seats=12, free_seats=12, checked=False)
    table2 = Table(name="Table2", seats=10, free_seats=10, checked=False)
    table3 = Table(name="Table5", seats=8, free_seats=4, checked=False)
    st.session_state.tables = []
    st.session_state.tables.append(table1)
    st.session_state.tables.append(table2)
    st.session_state.tables.append(table3)

if "booking" not in st.session_state:
    st.session_state.booking = []

if "is_similar_tables" not in st.session_state:
    st.session_state.is_similar_tables = False


PAGES = {
    "Booking": PageBooking(),
    "Table management page": PageManagement(),
    "Table status page": PageStatus()
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.show_page()
