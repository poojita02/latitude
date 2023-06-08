import csv
import json
import os
from faker import Faker


def generate_fixed_width_file(spec_file, output_file):
    # Load the spec file to retrieve parameters


    with open(spec_file, 'r') as f:
        spec = json.load(f)

    column_names = spec['ColumnNames']
    offsets = spec['Offsets']
    fixed_width_encoding = spec['FixedWidthEncoding']
    include_header = spec['IncludeHeader']

    fake = Faker()

    data_rows = []
    # Sample data preparation using faker as per the offset (length of the column)
    for _ in range(10):
        row = [fake.word()[:int(offset)] for offset in offsets]
        data_rows.append(row)
    # Creating the fixed width file with the header and the sample data
    with open(output_file, 'w', encoding=fixed_width_encoding) as f:
        if include_header:
            header = ''.join(f'{column:<{int(offset)}}' for column, offset in zip(column_names, offsets))
            f.write(header + '\n')
        for row in data_rows:
            formatted_row = ''.join(f'{value:<{int(offset)}}' for value, offset in zip(row, offsets))
            f.write(formatted_row + '\n')




def generate_csv_from_fixed_width(fixed_width_file, csv_file, spec_file):
    # Load the spec file to retrieve parameters
    with open(spec_file, 'r') as f:
        spec = json.load(f)

    column_names = spec['ColumnNames']
    offsets = [int(offset) for offset in spec['Offsets']]  # Convert offsets to integers
    fixed_width_encoding = spec['FixedWidthEncoding']
    include_header = spec['IncludeHeader']
    delimited_encoding = spec['DelimitedEncoding']

    data_rows = []
    # Parsing the Fixed width file in each line as per the column length (offsets)
    with open(fixed_width_file, 'r', encoding=fixed_width_encoding) as f:
        if include_header:
            next(f)  # Skip the header line
        for line in f:
            rev_offsets = [offsets[i] if i == 0 else sum(offsets[:i + 1]) for i in range(len(offsets))]
            row = [line[start:end + 1].strip() for start, end in
                   zip([0 if i == 0 else rev_offsets[i - 1] for i in range(len(rev_offsets))],
                       [rev_offsets[i] - 1 for i in range(len(rev_offsets))])]
            data_rows.append(row)
    # Load the parsed data into a csv delimited file
    with open(csv_file, 'w', newline='', encoding=delimited_encoding) as f:
        writer = csv.writer(f)
        if include_header:
            writer.writerow(column_names)
        writer.writerows(data_rows)




if __name__ == '__main__':
    # Load the parameter file to retrieve file paths and configurations
    script_dir = os.path.dirname(os.path.abspath(__file__))
    param_file_path = os.path.join(script_dir, 'latitude_param.json')

    with open(param_file_path, 'r') as param_file:
        parameters = json.load(param_file)

    parent_dir = os.path.join(script_dir, '..')
    fixed_width_file = os.path.join(parent_dir, 'data', parameters['FixedWidthFile'])
    csv_file = os.path.join(parent_dir, 'data', parameters['CSVFile'])
    spec_file = os.path.join(script_dir, parameters['SpecFile'])
    # spec_file = parameters['SpecFile']

    generate_fixed_width_file(spec_file, fixed_width_file)
    generate_csv_from_fixed_width(fixed_width_file, csv_file, spec_file)
