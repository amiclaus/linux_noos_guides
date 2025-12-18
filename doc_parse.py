#!/usr/bin/env python3
"""
Script to extract base64 inlined images from PDF or markdown files and replace them with file references.

The script:
1. For PDF files: Converts to markdown using docling CLI tool
2. Finds all base64 inlined images in the markdown file
3. Creates a subfolder named <documentName>_images
4. Saves images with increasing number names (1.png, 2.jpg, etc.)
5. Updates the markdown to reference these image files instead of base64 data

Requirements:
- docling must be installed for PDF conversion (pip install docling)
"""

import re
import base64
import os
import sys
import subprocess
from pathlib import Path
from typing import List, Tuple


def detect_image_format(base64_data: str) -> str:
    """
    Detect image format from base64 data by checking the header.

    Args:
        base64_data: Base64 encoded image data

    Returns:
        File extension (png, jpg, gif, etc.)
    """
    try:
        # Decode just the first few bytes to check the signature
        decoded_header = base64.b64decode(base64_data[:50])

        # Check common image signatures
        if decoded_header.startswith(b'\x89PNG\r\n\x1a\n'):
            return 'png'
        elif decoded_header.startswith(b'\xff\xd8\xff'):
            return 'jpg'
        elif decoded_header.startswith(b'GIF8'):
            return 'gif'
        elif decoded_header.startswith(b'RIFF') and b'WEBP' in decoded_header[:20]:
            return 'webp'
        elif decoded_header.startswith(b'BM'):
            return 'bmp'
        else:
            # Default to png if we can't determine
            return 'png'
    except Exception:
        # If we can't decode or detect, default to png
        return 'png'


def convert_pdf_to_markdown(pdf_path: str) -> str:
    """
    Convert a PDF file to markdown using the docling CLI tool.

    Args:
        pdf_path: Path to the PDF file

    Returns:
        Path to the generated markdown file

    Raises:
        RuntimeError: If docling is not installed or conversion fails
    """
    # Check if docling is available
    try:
        subprocess.run(['docling', '--version'],
                      capture_output=True,
                      check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        raise RuntimeError(
            "docling is not installed or not in PATH. "
            "Please install it first: pip install docling"
        )

    # Derive expected markdown filename
    # Docling creates the .md file in the current working directory, not the PDF's directory
    pdf_path_obj = Path(pdf_path)
    pdf_basename = pdf_path_obj.stem  # Get filename without extension
    expected_md_path = Path.cwd() / f"{pdf_basename}.md"

    print(f"Converting PDF to markdown using docling: {pdf_path}")

    # Execute docling conversion
    try:
        result = subprocess.run(
            ['docling', pdf_path],
            capture_output=True,
            text=True,
            check=True
        )
        print(f"Docling output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(
            f"Docling conversion failed with error:\n{e.stderr}"
        )

    # Verify the markdown file was created
    if not expected_md_path.exists():
        raise RuntimeError(
            f"Expected markdown file not found: {expected_md_path}\n"
            f"Docling may have failed silently or used a different output path."
        )

    print(f"Successfully converted to: {expected_md_path}")
    return str(expected_md_path)


def extract_base64_images(markdown_content: str) -> List[Tuple[str, str, str, str]]:
    """
    Extract base64 inlined images from markdown content.

    Args:
        markdown_content: The markdown file content

    Returns:
        List of tuples containing (full_match, alt_text, mime_type, base64_data)
    """
    # Pattern to match markdown images with base64 data
    # ![alt text](data:image/type;base64,data)
    pattern = r'!\[([^\]]*)\]\(data:image/([^;]+);base64,([A-Za-z0-9+/=]+)\)'

    matches = []
    for match in re.finditer(pattern, markdown_content):
        full_match = match.group(0)
        alt_text = match.group(1)
        mime_type = match.group(2)
        base64_data = match.group(3)
        matches.append((full_match, alt_text, mime_type, base64_data))

    return matches


def process_markdown_file(file_path: str) -> bool:
    """
    Process a markdown file to extract base64 images and update references.

    Args:
        file_path: Path to the markdown file

    Returns:
        True if successful, False otherwise
    """
    try:
        # Read the markdown file
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract base64 images
        base64_images = extract_base64_images(content)

        if not base64_images:
            print(f"No base64 images found in {file_path}")
            return True

        print(f"Found {len(base64_images)} base64 images in {file_path}")

        # Create images folder
        file_path_obj = Path(file_path)
        document_name = file_path_obj.stem
        images_folder = file_path_obj.parent / f"{document_name}_images"
        images_folder.mkdir(exist_ok=True)

        print(f"Created images folder: {images_folder}")

        # Process each image
        updated_content = content
        for i, (full_match, alt_text, mime_type, base64_data) in enumerate(base64_images, 1):
            try:
                # Decode base64 data
                image_data = base64.b64decode(base64_data)

                # Determine file extension
                if mime_type in ['jpeg']:
                    extension = 'jpg'
                else:
                    extension = mime_type.lower()

                # Validate extension by checking actual image format
                detected_format = detect_image_format(base64_data)
                if detected_format != extension:
                    print(f"Warning: MIME type suggests {extension} but detected {detected_format}. Using detected format.")
                    extension = detected_format

                # Create filename
                filename = f"{i}.{extension}"
                image_path = images_folder / filename

                # Save image
                with open(image_path, 'wb') as img_file:
                    img_file.write(image_data)

                print(f"Saved image {i}: {filename} ({len(image_data)} bytes)")

                # Create new markdown reference
                relative_path = f"{document_name}_images/{filename}"
                new_reference = f"![{alt_text}]({relative_path})"

                # Replace in content
                updated_content = updated_content.replace(full_match, new_reference, 1)

            except Exception as e:
                print(f"Error processing image {i}: {e}")
                continue

        # Write updated markdown file
        backup_path = f"{file_path}.backup"
        os.rename(file_path, backup_path)

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)

        print(f"Updated markdown file saved. Original backed up as: {backup_path}")
        return True

    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
        return False


def main():
    """Main function to handle command line arguments and process files."""
    if len(sys.argv) != 2:
        print("Usage: python extract_images.py <file_path>")
        print("Supported formats: PDF (.pdf) or Markdown (.md)")
        print("Examples:")
        print("  python extract_images.py document.pdf")
        print("  python extract_images.py document.md")
        sys.exit(1)

    file_path = sys.argv[1]

    if not os.path.exists(file_path):
        print(f"Error: File {file_path} does not exist.")
        sys.exit(1)

    file_path_lower = file_path.lower()

    # Handle PDF files - convert to markdown first
    if file_path_lower.endswith('.pdf'):
        print(f"Processing PDF file: {file_path}")
        try:
            md_file_path = convert_pdf_to_markdown(file_path)
            print(f"Processing generated markdown file: {md_file_path}")
            success = process_markdown_file(md_file_path)
        except RuntimeError as e:
            print(f"Error: {e}")
            sys.exit(1)

    # Handle markdown files directly
    elif file_path_lower.endswith('.md'):
        print(f"Processing markdown file: {file_path}")
        success = process_markdown_file(file_path)

    # Unsupported file type
    else:
        print(f"Error: Unsupported file type: {file_path}")
        print("Please provide a PDF (.pdf) or Markdown (.md) file.")
        sys.exit(1)

    if success:
        print("Processing completed successfully!")
    else:
        print("Processing failed!")
        sys.exit(1)


if __name__ == "__main__":
    main()
