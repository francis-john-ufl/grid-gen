from PIL import Image, ImageDraw

# Config
width = 801
height = 601
spacing = 50  # Distance between lines

# Create transparent image
img = Image.new("RGBA", (width, height), (0, 0, 0, 0))
draw = ImageDraw.Draw(img)

# Draw vertical lines
for x in range(0, width, spacing):
  draw.line([(x, 0), (x, height)], fill=(0, 0, 0, 255))

# Draw horizontal lines
for y in range(0, height, spacing):
  draw.line([(0, y), (width, y)], fill=(0, 0, 0, 255))

# Save image
img.save("grid.png", "PNG")
