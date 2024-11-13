from PIL import Image, ImageEnhance
import os

# Define the image filename (must be in the same folder as this script)
filename = 'aymansadik.jpg'  # Replace this with your image's filename

# Open the image
img = Image.open(filename)

# Apply sharpness enhancement
sharpness_enhancer = ImageEnhance.Sharpness(img)
img_sharp = sharpness_enhancer.enhance(2.0)  # Adjust sharpness level as desired

# Apply saturation (color) enhancement
color_enhancer = ImageEnhance.Color(img_sharp)
img_enhanced = color_enhancer.enhance(1.5)  # Adjust saturation level as desired

# Save the edited image
clean_name = os.path.splitext(filename)[0]
img_enhanced.save(f"{clean_name}_enhanced.jpg")
