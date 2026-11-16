# Python Network Speed Test

A Python-based internet speed testing tool that measures download speed, upload speed, network latency, and jitter.

## Features

- Measure download speed (Mbps).
- Measure upload speed (Mbps).
- Measure network latency (Ping).
- Measure network jitter.
- Display internet service provider (ISP).
- Display selected test server information.
- Simple and easy-to-use terminal interface.

## Technologies Used

- Python
- Speedtest-cli
- Colorama
- Subprocess
- Statistics

## Requirements

- Python 3.8 or newer
- Internet connection

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/pradipta-web/python-network-speed-test.git
   ```

2. Navigate to the project directory:

   ```bash
   cd python-network-speed-test
   ```

3. Install dependencies:

   ```bash
   py -m pip install -r requirements.txt
   ```

## Usage

Run the application:

```bash
py main.py
```

The application will automatically:

1. Find the best available Speedtest server.
2. Measure download speed.
3. Measure upload speed.
4. Measure network latency.
5. Calculate jitter using multiple ping measurements.
6. Display the test results.

## Project Structure

```text
python-network-speed-test/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Notes

- An active internet connection is required.
- Download and upload speeds are measured using Speedtest servers.
- Jitter is estimated using five ping measurements to `1.1.1.1`.
- Test results may vary depending on network conditions and server availability.

## Author

**Kinervaaa**