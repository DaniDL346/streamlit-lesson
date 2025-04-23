# Create a function named calculator_body()
# Within it, create 3 columns using the st.columns() function
# Note, in the video, this column function was still in beta
    
import streamlit as st

def calculator_body():
    st.write("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        num1 = st.number_input(label="Enter the first number", step=1)
    with col2:
        num2 = st.number_input(label="Enter the second number", step=1)
    with col3:
        operation = st.selectbox(label="Select an operation", options=["Addition", "Subtraction", "Multiplication", "Division"])     

    if st.button("Click here for the maths"):
        if num2 == 0 and operation == "Division":
            st.error("Cannot divide by zero. Try again")
        else:
            calculator_function(num1,num2, operation)

def calculator_function(num1, num2, operation):
    """
    Perform a basic arithmetic operation (Addition, Subtraction, Multiplication, or Division) 
    on two numbers and display the result using Streamlit.

    Args:
        num1 (float): The first number for the operation.
        num2 (float): The second number for the operation.
        operation (str): The arithmetic operation to perform. 
                         Accepted values are "Addition", "Subtraction", "Multiplication", and "Division".

    Returns:
        None: The function displays the result using Streamlit's `st.success` or an error message 
              using `st.error` if the operation is invalid.

    Raises:
        ZeroDivisionError: If the operation is "Division" and `num2` is zero.
    """
    if operation == "Addition":
        result = num1 + num2
        st.success(f"The sum of {num1} and {num2} is: **{result}**")
    elif operation == "Subtraction":
        result = num1 - num2
        st.success(f"The difference of {num1} and {num2} is: **{result}**")
    elif operation == "Multiplication":
        result = num1 * num2
        st.success(f"The product of {num1} and {num2} is: **{result}**")
    elif operation == "Division":
        result = num1 / num2
        st.success(f"The quotient of {num1} and {num2} is: **{result}**")
    else:
        st.error("Invalid operation. Please try again.")

    