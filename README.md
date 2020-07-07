# Utility to scrape the darknet
This project is a collection of open source projects and custom parsers to scrape the darknet marketplaces to produce a JSON that can be digested by the ELK stack.

# Recommended
- Ubuntu 16.04 or newer
- 8GB of RAM
- 16GB minimum of Storage

# TOR Setup
Install TOR `apt install tor`

Run tor `service sudo service tor star`

Set a password `tor --hash-password "my_password"`

Copy the hash of your password to the file `/Modules/Scrape.py` and replace with your new generated hash.

Navigate to `nano /etc/tor/torrc` and uncomment `ControlPort 9051`

# Running the Crawler or Scraper
Navigate into the project directory `cd Darknet-Stack Scrape`

Add an onion link to the the file `nano onions.txt` 

Run the driver code `python3 main.py`

# Credit
[Abhisek Singn](https://github.com/absingh31/Tor_Spider)