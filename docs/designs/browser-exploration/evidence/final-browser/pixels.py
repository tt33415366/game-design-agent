from pathlib import Path
import json

from PIL import Image

out = {}
for path in Path('/tmp/valley-final-v2').glob('*.png'):
    image = Image.open(path).convert('RGB')
    colors = image.getcolors(maxcolors=image.width * image.height)
    out[path.name] = {
        'size': image.size,
        'unique_colors': len(colors) if colors else 'over-limit',
        'non_background_pixels': sum(count for count, color in colors if color != (127, 187, 91)) if colors else 'not-counted',
    }
Path('/tmp/valley-final-v2/pixels.json').write_text(json.dumps(out, indent=2))
print(json.dumps(out, indent=2))
