import os
import streamlit as st

# Disable error message display in Streamlit
st.set_option('client.showErrorDetails', False)

# Function to deallocate file space
def deallocate_file_space(filename):
    try:
        if os.path.exists(filename):  # Check if the file exists before trying to remove it
            os.remove(filename)
            st.write(f"Memory deallocated for file: {filename}")
        else:
            st.write(f"File '{filename}' does not exist.")
    except Exception as e:
        st.write(f"Error occurred while deallocating memory for file '{filename}': {e}")

def deallocate_main():
    st.title("File Space Deallocator")

    filename = st.text_input("Enter the filename to deallocate memory:")
    if st.button("Deallocate Memory"):
        # Deallocate memory for the file
        deallocate_file_space(filename)

if __name__ == "__main__":
    deallocate_main()
