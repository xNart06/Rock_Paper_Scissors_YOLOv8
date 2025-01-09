# Rock, Paper, Scissors & YOLOv8 Training

Welcome to this repository! This project combines two interesting implementations that demonstrate the power of YOLOv8 and object detection:

1. **Rock, Paper, Scissors Video Test**:
   - Detects and classifies hand gestures (rock, paper, scissors) in video streams.
2. **YOLOv8 Training**:
   - A detailed tutorial on how to train the YOLOv8 object detection model on a custom dataset.

---

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Features](#features)
- [Requirements](#requirements)
- [Usage](#usage)
  - [Rock, Paper, Scissors Video Test](#rock-paper-scissors-video-test)
  - [YOLOv8 Training](#yolov8-training)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

### Rock, Paper, Scissors Video Test
This project demonstrates how to use YOLOv8 for a fun application: classifying hand gestures (`rock`, `paper`, `scissors`) in real-time video streams. The notebook is lightweight and perfect for beginners looking to get started with video-based object detection.

### YOLOv8 Training
Learn how to train the powerful YOLOv8 object detection model on your own custom dataset. This tutorial covers:
- Setting up YOLOv8
- Preparing and augmenting a dataset
- Training and validating a model
- Running inferences on test data

Whether you're new to object detection or looking to fine-tune a model for specific tasks, this notebook has you covered.

---

## Project Structure

```plaintext
.
├── Rock_paper_scissors_videoTest.ipynb   # Notebook for video-based RPS detection
├── Yolo_v8_train.ipynb                   # Notebook for YOLOv8 training on custom datasets
├── README.md                             # Project documentation
├── requirements.txt                      # Python dependencies
└── data/                                 # Placeholder for datasets
```

---

## Features

- **Rock, Paper, Scissors Video Test**:
  - Classifies hand gestures in video streams.
  - Uses YOLOv8 for detection and classification.
  - Simple and intuitive workflow.

- **YOLOv8 Training**:
  - Supports custom datasets.
  - Step-by-step tutorial.
  - Detailed performance evaluation.
  - GPU acceleration for faster training.

---

## Requirements

Ensure you have the following installed:

- Python 3.8+
- Jupyter Notebook or Google Colab
- Required libraries (see `requirements.txt`):
  - `ultralytics`
  - `opencv-python`
  - `numpy`
  - `matplotlib`

---


## Usage

### Rock, Paper, Scissors Video Test

1. Open `Rock_paper_scissors_videoTest.ipynb` in Jupyter Notebook or Colab.
2. Follow the steps to load a video and classify gestures.
3. Modify the input video path in the notebook to test with your own videos.

### YOLOv8 Training

1. Open `Yolo_v8_train.ipynb` in Jupyter Notebook or Colab.
2. Follow the outlined steps to:
   - Install YOLOv8
   - Load your custom dataset
   - Train and validate your model
3. Adjust hyperparameters as needed for better results.

---

## Results

- **Rock, Paper, Scissors Video Test**:
  - Outputs processed video frames with classified gestures.
  - Example result:
    ![Example Output](path/to/example_output_rps.png)

- **YOLOv8 Training**:
  - Model performance metrics (e.g., mAP, precision, recall).
  - Sample inference results:
    ![Inference Example](path/to/inference_example.png)

---

## Contributing

Contributions are welcome! If you find a bug or have an idea for improvement, feel free to open an issue or submit a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
