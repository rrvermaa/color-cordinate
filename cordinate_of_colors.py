from PIL import Image

def get_pixel_size(image_path, x, y):
    try:
        image = Image.open(image_path)
        pixel = image.getpixel((x, y))
        return len(pixel)
    
    except Exception as e:
        print("Error:", e)
        return None

image_path = './segmentationCLASS_PNG/1.png'
  
y_coordinate = 900  
for i in range(0,2560,100):
    pixel_size = get_pixel_size(image_path, i, y_coordinate)

    if pixel_size is not None:
        print(f"Size of pixel at ({i}, {y_coordinate}): {pixel_size}")
