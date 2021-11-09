# Booking app

run local: `streamlit run main.py`

deploy: https://oop-booking-app.herokuapp.com/

This application is designed to manage tables and reservations.

## The main functionality
`PageBooking` - reservation page. It is possible to book the selected table by indicating the name, phone number, date, time and duration of the reservation. You can also see a list of free tables and a list of existing reservations.

`PageManagement` - tables management page. You can perform operations with current tables - mark tables as occupied, mark tables as free, remove tables from the list. Operations can be carried out with one table or with several tables at the same time. You can also add a new table by specifying its name and number of seats.

`PageStatus` - page for displaying the status of tables. It is possible to view the list of tables and view the total number of free seats and free tables.

## Application structure

* The entities `Table` and `BookingItem` are described using classes.

* Pages are wrapped in classes, which are inherited from an abstract base class. Inside the pages, there is code responsible for rendering.

* Data storage is organized through `session_state`. 

* Data processing logic in `session_state` is placed in controllers - `booking_controller.py` and `tables_controller.py`. 

* Linking interface elements to data and reactivity is organized through `session_state`. 

* Reactivity to user clicks is implemented through callbacks.

* A sidebar with radio buttons is used to switch pages.

* The auxiliary functions are located in the file `utils.py`.

