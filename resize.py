import os
from PIL import Image

# -------- Settings --------
input_folder = r"D:\intern_python\assign8\ECG Images of Myocardial Infarction Patients (240x12=2880)"
output_folder = r"D:\intern_python\assign8\resized_images"
size = (300, 300)                # desired size (width, height)
output_format = "JPEG"           # format to save (JPEG, PNG, etc.)
# ---------------------------

def resize_images(input_folder, output_folder, size, output_format):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)

        try:
            with Image.open(file_path) as img:
                resized_img = img.resize(size)

                base_name, _ = os.path.splitext(filename)
                new_filename = f"{base_name}.{output_format.lower()}"
                save_path = os.path.join(output_folder, new_filename)

                resized_img.save(save_path, output_format)
                print(f"✅ Saved: {save_path}")
        except Exception as e:
            print(f"Skipped {filename}: {e}")

resize_images(input_folder, output_folder, size, output_format)
