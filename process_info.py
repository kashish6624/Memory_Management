import streamlit as st
import psutil
import pandas as pd

def get_process_info(process):
    try:
        memory_info = process.memory_info()
        return {
            "Process ID": process.pid,
            "Name": process.name(),
            "Status": process.status(),
            "RSS (Resident Set Size)": memory_info.rss,
            "VMS (Virtual Memory Size)": memory_info.vms,
            "Number of Page Faults": memory_info.num_page_faults,
            "Peak Working Set Size": memory_info.peak_wset,
            "Working Set Size": memory_info.wset,
            "Peak Pagefile Usage": memory_info.peak_pagefile
        }
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return None

def Process_main():
    # st.set_page_config(page_title="Process Monitor")
    st.title("Process Monitor")
    st.write("## Process Information")

    # Get process information for the first 100 processes using list comprehension
    table_data = [get_process_info(process) for process in list(psutil.process_iter(['pid', 'name', 'status']))[:100] if get_process_info(process)]

    if table_data:
        df = pd.DataFrame(table_data)
        st.write(df)
    else:
        st.write("No running processes found.")

if __name__ == "__main__":
    Process_main()
