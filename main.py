import streamlit as st

import page_booking
import page_management
import page_status

st.title('Table booking app')

# Define initial state.
if "tables" not in st.session_state:

    st.session_state.tables = [
        {"name": "Table 1", "checked": False, "free": True, "seats": 4, 'free_seats': 4},
        {"name": "Table 2", "checked": False, "free": False, "seats": 5, 'free_seats': 3},
        {"name": "Table 3", "checked": False, "free": True, "seats": 6, 'free_seats': 6},
    ]

if "booking" not in st.session_state:
    st.session_state.booking = []


PAGES = {
    "Booking": page_booking,
    "Table management page": page_management,
    "Table status page": page_status
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.page()
