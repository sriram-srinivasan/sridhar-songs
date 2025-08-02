import xml.etree.ElementTree as ET
import sys
file = sys.argv[1]

# Load SVG from file or string
with open(file, "r", encoding="utf-8") as f:
    svg_data = f.read()

# Register namespaces (adjust these if needed)
namespaces = {
    'svg': 'http://www.w3.org/2000/svg',
    'xl': 'http://www.w3.org/1999/xlink'
}

# Parse the SVG
root = ET.fromstring(svg_data)

# Find all <a> elements
for a in root.findall('.//svg:a', namespaces):
    href = a.attrib.get('{http://www.w3.org/1999/xlink}href')

    # Find first <tspan> under <text>
    first_tspan = a.find('.//svg:tspan', namespaces)
    title = first_tspan.text.strip() if first_tspan is not None else None

    if href and title:
        print(f"{href} {title}")
