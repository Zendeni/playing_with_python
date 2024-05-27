# pcap-to-kml

## Description

`pcap-to-kml` is a Python script that processes a packet capture (pcap) file to generate KML (Keyhole Markup Language) data, which can be used to visualize IP addresses on geographic maps, such as Google Earth.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python 3.x
- `dpkt` library: For parsing pcap files
- `pygeoip` library: For geolocation lookup
- A GeoIP database file (e.g., Geo.dat)

## Installation

You can install the required libraries using pip:

```bash
pip install dpkt pygeoip
```

## Usage

python pcap_to_kml.py -p <pcap_file>

The output KML data is printed to the console. You can redirect this to a file if needed.

python pcap_to_kml.py -p example.pcap > output.kml
