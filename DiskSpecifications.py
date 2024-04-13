import psutil
import streamlit as st

def get_disk_details():
    partitions = psutil.disk_partitions()
    disk_info = []
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            disk_info.append({
                "Device": partition.device,
                "Mountpoint": partition.mountpoint,
                "File System Type": partition.fstype,
                "Total Size (GB)": round(usage.total / (1024 ** 3), 2),
                "Used Size (GB)": round(usage.used / (1024 ** 3), 2),
                "Free Size (GB)": round(usage.free / (1024 ** 3), 2),
                "Percentage Used": usage.percent
            })
        except PermissionError:
            # This can happen due to restricted access
            pass
    return disk_info

def disk_main():
    st.title("Disk Details")

    disk_info = get_disk_details()

    if disk_info:
        st.write("### Disk Information:")
        st.write(disk_info)
    else:
        st.write("No disk information available.")

if __name__ == "__main__":
    disk_main()
