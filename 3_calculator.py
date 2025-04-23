import streamlit as st
from app_pages.multi_page import MultiPage  # Import the MultiPage class for managing multiple pages in the app

from app_pages.page_calculator import calculator_body  # Import the calculator page's content

# Create an instance of the MultiPage class with the app name "Calculator App"
app = MultiPage(app_name="Calculator App")

# Add the "Calculator" page to the app, linking it to the calculator_body function
app.add_page("Calculator", calculator_body)

# Run the Streamlit app
app.run()
