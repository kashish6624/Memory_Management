import streamlit as st
import psutil
import pandas as pd

def get_file_summary_and_details():
    file_summary = {}
    file_details = {}
    file_counter = 0  # Counter to track the number of files processed

    # Get a list of all processes
    processes = psutil.process_iter(['pid', 'name', 'memory_maps'])

    # Iterate over each process
    for process in processes:
        try:
            memory_maps = process.memory_maps()
        except psutil.AccessDenied:
            # Skip processes where access to memory maps is denied
            continue
        
        # Iterate over memory maps for each process
        for mem_map in memory_maps:
            # Check if the memory map is valid
            if not hasattr(mem_map, 'path'):
                continue
                
            file_path = mem_map.path

            # Update file summary
            if file_path in file_summary:
                file_summary[file_path] += 1
            else:
                file_summary[file_path] = 1

            # Update file details
            if file_path in file_details:
                file_details[file_path].append(mem_map)
            else:
                file_details[file_path] = [mem_map]
            
            # Increment the file counter
            file_counter += 1
            
            # Check if 250 files have been processed
            if file_counter >= 250:
                break
    
        # Check if 250 files have been processed
        if file_counter >= 250:
            break
    
    return file_summary, file_details

# Function to create and display file summary table
def display_file_summary_table(file_summary, file_details):
    data = []
    for file_path, count in file_summary.items():
        rss_values = [detail.rss for detail in file_details[file_path]]
        rss_str = ', '.join(map(str, rss_values))
        data.append((file_path, count, rss_str))

    df = pd.DataFrame(data, columns=['File Path', 'Instances', 'RSS'])
    st.write(df)

# Main function
def File_main():
    st.title("File Summary Viewer")
    file_summary, file_details = get_file_summary_and_details()
    display_file_summary_table(file_summary, file_details)

if __name__ == "__main__":
    File_main()