import unittest
import os
import sys

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

from src.latitude_code_challenge import generate_fixed_width_file, generate_csv_from_fixed_width

# Add parent directory to Python module search path

class TestLatitudeCodeChallenge(unittest.TestCase):
    def setUp(self):
        # Set up test file paths
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.test_data_dir = os.path.abspath(os.path.join(self.script_dir, '..', 'data'))
        self.src_dir = os.path.abspath(os.path.join(self.script_dir, '..', 'src'))

        self.spec_file = os.path.join(self.src_dir, 'spec.json')
        self.fixed_width_file = os.path.join(self.test_data_dir, 'fixed_width_file.txt')
        self.csv_file = os.path.join(self.test_data_dir, 'csv_file.csv')

        print(self.script_dir)
        print(self.test_data_dir)
        print(self.src_dir)
        print(self.spec_file)
        print(self.fixed_width_file)
        print(self.csv_file)

    def tearDown(self):
        pass
        # Clean up generated test files
        # os.remove(self.fixed_width_file)
        # os.remove(self.csv_file)

    def test_generate_fixed_width_file(self):
        # Generate fixed width file
        generate_fixed_width_file(self.spec_file, self.fixed_width_file)

        # Check if the file is created
        self.assertTrue(os.path.exists(self.fixed_width_file))

        # Read the actual content from the file
        with open(self.fixed_width_file, 'r') as file:
            actual_content = file.readlines()

        # Remove newlines and delimiters between columns
        fw_content = [line.replace(' ', '').strip() for line in actual_content]

        return fw_content

    def test_generate_csv_from_fixed_width(self):


        # Generate CSV from fixed width file
        generate_csv_from_fixed_width(self.fixed_width_file, self.csv_file, self.spec_file)

        # Check if the file is created
        self.assertTrue(os.path.exists(self.csv_file))

        # Read the actual content from the file
        with open(self.csv_file, 'r') as file:
            actual_content = file.readlines()

        # Remove newlines and delimiters between columns
        csv_actual_content = [line.replace(',', '').strip() for line in actual_content]

        return csv_actual_content

    def test_compare_fixed_width_and_csv(self):
        fw_content = self.test_generate_fixed_width_file()
        csv_content = self.test_generate_csv_from_fixed_width()

        # Print the content of the files for debugging
        print("Fixed Width File Content:")
        print(fw_content)
        print("CSV File Content:")
        print(csv_content)

        # Compare line by line
        self.assertListEqual(fw_content, csv_content)

if __name__ == '__main__':
    unittest.main()
