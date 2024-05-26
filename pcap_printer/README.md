# Packet Sniffer Tool

A simple packet sniffer written in Python that reads packets from a pcap file, extracts IP addresses, and retrieves geographical information for the source and destination IPs. 

## Prerequisites

- Python 3.x
- `dpkt` library
- `pygeoip` library
- GeoIP database file (e.g., Geo.dat)

## Installation

1. **Clone the repository** (if applicable) or download the script file.

2. **Install required libraries**:
    ```sh
    pip install dpkt pygeoip
    ```

3. **Download and set up the GeoIP database**:
    - Place the GeoIP database file (e.g., `Geo.dat`) in the directory `/opt/GeoIP/`.
    - You can obtain the GeoIP database from [MaxMind's website](https://www.maxmind.com/en/geoip2-databases).

## Usage

Run the script with the path to your pcap file as an argument:

```sh
python packet_sniffer.py -p <pcap_file>
```

![image](https://github.com/Zendeni/playing_with_python/assets/53412927/7184c516-74ba-46b2-a491-d93ed5190bf8)

