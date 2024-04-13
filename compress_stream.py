import streamlit as st
import zipfile
import os

def compress_file(file_path, zip_path):
    """
    Compresses a file to a ZIP archive.

    Parameters:
        file_path (str): Path to the file to be compressed.
        zip_path (str): Path to save the resulting ZIP archive.

    Returns:
        str: Path to the created ZIP archive.
    """
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(file_path, os.path.basename(file_path))
        return zip_path
    except Exception as e:
        st.error(f"Error occurred while compressing the file: {e}")
        return None

def fileCompress_main():
    st.title("File Compression")

    file_to_compress = st.text_input("Enter the path of the file to compress:")
    compressed_file = st.text_input("Enter the path to save the compressed file (including filename with .zip extension):")

    if st.button("Compress File"):
        if not file_to_compress or not compressed_file:
            st.warning("Please enter both the file path and the path to save the compressed file.")
        elif not os.path.isfile(file_to_compress):
            st.error("Error: The specified file does not exist or it is a directory.")
        else:
            result = compress_file(file_to_compress, compressed_file)
            if result:
                st.success(f"File compressed and saved as: {result}")

if __name__ == "__main__":
    fileCompress_main()

