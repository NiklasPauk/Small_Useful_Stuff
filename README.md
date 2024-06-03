# Small (Un-)useful Stuff

A compilation of potentially usefull stuff.

## 01 - Bib-Cleaner

Small utility [file](https://github.com/NiklasPauk/Small_Useful_Stuff/blob/main/01_Bibtex_Cleaner/bib_cleaner.py) to clean a bibtex file to make it compatible with latex and remove unwanted fields. Customizable to replace symbols (e.g. the infinity symbol), make underscores latex save and remove unwanted fields from the generated bibtex file (e.g. the journal abstract or file location).


## 02 - Figure-Converter (Inkscape)

Small utility [file](https://github.com/NiklasPauk/Small_Useful_Stuff/blob/main/02_Figure_Converter/convert_figure_to_emf.py) to convert figure files (".svg" or ".pdf") into ".emf". Requires the opensource software inkscape to be installed and its executable added to PATH. Place this file in a directory with a folder "Plots" that contains the figures to be converted. Run this file from the command line as one of three options
1. SVG to EMF
```sh
python convert_figure_to_emf.py svg
```
2. PDF to EMF
```sh
python convert_figure_to_emf.py pdf
```
3. SVG and PDF to EMF
```sh
python convert_figure_to_emf.py svg pdf
```
Not specifying the datatype defaults to both SVG and PDF
