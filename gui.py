from keras.models import load_model
from tkinter import *
import tkinter as tk
from PIL import Image, ImageDraw, ImageOps
import numpy as np

# Load the model
model = load_model('mnist.keras')

def predict_digit(img):
    # Resize image to 28x28 pixels
    img = img.resize((28,28))
    # Convert RGB to grayscale
    img = img.convert('L')
    # Invert image to have a white background and black digits, like MNIST
    img = ImageOps.invert(img)
    img = np.array(img)
    # Reshaping to support our model input and normalizing
    img = img.reshape(1, 28, 28, 1)
    img = img.astype('float32') / 255.0
    # Predicting the class
    res = model.predict([img])[0]
    return np.argmax(res), max(res)

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.x = self.y = 0
        self.image = Image.new("RGB", (1000, 1000), "black")
        self.draw = ImageDraw.Draw(self.image)

        # Creating elements
        self.canvas = tk.Canvas(self, width=300, height=300, bg="black", cursor="cross")
        self.label = tk.Label(self, text="Thinking..", font=("Helvetica", 48))
        self.classify_btn = tk.Button(self, text="Recognise", command=self.classify_handwriting)
        self.button_clear = tk.Button(self, text="Clear", command=self.clear_all)

        # Grid structure
        self.canvas.grid(row=0, column=0, pady=2, sticky=W)
        self.label.grid(row=0, column=1, pady=2, padx=2)
        self.classify_btn.grid(row=1, column=1, pady=2, padx=2)
        self.button_clear.grid(row=1, column=0, pady=2)

        self.canvas.bind("<B1-Motion>", self.draw_lines)

    def clear_all(self):
        self.canvas.delete("all")
        self.image = Image.new("RGB", (300, 300), "black")
        self.draw = ImageDraw.Draw(self.image)

    def classify_handwriting(self):
        # Convert the PIL image to grayscale for digit prediction
        img_gray = self.image.convert('L')
        digit, acc = predict_digit(img_gray)
        self.label.configure(text=str(digit) + ', ' + str(int(acc * 100)) + '%')

    def draw_lines(self, event):
        self.x = event.x
        self.y = event.y
        r = 8
        self.canvas.create_oval(self.x - r, self.y - r, self.x + r, self.y + r, fill='white')
        # Draw on the PIL image as well
        self.draw.ellipse([self.x - r, self.y - r, self.x + r, self.y + r], fill='white')

if __name__ == '__main__':
    app = App()
    mainloop()
