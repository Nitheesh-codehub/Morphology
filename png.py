import numpy as np
from PIL import Image

# ---------------- CONFIG ----------------
HEX_FILE = "output.hex"     # input from RTL
OUT_IMG  = "f11.png"

IMG_W = 256
IMG_H = 256
TOTAL_PIXELS = IMG_W * IMG_H

# ---------------- READ HEX ----------------
with open(HEX_FILE, "r") as f:
    pixels = [int(line.strip(), 16) for line in f if line.strip()]

orig_len = len(pixels)
print("Total pixels in hex file:", orig_len)

# ---------------- FIX LENGTH ----------------
if orig_len < TOTAL_PIXELS:
    # pad with zeros (black)
    pad_count = TOTAL_PIXELS - orig_len
    print(f"Padding with {pad_count} zero pixels")
    pixels.extend([0] * pad_count)

elif orig_len > TOTAL_PIXELS:
    # crop extra pixels
    print(f"Cropping extra {orig_len - TOTAL_PIXELS} pixels")
    pixels = pixels[:TOTAL_PIXELS]

# ---------------- RESHAPE ----------------
img = np.array(pixels, dtype=np.uint8).reshape((IMG_H, IMG_W))

# ---------------- SAVE IMAGE ----------------
Image.fromarray(img, mode="L").save(OUT_IMG)

print(f"✅ PNG generated: {OUT_IMG}")
print(f"Image size: {IMG_W} x {IMG_H}")
