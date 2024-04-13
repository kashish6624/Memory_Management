import streamlit as st
import psutil
import matplotlib.pyplot as plt

# Backend functions
def calculate_cached_memory():
    total_memory = psutil.virtual_memory().total
    used_memory = psutil.virtual_memory().used
    cached_memory = total_memory - used_memory
    return cached_memory

def get_use_counts():
    total_memory = psutil.virtual_memory().total
    usage_summary = {
        'Total Memory': total_memory,
        'Available Memory': psutil.virtual_memory().available,
        'Used Memory': psutil.virtual_memory().used,
        'Free Memory': psutil.virtual_memory().free,
        'Swap Total': psutil.swap_memory().total,
        'Swap Used': psutil.swap_memory().used,
        'Swap Free': psutil.swap_memory().free,
    }
    return usage_summary

# Frontend
def Memory_main():
    st.title("System Memory Information")

    # Display use counts
    st.header("Memory Usage Counts")
    usage_counts = get_use_counts()
    labels = list(usage_counts.keys())
    values = list(usage_counts.values())

    # Display memory usage counts data in a pie chart
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)

    # Display cached memory
    st.header("Cached Memory")
    cached_memory = calculate_cached_memory()
    st.write(f"Cached Memory: {cached_memory} bytes")

if __name__ == "__main__":
    Memory_main()