# 3D Reconstruction using Sparse and Dense Methods

This project implements 3D reconstruction from images using both sparse and dense reconstruction techniques. It supports single-camera and multi-camera setups for generating 3D point clouds from 2D images.

## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.7 or higher
- pip (Python package manager)
- For better performance, consider using a CUDA-enabled GPU if available

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/hassaanahmed04/3d-reconstruction.git
   cd 3d-reconstruction
   ```

2. **Create a virtual environment (recommended)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Project

### Option 1: Using Jupyter Notebooks

For single camera reconstruction:
```bash
jupyter notebook "Single camera.ipynb"
```

For stereo camera reconstruction:
```bash
jupyter notebook "Two Cameras.ipynb"
```

### Option 2: Using the Main Application

Run the main application:
```bash
python main.py
```
> **Note**: If `main.py` requires command-line arguments, you may need to specify them. Check the file or documentation for details.

## Usage Instructions

### Single Camera Workflow

- Place your images in the `data/` directory
- The system will:
  - Detect keypoints and features
  - Estimate camera poses
  - Perform sparse reconstruction
  - Optionally perform dense reconstruction

### Stereo Camera Workflow

- Place your left and right image pairs in the `data/` directory
- The system will:
  - Perform stereo calibration (if needed)
  - Compute disparity maps
  - Generate depth maps
  - Create 3D point clouds

## Configuration

You may need to adjust parameters in the following files depending on your use case:

- `core/config.py` (if exists) - Contains algorithm parameters
- `main.py` - May contain paths to input images

## Sample Data

The repository includes sample images:

- `1.jpg`, `2.jpg` - For single camera reconstruction
- `ll12.png`, `rr12.png` - Stereo image pair for testing

## Troubleshooting

### Dependency installation issues:
- Ensure you have the latest pip:
  ```bash
  pip install --upgrade pip
  ```

- On some systems, you may need to install OpenCV separately:
  ```bash
  pip install opencv-contrib-python
  ```

### CUDA errors:
If you encounter CUDA-related errors, try running with CPU-only:
```python
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
```

### Memory issues:
- For large images, consider resizing them before processing

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

[Specify your license here, e.g., MIT, GPL, etc.]

## Contact

For questions or support, contact:

**Hassaan Ahmed**  
GitHub: [hassaanahmed04](https://github.com/hassaanahmed04)

---

### Additional Notes

1. You should customize the "License" section with your actual license.
2. If there are any specific command-line arguments for `main.py`, add them to the "Running the Project" section.
3. For complex projects, consider adding:
   - A "Features" section
   - A "Roadmap" section
   - More detailed troubleshooting tips
   - Citation information if this is an academic project
4. If your project includes trained models or large data files, add instructions for downloading them.
