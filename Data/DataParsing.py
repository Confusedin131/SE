import sys
import csv
import json
import xml.etree.ElementTree as ET

def read_tab_delimited_file(filename):
    data = []
    with open(filename, 'r', newline='') as file:
        for line in file:
            row = line.strip().split('\t')
            data.append(row)
    return data

def save_csv(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def save_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def save_xml(data, filename):
    root = ET.Element("root")
    for row in data:
        item = ET.SubElement(root, "row")
        for i, value in enumerate(row):
            ET.SubElement(item, f"col{i}").text = value

    tree = ET.ElementTree(root)
    tree.write(filename)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python convert.py <filename> <-c|-j|-x>")
        sys.exit(1)

    filename = sys.argv[1]
    output_format = sys.argv[2]

    data = read_tab_delimited_file(filename)

    if output_format == '-c':
        output_filename = filename.replace('.txt', '.csv')
        save_csv(data, output_filename)
    elif output_format == '-j':
        output_filename = filename.replace('.txt', '.json')
        save_json(data, output_filename)
    elif output_format == '-x':
        output_filename = filename.replace('.txt', '.xml')
        save_xml(data, output_filename)
    else:
        print("Invalid output format. Use -c for CSV, -j for JSON, or -x for XML.")
        sys.exit(1)

    print(f"File converted and saved as {output_filename}")
