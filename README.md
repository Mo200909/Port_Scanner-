# Port_Scanner-

# Port Scanner

A multi-threaded Python tool that scans network ports and identifies open services.

## What It Does

Scans a target host for open ports using 10 concurrent threads. Shows which ports are open and what services run on them (SSH, HTTP, HTTPS, DNS, etc.).

## How to Use

```bash
python Port_Scanner.py

Enter Target Host: 8.8.8.8
Enter Target Ports (e.g., 1-1000): 1-100
```

**Output:**
```
Port 53 is open (DNS)
```

## Features

- **Multi-threaded** — 10 concurrent threads for speed
- **Service mapping** — Identifies common ports (22=SSH, 80=HTTP, 443=HTTPS, etc.)
- **Hostname resolution** — Works with domain names or IPs
- **Clean output** — Shows summary of results

## How It Works

1. Takes the target host and port range from the user
2. Resolves hostname to IP address
3. Uses a thread-safe queue to distribute ports to 10 worker threads
4. Each thread tests connection to a port (1-second timeout)
5. Open ports are logged with service names
6. Displays an organized summary

## Technical Details

- **Language:** Python 3.6+
- **Libraries:** socket, threading, queue (standard library only)
- **Threading:** 10 worker threads pull from the queue
- **Connection:** Uses `socket.connect_ex()` for non-blocking checks
- **Performance:** ~1000 ports in ~100 seconds

## Testing

Safe public servers to test:
- `8.8.8.8` (Google DNS) — Port 53 should be open
- `1.1.1.1` (Cloudflare) — Port 53 should be open
- `google.com` — Ports 80, 443 should be open

## Code Structure

```
SERVICE_PORTS dict    → Maps ports to service names
scan_ports()          → Worker thread function
main()                → User input and thread management
```

## Legal Note

Only scan systems you own or have permission to test.
