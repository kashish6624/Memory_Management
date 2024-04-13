import os
import streamlit as st

# Function to allocate file space
def allocate_file_space(filename, size_bytes):
    try:
        with open(filename, 'wb') as file:
            file.seek(size_bytes - 1)
            file.write(b'\0')
    except:
        # If any error occurs, do not display it to the user
        pass

def allocate_main():
    st.title("File Space Allocator")

    while True:
        try:
            filename = st.text_input("Enter the filename:")
            size_str = st.text_input("Enter the size of the file in bytes:")

            size_bytes = int(size_str)

            abs_path = os.path.abspath(filename)

            # Allocate memory to the file
            allocate_file_space(filename, size_bytes)

            # Print the absolute path of the file
            st.write(f"Allocated {size_bytes} bytes for file: {abs_path}")

            # Ask user if they want to add another file
            choice = st.radio("Do you want to add another file?", ('Yes', 'No'))
            if choice == 'No':
                break
        except:
            # If any error occurs, do not display it to the user
            pass

if __name__ == "__main__":
    allocate_main()