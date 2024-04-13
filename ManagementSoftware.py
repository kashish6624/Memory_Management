import streamlit as st
from AllocateMemory import allocate_main
from DeallocateMemory import deallocate_main
from compress_stream import fileCompress_main
from decompress_stream import Decompress_main
from display_metadata_stream import Metadata_main
from memorystat_stream import Memory_main
from process_info import Process_main
from physicalRange import Range_main
from filees import File_main
from DiskSpecifications import disk_main
from MemorySpecifications import mem_main

def main():
    st.title("Memory Management Software")

    # Sidebar navigation
    option = st.sidebar.radio("Navigation", ["Welcome", "Memory Management", "File Management", "System Analysis", "System Specifications"])

    if option == "Welcome":
        st.header("Welcome")
        st.write("Please select an option from the sidebar.")

    elif option == "Memory Management":
        st.header("Memory Management")
        st.write("This section is for managing memory.")
        st.write("You can allocate or deallocate memory here.")

        # Add dropdown for memory management apps
        selected_app = st.sidebar.selectbox("Select Specification", ["Select Specification", "Allocate Memory", "Deallocate Memory"])

        # Check if an app is selected
        if selected_app != "Select Specification":
            # Execute the selected app
            if selected_app == "Allocate Memory":
                allocate_main()
            elif selected_app == "Deallocate Memory":
                deallocate_main()

    elif option == "File Management":
        st.header("File Management")
        st.write("This section is for managing files.")
        st.write("You can compress files and view metadata here.")

        # Add dropdown for file management apps
        selected_app = st.sidebar.selectbox("Select Specification", ["Select Specification", "Compress File","Decompress File", "Display MetaData"])

        # Check if an app is selected
        if selected_app != "Select Specification":
            # Execute the selected app
            if selected_app == "Compress File":
                fileCompress_main()
            elif selected_app == "Decompress File":
                Decompress_main()
            elif selected_app == "Display MetaData":
                Metadata_main()

    elif option == "System Analysis":
        st.header("System Analysis")
        st.write("This section is for analyzing system information.")
        st.write("You can view memory stats and process information here.")

        # Add dropdown for system analysis apps
        selected_app = st.sidebar.selectbox("Select Specification", ["Select Specification", "Memory Status", "Process Information", "Physical Range", "File Summary"])

        # Check if an app is selected
        if selected_app != "Select Specification":
            # Execute the selected app
            if selected_app == "Memory Status":
                Memory_main()
            elif selected_app == "Process Information":
                Process_main()
            elif selected_app == "Physical Range":
                Range_main()
            elif selected_app == "File Summary":
                File_main() 

    elif option == "System Specifications":
        st.header("System Specifications")
        st.write("This section is for viewing various system specifications.")

        # Add dropdown for different aspects of system specifications
        selected_app = st.sidebar.selectbox("Select Specification", ["Select Specification", "Disk Information", "RAM and Memory Information"])
        
        if selected_app != "Select Specification":
            if selected_app == "Disk Information":
                disk_main()
            elif selected_app == "RAM and Memory Information":
                mem_main()

if __name__ == "__main__":
    main()
