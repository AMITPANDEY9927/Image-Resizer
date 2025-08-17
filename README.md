# ECG Image Resizer & Converter

## 📌 Project Overview
This project is a **batch image resizer and converter tool** built using **Python** and **Pillow (PIL)**. It takes all images from a given input folder, resizes them to a fixed size, and saves them into an output folder in the chosen format. This tool is especially useful for **ECG medical image preprocessing** or preparing datasets for **machine learning and deep learning models**.

## 🛠️ Tools & Libraries
- Python 3.x
- Pillow (PIL)
- os module

## 🚀 Features
- Resizes all images in a folder to a fixed size (default: 300x300).
- Converts images to a desired format (JPEG/PNG).
- Automatically creates an output folder if it doesn’t exist.
- Skips unsupported or corrupted files gracefully.

## 📂 Project Structure
D:\intern_python\assign8\
│── ECG Images of Myocardial Infarction Patients (240x12=2880)\   # Input folder (original images)  
│── resized_images\                                              # Output folder (resized images)  
│── image_resizer.py                                             # Python script  

## ⚡ How to Run
1. Install dependencies:
   pip install pillow

2. Update the folder paths in `image_resizer.py`:
   input_folder = r"D:\intern_python\assign8\ECG Images of Myocardial Infarction Patients (240x12=2880)"  
   output_folder = r"D:\intern_python\assign8\resized_images"

3. Run the script:
   python image_resizer.py

## 🎯 Example Output
- Input: image1.png (1024x768)  
- Output: image1.jpeg (300x300)  

## 📖 Notes
- Change `size = (300, 300)` to your desired dimensions.  
- Change `output_format = "JPEG"` to `"PNG"` or others if needed.  
- This project can be extended to include **aspect ratio preservation** and **batch format conversions**.

✅ Project Complete: **ECG Image Resizer & Converter**
