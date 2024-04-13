import streamlit as st
import zipfile
import os
import tempfile
import shutil

def decompress_zip_file(zip_file):
    """
    Decompresses a ZIP file and displays its content.
    
    Parameters:
        zip_file (UploadedFile): Uploaded ZIP file to decompress.
    """
    # Get the size of the original ZIP file
    original_size = zip_file.size
    st.write(f'Original file size: {original_size} bytes')
    
    # Create a temporary folder to extract files
    extracted_folder = tempfile.mkdtemp()
    try:
        # Extract the contents of the specified ZIP file
        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(extracted_folder)  # Extract to the temporary folder
        
        # Get the size of the decompressed files
        decompressed_size = sum(os.path.getsize(os.path.join(extracted_folder, f))
                                for f in os.listdir(extracted_folder))
        st.write(f'Decompressed file size: {decompressed_size} bytes')
        
        # List the contents of the decompressed files
        st.write("Contents of decompressed files:")
        for f in os.listdir(extracted_folder):
            st.write(f)

        # Optional: Open the decompressed files if they are text files
        for f in os.listdir(extracted_folder):
            file_path = os.path.join(extracted_folder, f)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as file:
                    st.write(f'\nContents of {f}:')
                    st.write(file.read())
    
    except Exception as e:
        # If any error occurs, do not display it to the user
        pass
    
    finally:
        # Clean up the temporary folder
        shutil.rmtree(extracted_folder)

def Decompress_main():
    st.title("ZIP File Decompression Tool")

    # File input widget to upload the ZIP file
    uploaded_file = st.file_uploader("Upload a ZIP file", type=["zip"])

    if uploaded_file is not None:
        # Call the decompress_zip_file function with the uploaded ZIP file
        decompress_zip_file(uploaded_file)

if __name__ == "__main__":
    Decompress_main()