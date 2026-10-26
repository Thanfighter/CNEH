# Week 9 — DNS and Mail Server Enumeration (nslookup, host, dig)

## Aim
To enumerate DNS records and mail (SMTP) servers of a domain using `nslookup`, `host`, and `dig`, and understand how this information supports reconnaissance in an ethical hacking engagement.

## Final Command Checklist

```bash
# 1. Install DNS utilities if needed
sudo apt update
sudo apt install dnsutils bind9-host -y

# 2. Look up the default A record
nslookup vnrvjiet.ac.in

# 3. Query mail server (MX) records
nslookup -type=MX vnrvjiet.ac.in

# 4. Query name server records
nslookup -type=NS vnrvjiet.ac.in

# 5. Query SOA, TXT, and IPv6 (AAAA) records
nslookup -type=SOA vnrvjiet.ac.in

nslookup -type=TXT vnrvjiet.ac.in

nslookup -type=AAAA vnrvjiet.ac.in


# 7. Query records with host
host vnrvjiet.ac.in
host -t mx vnrvjiet.ac.in
host -t ns vnrvjiet.ac.in
host -t soa vnrvjiet.ac.in
host -t txt vnrvjiet.ac.in
host -t A vnrvjiet.ac.in
host -t AAAA vnrvjiet.ac.in

# 8. Query records with dig
dig vnrvjiet.ac.in A +short
dig vnrvjiet.ac.in mx +short
dig vnrvjiet.ac.in ns +short
dig vnrvjiet.ac.in txt +short
dig vnrvjiet.ac.in soa +short
# 9. Attempt a zone transfer only against an authorized lab name server
dig vnrvjiet.ac.in any

dnsenum vnrvjiet.ac.in

dnsrecon -d vnrvjiet.in
```

## Key Record Types

| Record | Meaning |
|---|---|
| A | Hostname to IPv4 address |
| AAAA | Hostname to IPv6 address |
| MX | Mail exchanger |
| NS | Authoritative name server |
| SOA | Primary name server and zone administration data |
| CNAME | Alias to another hostname |
| TXT | Text records such as SPF, DKIM, and domain verification |
| PTR | Reverse lookup from IP address to hostname |

## Observation Table

| Tool / Query | Key Information Found |
|---|---|
| `nslookup` | A, MX, NS, SOA, TXT, AAAA and reverse lookup results |
| `host` | DNS records in concise form |
| `dig` | DNS answer sections and record details |
| Zone transfer check | Whether the authorized server refuses or permits AXFR |
| SMTP banner (optional) | Mail software banner, if exposed by the lab server |

## Result
DNS records and mail-server information were queried using `nslookup`, `host`, and `dig`. Record the actual outputs and note that MX records with lower preference values have higher priority.

## Ethics Note
Use only public DNS queries and explicitly authorized lab targets. Attempt zone transfers and SMTP banner checks only against systems you are permitted to test.
