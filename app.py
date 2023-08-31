import streamlit as st

def find_largest(n1, n2, n3):
    return max(n1, n2, n3)

def main():
    st.title("Find the Largest Number")
    
    n1 = st.number_input("Enter number1:")
    n2 = st.number_input("Enter number2:")
    n3 = st.number_input("Enter number3:")
    
    if st.button("Find Largest"):
        largest = find_largest(n1, n2, n3)
        st.write(f"The largest number is: {largest}")

if _name_ == "_main_":
    main()
