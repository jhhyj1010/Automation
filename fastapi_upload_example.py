from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.responses import FileResponse
import shutil
import os
from pathlib import Path
from typing import List, Optional
import aiofiles
import json

app = FastAPI(title="File Upload API", version="1.0.0")

# Create upload directory
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.get("/")
async def root():
    return {"message": "File Upload API"}

# Basic single file upload
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    """
    Upload a single file.
    
    Args:
        file: The file to upload
        
    Returns:
        dict: File information
    """
    try:
        # Validate file
        if not file.filename:
            raise HTTPException(status_code=400, detail="No file provided")
        
        # Create file path
        file_path = UPLOAD_DIR / file.filename
        
        # Save file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        return {
            "filename": file.filename,
            "size": file.size,
            "content_type": file.content_type,
            "saved_path": str(file_path)
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")

# Multiple files upload
@app.post("/upload-multiple/")
async def upload_multiple_files(files: List[UploadFile] = File(...)):
    """
    Upload multiple files.
    
    Args:
        files: List of files to upload
        
    Returns:
        dict: Files information
    """
    try:
        uploaded_files = []
        
        for file in files:
            if not file.filename:
                continue
            
            # Create unique filename to avoid conflicts
            file_path = UPLOAD_DIR / f"{file.filename}"
            counter = 1
            while file_path.exists():
                name, ext = os.path.splitext(file.filename)
                file_path = UPLOAD_DIR / f"{name}_{counter}{ext}"
                counter += 1
            
            # Save file
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            
            uploaded_files.append({
                "filename": file.filename,
                "size": file.size,
                "content_type": file.content_type,
                "saved_path": str(file_path)
            })
        
        return {
            "message": f"Successfully uploaded {len(uploaded_files)} files",
            "files": uploaded_files
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")

# File upload with additional form data
@app.post("/upload-with-data/")
async def upload_file_with_data(
    file: UploadFile = File(...),
    description: str = Form(...),
    category: str = Form("general")
):
    """
    Upload file with additional metadata.
    
    Args:
        file: The file to upload
        description: File description
        category: File category
        
    Returns:
        dict: File and metadata information
    """
    try:
        if not file.filename:
            raise HTTPException(status_code=400, detail="No file provided")
        
        # Create file path
        file_path = UPLOAD_DIR / file.filename
        
        # Save file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Save metadata
        metadata = {
            "filename": file.filename,
            "description": description,
            "category": category,
            "size": file.size,
            "content_type": file.content_type,
            "saved_path": str(file_path)
        }
        
        metadata_path = UPLOAD_DIR / f"{file.filename}.json"
        with open(metadata_path, "w") as f:
            json.dump(metadata, f, indent=2)
        
        return metadata
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")

# Async file upload (for large files)
@app.post("/upload-async/")
async def upload_file_async(file: UploadFile = File(...)):
    """
    Upload file asynchronously (better for large files).
    
    Args:
        file: The file to upload
        
    Returns:
        dict: File information
    """
    try:
        if not file.filename:
            raise HTTPException(status_code=400, detail="No file provided")
        
        file_path = UPLOAD_DIR / file.filename
        
        # Async file writing
        async with aiofiles.open(file_path, "wb") as buffer:
            content = await file.read()
            await buffer.write(content)
        
        return {
            "filename": file.filename,
            "size": file.size,
            "content_type": file.content_type,
            "saved_path": str(file_path)
        }
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")

# File validation and type checking
@app.post("/upload-validated/")
async def upload_validated_file(
    file: UploadFile = File(...),
    max_size_mb: int = Form(10)
):
    """
    Upload file with validation.
    
    Args:
        file: The file to upload
        max_size_mb: Maximum file size in MB
        
    Returns:
        dict: File information
    """
    try:
        # Check file size
        max_size_bytes = max_size_mb * 1024 * 1024
        if file.size and file.size > max_size_bytes:
            raise HTTPException(
                status_code=400, 
                detail=f"File too large. Max size: {max_size_mb}MB"
            )
        
        # Check file type
        allowed_types = ["image/jpeg", "image/png", "image/gif", "application/pdf"]
        if file.content_type not in allowed_types:
            raise HTTPException(
                status_code=400,
                detail=f"File type not allowed. Allowed: {allowed_types}"
            )
        
        # Check filename
        if not file.filename or "." not in file.filename:
            raise HTTPException(status_code=400, detail="Invalid filename")
        
        file_path = UPLOAD_DIR / file.filename
        
        # Save file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        return {
            "filename": file.filename,
            "size": file.size,
            "content_type": file.content_type,
            "saved_path": str(file_path),
            "validation": "passed"
        }
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Upload failed: {str(e)}")

# Download uploaded file
@app.get("/download/{filename}")
async def download_file(filename: str):
    """
    Download an uploaded file.
    
    Args:
        filename: Name of the file to download
        
    Returns:
        FileResponse: The file
    """
    file_path = UPLOAD_DIR / filename
    
    if not file_path.exists():
        raise HTTPException(status_code=404, detail="File not found")
    
    return FileResponse(
        path=file_path,
        filename=filename,
        media_type="application/octet-stream"
    )

# List uploaded files
@app.get("/files/")
async def list_files():
    """
    List all uploaded files.
    
    Returns:
        dict: List of files
    """
    try:
        files = []
        for file_path in UPLOAD_DIR.iterdir():
            if file_path.is_file() and not file_path.suffix == ".json":
                files.append({
                    "filename": file_path.name,
                    "size": file_path.stat().st_size,
                    "created": file_path.stat().st_ctime
                })
        
        return {"files": files}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to list files: {str(e)}")

# Delete uploaded file
@app.delete("/files/{filename}")
async def delete_file(filename: str):
    """
    Delete an uploaded file.
    
    Args:
        filename: Name of the file to delete
        
    Returns:
        dict: Deletion status
    """
    try:
        file_path = UPLOAD_DIR / filename
        
        if not file_path.exists():
            raise HTTPException(status_code=404, detail="File not found")
        
        file_path.unlink()
        
        # Also delete metadata if exists
        metadata_path = UPLOAD_DIR / f"{filename}.json"
        if metadata_path.exists():
            metadata_path.unlink()
        
        return {"message": f"File {filename} deleted successfully"}
    
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to delete file: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 