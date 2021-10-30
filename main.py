import streamlit as st

from components.Table import Table
from views.PageBooking import PageBooking
from views.PageManagement import PageManagement
from views.PageStatus import PageStatus

st.title('Table booking app')

# Define initial state.
if "tables" not in st.session_state:
    table1 = Table(name="Table1", seats=12, free_seats=12, checked=False, free=True)
    table2 = Table(name="Table2", seats=10, free_seats=10, checked=False, free=True)
    table3 = Table(name="Table5", seats=8, free_seats=4, checked=False, free=False)
    st.session_state.tables = []
    st.session_state.tables.append(table1)
    st.session_state.tables.append(table2)
    st.session_state.tables.append(table3)

    # st.session_state.tables = [
    #     {"name": "Table 1", "checked": False, "free": True, "seats": 4, 'free_seats': 4},
    #     {"name": "Table 2", "checked": False, "free": False, "seats": 5, 'free_seats': 3},
    #     {"name": "Table 3", "checked": False, "free": True, "seats": 6, 'free_seats': 6},
    # ]

if "booking" not in st.session_state:
    st.session_state.booking = []


PAGES = {
    "Booking": PageBooking(),
    "Table management page": PageManagement(),
    "Table status page": PageStatus()
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.show_page()
