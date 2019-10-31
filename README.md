# handy code snippets
This is a collection of random bits of code that are either useful or interesting (or sometimes neither).


### batgraph
Python script that prints battery percentage vs. time. Designed to be used in conjunction with a cron job (see `cronbatlife`) that echos the battery percentage at certain intervals to the file `$HOME/.local/share/battery-life.csv`.

### cronbatlife
Bash script that echos the current time and the battery percentage into the specified file. To implement:
```
$ crontab -e
> */5 * * * * /path/to/cronbatlife/
```

### ipparser
Python script that reads your current public IP and prints the geolocation of that IP to the terminal. Useful to check if your VPN is working.
