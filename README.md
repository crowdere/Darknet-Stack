# Setting up TOR
Run tor `service sudo service tor star`

Set a password `tor --hash-password "my_password"`

Copy the hash of your password to the file `/Modules/Scrape.py` 
`from stem.control import Controller with Controller.from_port(port = 9051) as controller: controller.authenticate("your_password_hash") controller.signal(Signal.NEWNYM)`

Go to /etc/tor/torrc and uncomment `ControlPort 9051` 