from manifesto.mnfs_parser import *
import argparse
import csv
import os

# Header you want to write to the file if it doesn't exist
header = ["Click board", "Manufacture", "Status", "Linux Driver", "Protocol", "URL"]
csv_rows = list()
    
def open_output_file(file_name, delimiter=','):
    if os.path.isfile(file_name):
        # The file already exists, open it in append mode
        try:
            file = open(file_name, mode='r+', newline='')
            return file
        except Exception as e:
            print(f"Error opening the file: {e}")
            return None
    else:
        # The file does not exist, create it and write the header
        try:
            file = open(file_name, mode='w+', newline='')
            writer = csv.writer(file, delimiter=delimiter)
            writer.writerow(header)
            return file
        except Exception as e:
            print(f"Error creating the file: {e}")
            return None

def load_csv(file):
    file.seek(0)
    reader = csv.reader(file)
    csv_rows = list(reader)
    return csv_rows

def update_csv(file, data):
    writer = csv.writer(file)
    file.seek(0)
    writer.writerows(data)
    file.truncate()

def generate_output_data(manifest):
    output = []

    product = manifest.string_descs[manifest.interface_desc.psid].string
    output.append(product)
    vendor = manifest.string_descs[manifest.interface_desc.vsid].string
    output.append(vendor)
    output.append("TESTED")
    if manifest.device_descs is not None:
        device_desc = next(iter(manifest.device_descs.items()))
        output.append(manifest.string_descs[device_desc[1].driver_string_id].string)
        output.append(CPortDescriptor.cport_protocol[device_desc[1].protocol][0])
    else :
        output.append('')
        output.append('')
    url = "https://www.mikroe.com/" + str(product).replace(' ', '-') + "-click"
    url = url.lower()
    output.append(url)

    return output

def update_row_in_csv(csv_rows, data):
    
    new_click = True

    for row in csv_rows:
        if data[header.index("Click board")] in row:
            status_idx = header.index("Status")
            data[status_idx] = row[status_idx]
            new_click = False
            break
    
    if new_click:
        csv_rows.append(data)


def anylyze_mnfs(file):
    parser = MnfsParser()
    manifest = parser.parse_file(file)
    output = generate_output_data(manifest)
    
    return output

def update_click(path, csv_rows):
    #
    if os.path.isdir(path):
        for cur_dir, sub_dir, files in os.walk(path):
            for file in files:
                if file.endswith('.mnfs'):
                    full_path = os.path.join(cur_dir, file)
                    update_row_in_csv(csv_rows, anylyze_mnfs(full_path))
    else:
        if path.endswith('mnfs') and os.path.isfile(path) :
            update_row_in_csv(csv_rows, anylyze_mnfs(path))

### Command line arguments
def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--infile',
            help='specify an input manifest file or directory')

    parser.add_argument('-o', '--out', default='clicks_status.csv',
            help='output file (default is clicks_status.csv)')

    parser.add_argument('-s', '--silent', action='store_true',
            help='silence the (potentially relevant) warnings')

    return parser.parse_args()

### Main
def main():
    # parse command line arguments
    args = get_args()
    # warnings.silent = args.silent

    output = open_output_file(args.out)
    if (output is not None):
        try:
            rows = load_csv(output)
            # get a manifest from the file
            update_click(args.infile, rows)
            update_csv(output, rows)
        except Exception as e:
            print(f"Error: {e}")
        finally:
            output.close()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("Error:", e)
        sys.exit(1)