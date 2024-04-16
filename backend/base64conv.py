from PIL import Image
import base64
import io
import binascii

# Open an image file
with Image.open('D:\dongzijing\桌面\谷物_麦片.png') as img:
    # Convert image to bytes
    byte_arr = io.BytesIO()
    image_format = img.format
    img.save(byte_arr, format=image_format)
    img_binary = byte_arr.getvalue()

hex_data = binascii.hexlify(img_binary)
print(hex_data)

# Print the image binary to txt file
with open('image_binary.txt', 'wb') as f:
    f.write(hex_data)

# # Convert bytes to base64
img_base64 = base64.b64encode(img_binary)

# # Decode to ASCII string
img_base64_string = img_base64.decode('utf-8')

with open('img_base64_string.txt', 'wb') as f:
    f.write(img_binary)

# Assuming img_binary is your binary image data
# Convert bytes to image
image = Image.open(io.BytesIO(img_binary))

# image_binary.txt stores the hex of a image, read and render it
# Read the hexadecimal data from the file
with open('image_binary.txt', 'r') as f:
    hex_data = f.read()

# Convert the hexadecimal data back to binary
binary_data = binascii.unhexlify(hex_data)

# Convert the binary data to a BytesIO object
image_data = io.BytesIO(binary_data)

# Open the image data with PIL
image = Image.open(image_data)

# Display the image
image.show()