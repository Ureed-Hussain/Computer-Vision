# 🧱 3D Reconstruction using Sparse and Dense Methods

This project implements 3D reconstruction from images using both **sparse** and **dense** reconstruction techniques. It supports **single-camera** and **multi-camera** (stereo) setups for generating 3D point clouds from 2D images.

---

## 📦 Features

- 📸 Supports both monocular and stereo camera setups
- 🧠 Sparse and dense 3D reconstruction
- 🔍 Keypoint detection and feature matching
- 🌄 Disparity and depth map computation
- ☁️ 3D point cloud generation
- 🧪 Jupyter notebooks for experimentation
- ⚙️ Configurable pipeline via code

---

## ✅ Prerequisites

Ensure the following are installed:

- Python 3.7+
- `pip` (Python package manager)
- (Optional) CUDA-enabled GPU for faster computation

---

## 🛠 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/hassaanahmed04/Computer-Vision.git
   cd 3d-reconstruction
   ```

2. **Create and activate a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install required packages**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Running the Project

### Option 1: Jupyter Notebooks

- **Single camera reconstruction**:
  ```bash
  jupyter notebook "Single camera.ipynb"
  ```

- **Stereo camera reconstruction**:
  ```bash
  jupyter notebook "Two Cameras.ipynb"
  ```

### Option 2: Python Application

- Run the main application:
  ```bash
  python main.py
  ```
  > **Note**: If `main.py` requires command-line arguments, refer to the script or documentation for usage.

---

## 🧭 Usage Instructions

### 🔹 Single Camera Workflow

1. Place input images in the `data/` directory.
2. The system will:
   - Detect keypoints and extract features
   - Match features across images
   - Estimate camera poses
   - Perform sparse reconstruction
   - Optionally perform dense reconstruction

### 🔸 Stereo Camera Workflow

1. Place left-right image pairs in the `data/` directory.
2. The system will:
   - Perform stereo calibration (if required)
   - Generate disparity maps
   - Convert disparity to depth
   - Construct 3D point clouds

---

## ⚙️ Configuration

You may need to modify parameters or paths:

- `core/*` — algorithm parameters
- `main.py` — modify paths to image files, settings, etc.

---

## 🗂 Sample Data

Example files included in the repository:

- `1.jpg`, `2.jpg` — for single-camera pipeline
- `ll12.png`, `rr12.png` — stereo image pairs

---

## 🧩 Troubleshooting

### 📦 Installation Issues

- Upgrade pip:
  ```bash
  pip install --upgrade pip
  ```
- Install OpenCV manually (if needed):
  ```bash
  pip install opencv-contrib-python
  ```

### ⚠️ CUDA Errors

Run with CPU-only:
```python
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
```

### 🧠 Memory Issues

- Resize large images before processing to avoid OOM (Out Of Memory) errors

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch
3. Submit a pull request with a clear description


---

## 📬 Contact

**Author**: Hassaan Ahmed  
GitHub: [@hassaanahmed04](https://github.com/hassaanahmed04)

---
## ✅ Example Output

*Coming soon:* Sample screenshots of point clouds or depth maps can enhance this documentation.

