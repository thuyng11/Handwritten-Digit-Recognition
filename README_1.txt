
# Handwritten Digit Recognition

## Overview
This project utilizes a Convolutional Neural Network (CNN) model, built with Keras, to accurately recognize handwritten digits. It includes a Python script for model training (`digit_recognition.py`) and a graphical user interface (GUI) developed with Tkinter (`gui.py`), allowing users to draw digits and get them recognized by the model.

## Key Features
- **Digit Recognition**: Leverages the MNIST dataset to train a CNN model for recognizing handwritten digits.
- **GUI for Digit Drawing**: Provides a user-friendly interface to draw digits and see the model's predictions in real-time.
- **Model Evaluation**: Assesses the trained model's accuracy and loss on the test set.

## Installation
Ensure you have Python installed on your system, along with the necessary libraries: Keras, Tkinter, Pillow (PIL), and NumPy. Install them using pip:
```
pip install tensorflow keras numpy pillow
```

## Running the Project
1. **Training the model**: Run `digit_recognition.py` to train the model. This script will automatically save the trained model as `mnist.keras`.
   ```
   python digit_recognition.py
   ```
2. **Launching the GUI**: Execute `gui.py` to open the drawing interface. Here, you can draw digits with your mouse, and the model will predict them.
   ```
   python gui.py
   ```

## Project Structure
- `digit_recognition.py`: Trains the CNN model using the MNIST dataset and saves it.
- `gui.py`: Implements the Tkinter-based GUI for drawing digits and recognizing them using the trained model.
- `mnist.keras`: The trained model file (generated after running `digit_recognition.py`).

## Contributing
Contributions to this project are welcome. Please ensure your pull requests are well-documented.
