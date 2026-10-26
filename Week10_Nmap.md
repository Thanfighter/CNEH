# Week 10 — Network Scanning with Nmap: Host Discovery and Port Scanning

## Aim
To discover live hosts on a network and scan their open ports using Nmap (Network Mapper).

## Final Command Checklist

```bash
# 1. Install Nmap if needed
sudo apt update
sudo apt install nmap -y

sudo su

nmap 132.148.130.26 

nmap -ns 132.148.130.26

nmap -sn 132.148.130.26

nmap -v 132.148.130.26

nmap -sS 132.148.130.26

nmap -sT 132.148.130.26

nmap -sU 132.148.130.26

nmap -p 0-65535 132.148.130.26
```

## Port States

| State | Meaning |
|---|---|
| `open` | An application is listening and accepting connections |
| `closed` | The host is reachable, but no application is listening |
| `filtered` | A firewall or other filter prevents Nmap from determining the state |
| `unfiltered` | The port is reachable, but Nmap cannot determine whether it is open or closed |

## Observation Table

| Scan | What to Record |
|---|---|
| Host discovery | Live hosts detected |
| Default scan | Open, closed, and filtered common ports |
| Selected-port scan | State of ports 22, 80, and 443 |
| UDP scan | Results for selected common UDP ports |
| Saved output | File names and important findings |

## Result
Nmap was used to discover hosts and inspect TCP/UDP port states. Record the actual scan output and explain any `open`, `closed`, or `filtered` states observed.

## Ethics Note
Scan only your own lab network, instructor-provided machines, or targets for which you have explicit authorization. Replace `192.168.56.0/24` with the subnet assigned for your lab.
