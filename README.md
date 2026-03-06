# Image Process API


Simple REST API for uploading images and applying basic image processing operations using **OpenCV** and **Flask**.


## Features

- Upload image via multipart/form-data
- Apply image transformations:
  - Convert to **grayscale**
  - Apply **Gaussian blur**
- Returns JSON with metadata + path to processed image
- Serves processed images statically

## Tech Stack

- **Backend**: Flask
- **Image Processing**: OpenCV (cv2)
- **Database**: SQLAlchemy (currently only metadata storage)
- **File handling**: secure_filename + UUID naming

## API Endpoints

| Method | Endpoint                          | Description                              | Content-Type          |
|--------|-----------------------------------|------------------------------------------|-----------------------|
| `POST` | `/upload`                         | Upload image + choose operation          | multipart/form-data   |
| `GET`  | `/media/output/<filename>`        | Serve processed image                    | —                     |

### Upload & Process Image

**`POST /upload`**

**Form-data fields:**

| Key        | Type     | Required | Description                                      | Example value              |
|------------|----------|----------|--------------------------------------------------|----------------------------|
| `image`    | file     | Yes      | Image file (png, jpg, jpeg, gif)                 | —                          |
| `operation`| text     | Yes      | Processing type to apply                         | `grayscale`, `blur`        |

**Supported operations:**

| Value       | Description                  | Parameter (future) |
|-------------|------------------------------|--------------------|
| `grayscale` | Convert image to grayscale   | —                  |
| `blur`      | Apply Gaussian blur          | ksize=21 (default) |

