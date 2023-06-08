
This repository contains a Python script that generates a fixed-width file based on the specifications provided in a JSON parameter file
and then Fixed width file is parsed and converted into a CSV file.

## Prerequisites

- Python 3.x
- Required Python libraries (specified in `requirements.txt`)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/poojita02/latitude
   ```

2. Navigate to the project directory:

   ```bash
   cd latitude
   ```

3. Install the required Python libraries using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place your input specification file (`spec.json`) in the `src` directory. In this case, I have already placed.

2. Execute the Python script:

   ```bash
   python app/src/latitude_code_challenge.py
   ```

3. The generated fixed-width file will be saved in the `data` directory with the name `fixed_width_file.txt`.

4. You can modify the input specification file (`spec.json`) to change the column names, offsets, encoding, or other parameters.

## Logging
1. The script utilizes logging to provide information about the execution process and any errors that occur. The log messages are saved in a log file named logfile.log located in the log directory.

2. To view the log file, navigate to the log directory and open logfile.log:

    ```bash
     cd app/log
     ```
3. The log file contains information such as the generation of the fixed-width file, the conversion of the fixed-width file to CSV, and any errors that occurred during the process.

## Unit Testing:
1. To run the unit tests, navigate to the app/unittesting directory:
   ```bash
   cd app/unittesting
   ```
2. Execute the unit test script:
     ```bash
     python unit_test.py
     ```
   The test results will be displayed in the console, indicating whether the tests passed or failed.

## Build the Docker image:

1. Build the docker image. Before run the command, make sure we are in the "app" directory
   docker build -t latitude-code-challenge .
   
2. Run the Docker container:
   docker run -v $(pwd)/data:/app/data latitude-code-challenge
   This command mounts the data directory from the host into the container, allowing the script to access the input specification file (spec.json) and saving the output files (fixed_width_file.txt and csv_file.csv) to the data directory on the host.

   The generated fixed-width file (fixed_width_file.txt) and CSV file (csv_file.csv) will be saved in the data directory on your host machine.

   You can modify the input specification file (spec.json) in the src directory to change the column names, offsets, encoding, or other parameters.

If you want to change the output file path within the container, modify the fixed_width_file variable in the Python script (app/src/latitude_code_challenge.py) accordingly.

## Notes

- If you want to change the output file path, modify the `fixed_width_file` variable in the Python script (`app/src/latitude_code_challenge.py`) accordingly.

- The generated CSV file (`csv_file.csv`) will also be saved in the `data` directory. You can find it after running the script.


