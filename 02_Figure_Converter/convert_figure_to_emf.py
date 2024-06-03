import os
import subprocess
import time
import argparse
from typing import List

def convert_svg_to_emf(svg_file: str, emf_file: str) -> None:
    """Converts a single SVG file to EMF using Inkscape."""
    command = f'inkscape "{svg_file}" --export-filename="{emf_file}"'
    try:
        process = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Conversion successful: {svg_file} to {emf_file}")
        print(process.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Conversion unsuccessful: {svg_file} to {emf_file} with error: {e}")
        print(e.stderr.decode())

def convert_pdf_to_emf(pdf_file: str, emf_file: str) -> None:
    """Convert a single PDF file to EMF using Inkscape."""
    command = f'inkscape "{pdf_file}" --export-filename="{emf_file}"'
    try:
        process = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"Conversion successful: {pdf_file} to {emf_file}")
        print(process.stdout.decode())
    except subprocess.CalledProcessError as e:
        print(f"Conversion unsuccessful: {pdf_file} to {emf_file} with error: {e}")
        print(e.stderr.decode())
        
def convert_figures(filetypes: List[str]=["svg", "pdf"]) -> None:
    # Directory definition
    base_dir = "Plots"
    emf_dir = "Plots_emf"

    # Check for emf_dir directory and create if not present
    if not os.path.exists(emf_dir):
        os.makedirs(emf_dir)

    if "svg" in filetypes:
        print("Starting with SVG files\n")
    
        # Lists all .svg files in base_dir
        svg_files = [f for f in os.listdir(base_dir) if f.endswith('.svg')]

        # Converts all SVG-files into EMF-files
        for svg_file in svg_files:
            svg_path = os.path.join(base_dir, svg_file)
            emf_file = os.path.splitext(svg_file)[0] + '.emf'
            emf_path = os.path.join(emf_dir, emf_file)
            convert_svg_to_emf(svg_path, emf_path)

    if "pdf" in filetypes:
        print("Starting with PDF files\n")
    
        # Lists all .pdf files in base_dir
        pdf_files = [f for f in os.listdir(base_dir) if f.endswith('.pdf')]

        # Converts all PDF-files into EMF-files
        for pdf_file in pdf_files:
            pdf_path = os.path.join(base_dir, pdf_file)
            emf_file = os.path.splitext(pdf_file)[0] + '.emf'
            emf_path = os.path.join(emf_dir, emf_file)
            convert_pdf_to_emf(pdf_path, emf_path)
    if all(ext not in filetypes for ext in ["svg", "pdf"]):
        print(f"No files converted. Expected [\"svg\"], [\"pdf\"] or [\"svg\", \"pdf\"] but got {filetypes}.")
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert figure files to EMF format.')
    parser.add_argument('filetypes', nargs='*', default=["svg", "pdf"], help='List of file types to convert (e.g., ["svg"], ["pdf"], or ["svg", "pdf"]).')

    args = parser.parse_args()
    start = time.time()
    convert_figures(args.filetypes)
    print(f"Conversion took {time.time()-start} seconds.")
