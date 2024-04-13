import psutil
import streamlit as st

def get_ram_details():
    svmem = psutil.virtual_memory()
    return {
        "Total RAM (GB)": round(svmem.total / (1024 ** 3), 2),
        "Available RAM (GB)": round(svmem.available / (1024 ** 3), 2),
        "Used RAM (GB)": round(svmem.used / (1024 ** 3), 2),
        "Free RAM (GB)": round(svmem.free / (1024 ** 3), 2),
        "RAM Usage Percentage": svmem.percent
    }

def get_memory_details():
    vm = psutil.virtual_memory()
    svmem = psutil.swap_memory()
    return {
        "Total Physical Memory (GB)": round(vm.total / (1024 ** 3), 2),
        "Used Physical Memory (GB)": round((vm.total - vm.available) / (1024 ** 3), 2),
        "Free Physical Memory (GB)": round(vm.available / (1024 ** 3), 2),
        "Total Virtual Memory (GB)": round(svmem.total / (1024 ** 3), 2),
        "Used Virtual Memory (GB)": round(svmem.used / (1024 ** 3), 2),
        "Free Virtual Memory (GB)": round(svmem.free / (1024 ** 3), 2),
    }

def mem_main():
    st.title("Memory Specifications")

    ram_info = get_ram_details()
    memory_info = get_memory_details()

    st.write("### RAM Information:")
    st.write(ram_info)

    st.write("### Memory Information:")
    st.write(memory_info)

if __name__ == "__main__":
    mem_main()
