import requests
import os
from pathlib import Path

# Test server URL
BASE_URL = "http://localhost:8000"

def test_basic_upload():
    """Test basic file upload."""
    print("Testing basic file upload...")
    
    # Create a test file
    test_file_path = "test_file.txt"
    with open(test_file_path, "w") as f:
        f.write("This is a test file for upload.")
    
    try:
        with open(test_file_path, "rb") as f:
            files = {"file": f}
            response = requests.post(f"{BASE_URL}/upload/", files=files)
        
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        
    finally:
        # Clean up test file
        if os.path.exists(test_file_path):
            os.remove(test_file_path)

def test_multiple_upload():
    """Test multiple file upload."""
    print("\nTesting multiple file upload...")
    
    # Create test files
    test_files = []
    for i in range(3):
        filename = f"test_file_{i}.txt"
        with open(filename, "w") as f:
            f.write(f"This is test file {i}.")
        test_files.append(filename)
    
    try:
        files = [("files", open(f, "rb")) for f in test_files]
        response = requests.post(f"{BASE_URL}/upload-multiple/", files=files)
        
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        
    finally:
        # Clean up test files
        for filename in test_files:
            if os.path.exists(filename):
                os.remove(filename)

def test_upload_with_data():
    """Test file upload with additional form data."""
    print("\nTesting file upload with metadata...")
    
    # Create a test file
    test_file_path = "test_metadata.txt"
    with open(test_file_path, "w") as f:
        f.write("This is a test file with metadata.")
    
    try:
        with open(test_file_path, "rb") as f:
            files = {"file": f}
            data = {
                "description": "Test file with metadata",
                "category": "test"
            }
            response = requests.post(f"{BASE_URL}/upload-with-data/", files=files, data=data)
        
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        
    finally:
        # Clean up test file
        if os.path.exists(test_file_path):
            os.remove(test_file_path)

def test_file_validation():
    """Test file validation."""
    print("\nTesting file validation...")
    
    # Create a test file
    test_file_path = "test_validation.txt"
    with open(test_file_path, "w") as f:
        f.write("This is a test file for validation.")
    
    try:
        with open(test_file_path, "rb") as f:
            files = {"file": f}
            data = {"max_size_mb": 1}  # 1MB limit
            response = requests.post(f"{BASE_URL}/upload-validated/", files=files, data=data)
        
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        
    finally:
        # Clean up test file
        if os.path.exists(test_file_path):
            os.remove(test_file_path)

def test_list_files():
    """Test listing uploaded files."""
    print("\nTesting file listing...")
    
    response = requests.get(f"{BASE_URL}/files/")
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

def test_download_file():
    """Test downloading a file."""
    print("\nTesting file download...")
    
    # First, upload a file
    test_file_path = "test_download.txt"
    with open(test_file_path, "w") as f:
        f.write("This is a test file for download.")
    
    try:
        # Upload the file
        with open(test_file_path, "rb") as f:
            files = {"file": f}
            response = requests.post(f"{BASE_URL}/upload/", files=files)
        
        if response.status_code == 200:
            filename = response.json()["filename"]
            
            # Download the file
            download_response = requests.get(f"{BASE_URL}/download/{filename}")
            print(f"Download Status: {download_response.status_code}")
            
            if download_response.status_code == 200:
                # Save downloaded file
                with open(f"downloaded_{filename}", "wb") as f:
                    f.write(download_response.content)
                print(f"File downloaded as: downloaded_{filename}")
        
    finally:
        # Clean up test file
        if os.path.exists(test_file_path):
            os.remove(test_file_path)

if __name__ == "__main__":
    print("FastAPI File Upload Test")
    print("=" * 40)
    
    try:
        # Test basic upload
        test_basic_upload()
        
        # Test multiple upload
        test_multiple_upload()
        
        # Test upload with metadata
        test_upload_with_data()
        
        # Test file validation
        test_file_validation()
        
        # Test listing files
        test_list_files()
        
        # Test downloading
        test_download_file()
        
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to server. Make sure the FastAPI server is running.")
        print("Run: python fastapi_upload_example.py")
    except Exception as e:
        print(f"Error: {e}")
    
    print("\nTest completed!") 
 