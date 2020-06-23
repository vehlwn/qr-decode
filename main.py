from PIL import Image, ImageDraw
import sys
from pyzbar import pyzbar
import os

if __name__ == "__main__":
    i = 1
    for fname in sys.argv[1:]:
        image = Image.open(fname).convert("RGB")
        out_image = image.copy()
        draw = ImageDraw.Draw(out_image)
        for code in pyzbar.decode(image):
            print(f"---\n{i}-th code decoded from '{fname}':")
            print(f"   type = {code.type}")
            print(f"   data = {code.data}")
            print(f"   utf-8 = {code.data.decode('utf-8')}")
            rect = code.rect
            WIDTH = 10
            draw.rectangle(
                (
                    (rect.left, rect.top),
                    (rect.left + rect.width, rect.top + rect.height),
                ),
                outline="#ff0000",
                width=WIDTH,
            )
            points = list(code.polygon)
            points.append(points[0])
            draw.line(points, fill="#0000ff", width=WIDTH, joint="curve")
        (name, ext) = os.path.splitext(fname)
        out_image.save(os.path.join(os.path.dirname(fname), name + "-scanned" + ext,))
