# Port Scanner

A multi-threaded Python port scanner. You give it a host and a port range, and it tells you which ports are open and what's likely running on them.

## How it works

- Uses 10 threads pulling from a shared, thread-safe queue so ports get scanned in parallel instead of one at a time
- Resolves the hostname to an IP first
- Checks each port with a raw socket connection (1-second timeout)
- Matches open ports against a dictionary of common services (FTP, SSH, HTTP, DNS, MySQL, etc.)
- Prints a summary of everything it found once all threads finish

## Run it

```
python port_scanner.py
```

Then enter a target host and a port range like `1-1000` when prompted.

## Example runs

Scanned `8.8.8.8` (Google DNS) — port 53 came back open and correctly identified as DNS.

Scanned `127.0.0.1` (localhost) — port 135 came back open, labeled "Unknown" since it's not in the service dictionary.

## Known services it recognizes

FTP, SSH, Telnet, SMTP, DNS, HTTP, IMAP, HTTPS, MySQL, PostgreSQL, VNC, HTTP-Alt, HTTPS-Alt

## Built with

- Python 3
- `socket` for the actual connections
- `threading` + `queue` for running scans in parallel

## Author

Mofolorunsho Adeleke
