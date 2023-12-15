import bibtexparser


def remove_fields(entry, fields_to_remove=['abstract', 'file', 'url', 'urldate']):
    """
    Removes unwanted fields form a bibtex file.

    Parameters
    ----------
    entry : bibtexparser
        Entry of the bibtex file.
    fields_to_remove : List of strings
        List of fields to remove from the bibtex entry.
    """
    for field in fields_to_remove:
        if field in entry:
            entry.pop(field)


def replace_infinity_symbol(entry):
    """
    Replaces infinity symbols by latex representation.

    Parameters
    ----------
    entry : bibtexparser
        Entry of the bibtex file.
    """
    infinity_symbol = '∞'
    if 'title' in entry:
        entry['title'] = entry['title'].replace(
            infinity_symbol, '$\\infinity$')


def replace_doi_underscore(entry):
    """
    Replaces underscores in the DOI field by latex compatible underscores.

    Parameters
    ----------
    entry : bibtexparser
        Entry of the bibtex file.
    """
    if 'doi' in entry:
        entry['doi'] = entry['doi'].replace('_', '\\_')


def process_bib_file(input_path, output_path):
    """
    Processing function. Reads the bibtex file from input path, performes processing
    on all entries and writes bibtex file to output path.

    Parameters
    ----------
    input_path : string
        Input path of the unprocessed bibtex file.
    output_path : string
        Output path of the processed bibtex file.
    """
    with open(input_path, 'r', encoding='utf-8') as bib_file:
        bib_database = bibtexparser.load(bib_file)

    for entry in bib_database.entries:
        remove_fields(entry)
        replace_infinity_symbol(entry)
        replace_doi_underscore(entry)

    with open(output_path, 'w', encoding='utf-8') as output_file:
        bibtexparser.dump(bib_database, output_file)


if __name__ == "__main__":
    input_bib_file = "bibliography.bib"  # Path to your input .bib file
    output_bib_file = "bibliography.bib"  # Path to the output .bib file

    process_bib_file(input_bib_file, output_bib_file)
    print("Abstracts, files, infinity symbols, and underscores replaced.")
