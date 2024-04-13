import streamlit as st
import os
import datetime
import hashlib
from langdetect import detect
import fitz  # PyMuPDF


def get_file_metadata(file_path):
    metadata = {}
    if os.path.exists(file_path):
        metadata['File Name'] = os.path.basename(file_path)
        metadata['File Type'] = os.path.splitext(file_path)[1].replace('.', '').upper()
        metadata['File Size'] = os.path.getsize(file_path)
        metadata['Creation Date'] = datetime.datetime.fromtimestamp(os.path.getctime(file_path))
        metadata['Last Modified Date'] = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))
        metadata['File Permissions'] = oct(os.stat(file_path).st_mode)[-3:]
        metadata['File Location'] = os.path.dirname(file_path)
        metadata['Checksums'] = calculate_checksums(file_path)
        metadata['Language'] = detect_language(file_path)
        return metadata
    else:
        st.error("File not found.")
        return None


def calculate_checksums(file_path):
    checksums = {}
    algorithms = ['md5', 'sha1', 'sha256']
    for algorithm in algorithms:
        checksums[algorithm] = calculate_checksum(file_path, algorithm)
    return checksums


def calculate_checksum(file_path, algorithm='md5'):
    checksum = None
    try:
        hasher = hashlib.new(algorithm)
        with open(file_path, 'rb') as f:
            while True:
                chunk = f.read(4096)
                if not chunk:
                    break
                hasher.update(chunk)
        checksum = hasher.hexdigest()
    except Exception as e:
        st.warning(f"Error: {e}")
    return checksum


def detect_language(file_path):
    language = None
    if os.path.exists(file_path):
        try:
            with open(file_path, 'rb') as f:
                # Read the file as binary
                content = f.read()
                # Decode the content, ignoring errors and replacing with a placeholder character
                text = content.decode('utf-8', errors='replace')
                # Detect the language of the decoded text
                language = detect(text)
        except Exception as e:
            st.warning(f"Error: {e}")
    return language


def Metadata_main():
    st.title("File Metadata Viewer")
    file_path = st.text_input("Enter the file path:")

    if st.button("Get Metadata"):
        if file_path:
            metadata = get_file_metadata(file_path)
            if metadata:
                st.write("### File Metadata:")
                for key, value in metadata.items():
                    st.write(f"{key}:** {value}")
        else:
            st.warning("Please enter a file path.")


if __name__ == "__main__":
    Metadata_main()