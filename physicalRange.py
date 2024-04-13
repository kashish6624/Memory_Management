import streamlit as st
import ctypes
from ctypes import wintypes

def get_physical_ranges():
    try:
        # Define the SYSTEM_INFO structure
        class SYSTEM_INFO(ctypes.Structure):
            _fields_ = [
                ("wProcessorArchitecture", wintypes.WORD),
                ("wReserved", wintypes.WORD),
                ("dwPageSize", wintypes.DWORD),
                ("lpMinimumApplicationAddress", wintypes.LPVOID),
                ("lpMaximumApplicationAddress", wintypes.LPVOID),
                ("dwActiveProcessorMask", wintypes.LPVOID),
                ("dwNumberOfProcessors", wintypes.DWORD),
                ("dwProcessorType", wintypes.DWORD),
                ("dwAllocationGranularity", wintypes.DWORD),
                ("wProcessorLevel", wintypes.WORD),
                ("wProcessorRevision", wintypes.WORD)
            ]

        # Get the system information
        system_info = SYSTEM_INFO()
        ctypes.windll.kernel32.GetSystemInfo(ctypes.byref(system_info))

        # Prepare data for display
        data = {
            "Parameter": ["Minimum Address", "Maximum Address", "Page Size"],
            "Value": [hex(int(system_info.lpMinimumApplicationAddress)),
                      hex(int(system_info.lpMaximumApplicationAddress)),
                      system_info.dwPageSize]
        }

        return data

    except Exception as e:
        return {"Parameter": ["Error"], "Value": [str(e)]}

def Range_main():
    st.title("System Information")

    # Call the get_physical_ranges function to retrieve system information
    data = get_physical_ranges()

    # Set up Streamlit layout
    st.markdown("---")
    st.write("### Physical Memory Ranges")
    st.write("Below is the information about physical memory ranges:")
    st.markdown("---")

    # Display the data
    st.table(data)

if __name__ == "__main__":
    Range_main()
