import os
import io
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
headers = {"Authorization": "Bearer testtoken"}

def test_successful_upload(tmp_path):
    data = {
        "username": "testuser",
        "bio": "testing upload"
    }
    image_content = b"\x89PNG\r\n\x1a\n" + b"\x00"*1024
    files = {"avatar": ("test.png", io.BytesIO(image_content), "image/png")}
    response = client.post("/users/me/profile", headers=headers, data=data, files=files)
    assert response.status_code == 200
    body = response.json()
    assert body["avatar_url"].endswith("test.png")
    assert body["username"] == "testuser"

def test_invalid_file_type():
    data = {"username": "testuser"}
    files = {"avatar": ("bad.gif", io.BytesIO(b"GIF89a"), "image/gif")}
    response = client.post("/users/me/profile", headers=headers, data=data, files=files)
    assert response.status_code == 400
    body = response.json()
    assert "PNG and JPEG" in body["detail"].capitalize() or body["error"].capitalize()

def test_invalid_file_size():
    data = {"username": "testuser"}
    big_content = b"\x89PNG" + b"0"*(2*1024*1024 + 1)
    files = {"avatar": ("big.png", io.BytesIO(big_content), "image/png")}
    response = client.post("/users/me/profile", headers=headers, data=data, files=files)
    assert response.status_code == 400
    body = response.json()
    assert "exceeds maximum" in (body.get("detail") or body.get("error")).lower()
