import os
from svgutils.transform import fromfile, SVGFigure
import xml.etree.ElementTree as ET

def resize_svg(input_path, output_path, target_width=120, target_height=120):
    # Load the SVG file
    fig = fromfile(input_path)
    
    # Get original dimensions
    orig_width = float(fig.width)
    orig_height = float(fig.height)
    
    # Calculate scale factor (use the smaller ratio to ensure fitting)
    scale_x = target_width / orig_width
    scale_y = target_height / orig_height
    scale = min(scale_x, scale_y)
    
    # Create new SVG with target dimensions
    new_svg = SVGFigure(f"{target_width}", f"{target_height}")
    
    # Get the root element and all its children
    root = fig.getroot()
    
    # Calculate centering offsets
    scaled_width = orig_width * scale
    scaled_height = orig_height * scale
    x_offset = (target_width - scaled_width) / 2
    y_offset = (target_height - scaled_height) / 2
    
    # Apply scaling and centering transformation
    root.moveto(x_offset, y_offset, scale)
    
    # Add the transformed content to the new SVG
    new_svg.append(root)
    
    # Save the result
    new_svg.save(output_path)

def process_folder(input_folder, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Process each SVG file in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.svg'):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            try:
                resize_svg(input_path, output_path)
                print(f"Successfully processed: {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {str(e)}")

# Example usage
input_folder = "/Users/oliverbarnum/Documents/git/peace-of-westphalia/art/graphicalInserts/princesMedium"
output_folder = "/Users/oliverbarnum/Documents/git/peace-of-westphalia/art/graphicalInserts/princesSmall"
process_folder(input_folder, output_folder)