import cv2
import numpy as np
import matplotlib.pyplot as plt

def stereo_rectify(image_left, image_right, camera_matrix, dist_coeffs, R, T):
    """ Perform stereo rectification for perfectly parallel cameras """

    # Load images
    imgL = cv2.imread(image_left)
    imgR = cv2.imread(image_right)

    # Convert to grayscale
    grayL = cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)
    grayR = cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)

    # **Fix Translation Vector (Only X-Shift)**
    T_fixed = np.array([[0.06], [0.0], [0.0]])  # Assume 6 cm baseline

    # **Stereo Rectification**
    R1, R2, P1, P2, Q, _, _ = cv2.stereoRectify(
        camera_matrix, dist_coeffs,  # Left Camera
        camera_matrix, dist_coeffs,  # Right Camera
        grayL.shape[::-1], R, T_fixed, alpha=1
    )

    # **Generate Remapping Matrices**
    mapL1, mapL2 = cv2.initUndistortRectifyMap(camera_matrix, dist_coeffs, R1, P1, grayL.shape[::-1], cv2.CV_16SC2)
    mapR1, mapR2 = cv2.initUndistortRectifyMap(camera_matrix, dist_coeffs, R2, P2, grayR.shape[::-1], cv2.CV_16SC2)

    # **Apply Remapping**
    rectifiedL = cv2.remap(imgL, mapL1, mapL2, cv2.INTER_LINEAR)
    rectifiedR = cv2.remap(imgR, mapR1, mapR2, cv2.INTER_LINEAR)

    # **Draw Epipolar Lines**
    def draw_epipolar_lines(img):
        h, w = img.shape[:2]
        for i in range(20, h, 40):  # 20px spacing
            cv2.line(img, (0, i), (w, i), (0, 255, 0), 1)

    draw_epipolar_lines(rectifiedL)
    draw_epipolar_lines(rectifiedR)

    # **Show Rectified Images**
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    axes[0].imshow(cv2.cvtColor(rectifiedL, cv2.COLOR_BGR2RGB))
    axes[0].set_title("Rectified Left Image")
    axes[0].axis("off")

    axes[1].imshow(cv2.cvtColor(rectifiedR, cv2.COLOR_BGR2RGB))
    axes[1].set_title("Rectified Right Image")
    axes[1].axis("off")

    plt.show()

    return rectifiedL, rectifiedR