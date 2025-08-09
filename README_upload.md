# FastAPI File Upload Examples

This project demonstrates various file upload functionalities using FastAPI and `UploadFile`.

## Features

- ✅ Single file upload
- ✅ Multiple files upload
- ✅ File upload with metadata
- ✅ File validation (size, type)
- ✅ Async file handling
- ✅ File download
- ✅ File listing and management

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
python fastapi_upload_example.py
```

The server will start at `http://localhost:8000`

## API Endpoints

### 1. Basic File Upload
```http
POST /upload/
Content-Type: multipart/form-data

file: [file]
```

### 2. Multiple Files Upload
```http
POST /upload-multiple/
Content-Type: multipart/form-data

files: [file1, file2, ...]
```

### 3. Upload with Metadata
```http
POST /upload-with-data/
Content-Type: multipart/form-data

file: [file]
description: string
category: string (optional, default: "general")
```

### 4. Validated Upload
```http
POST /upload-validated/
Content-Type: multipart/form-data

file: [file]
max_size_mb: integer (optional, default: 10)
```

### 5. Download File
```http
GET /download/{filename}
```

### 6. List Files
```http
GET /files/
```

### 7. Delete File
```http
DELETE /files/{filename}
```

## Usage Examples

### Python Requests Example
```python
import requests

# Basic upload
with open('file.txt', 'rb') as f:
    files = {'file': f}
    response = requests.post('http://localhost:8000/upload/', files=files)
    print(response.json())

# Upload with metadata
with open('file.txt', 'rb') as f:
    files = {'file': f}
    data = {'description': 'My file', 'category': 'documents'}
    response = requests.post('http://localhost:8000/upload-with-data/', 
                           files=files, data=data)
    print(response.json())
```

### cURL Examples
```bash
# Basic upload
curl -X POST "http://localhost:8000/upload/" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@/path/to/file.txt"

# Multiple files
curl -X POST "http://localhost:8000/upload-multiple/" \
     -H "Content-Type: multipart/form-data" \
     -F "files=@/path/to/file1.txt" \
     -F "files=@/path/to/file2.txt"

# Upload with metadata
curl -X POST "http://localhost:8000/upload-with-data/" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@/path/to/file.txt" \
     -F "description=My file description" \
     -F "category=documents"
```

## HTML Form Testing

Open `upload_form.html` in your browser to test the upload functionality with a web interface.

## Key Features Explained

### 1. UploadFile vs File
- `UploadFile`: Spooled file that can be read multiple times
- `File`: Direct file access, can only be read once

### 2. File Validation
- Size limits
- Type checking
- Filename validation
- Content-type validation

### 3. Async Handling
- Use `aiofiles` for large files
- Non-blocking file operations
- Better memory management

### 4. Error Handling
- Proper HTTP status codes
- Detailed error messages
- Exception handling

## File Storage

Files are stored in the `uploads/` directory. The application:
- Creates unique filenames to avoid conflicts
- Stores metadata in JSON files
- Provides file management endpoints

## Security Considerations

1. **File Size Limits**: Set appropriate max file sizes
2. **File Type Validation**: Only allow safe file types
3. **Filename Sanitization**: Prevent path traversal attacks
4. **Storage Limits**: Monitor disk space usage
5. **Access Control**: Implement authentication if needed

## Performance Tips

1. **Use async operations** for large files
2. **Stream files** instead of loading into memory
3. **Implement chunked uploads** for very large files
4. **Use CDN** for static file serving
5. **Compress files** when appropriate

## Common Issues

### 1. File Not Found
- Check if file exists in uploads directory
- Verify filename encoding

### 2. Permission Errors
- Ensure uploads directory is writable
- Check file permissions

### 3. Memory Issues
- Use streaming for large files
- Implement file size limits

### 4. CORS Issues
- Configure CORS middleware for web clients
- Set appropriate headers

## Advanced Usage

### Custom File Processing
```python
@app.post("/upload-process/")
async def upload_and_process(file: UploadFile = File(...)):
    # Read file content
    content = await file.read()
    
    # Process the file
    processed_content = process_file(content)
    
    # Save processed file
    processed_path = UPLOAD_DIR / f"processed_{file.filename}"
    with open(processed_path, "wb") as f:
        f.write(processed_content)
    
    return {"message": "File processed successfully"}
```

### Database Integration
```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Store file metadata in database
@app.post("/upload-db/")
async def upload_to_db(file: UploadFile = File(...)):
    # Save file
    file_path = UPLOAD_DIR / file.filename
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    
    # Store metadata in database
    file_record = FileRecord(
        filename=file.filename,
        size=file.size,
        path=str(file_path)
    )
    db.add(file_record)
    db.commit()
    
    return {"id": file_record.id, "filename": file.filename}
``` 