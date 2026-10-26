# Final Command Checklist – Passive Information Gathering in Kali Linux

**Target domain:** `vnrvjiet.ac.in`  
*(You can replace it with `wikipedia.org` if required.)*

## Part A: Whois Lookup

```bash
# 1. Install Whois
sudo apt update
sudo apt install whois -y

# 2. Find domain registration details
whois vnrvjiet.ac.in

# 3. Find IP network ownership details
whois 8.8.8.8
```

**Web lookup:**
- [ICANN Lookup](https://lookup.icann.org)
- [.IN Registry](https://www.registry.in)

## Part B: Netcraft Site Report

Open the following website in your browser:

[Netcraft Site Report](https://sitereport.netcraft.com)

Enter:

```text
https://vnrvjiet.ac.in
```

Repeat for a second website:

```text
https://wikipedia.org
```

## Part C: Website History – Wayback Machine

```bash
# 1. View archived versions of the website
# Open this URL in your browser:
# https://web.archive.org/web/*/vnrvjiet.ac.in/*

# 2. List archived captures using the CDX API
curl "https://web.archive.org/cdx/search/cdx?url=vnrvjiet.ac.in&output=text&fl=timestamp,original,statuscode&filter=statuscode:200&limit=10"

# 3. Archive the current page (optional)
# Open this URL in your browser:
# https://web.archive.org/save/https://vnrvjiet.ac.in
```

**Note:** The archive URLs are for your browser, not terminal commands. The `curl` command retrieves archived capture information.

## Part D: Search Engine Operators (Google Dorking)

Open [Google Search](https://www.google.com) and run these queries individually.

```text
# 1. Find indexed pages
site:vnrvjiet.ac.in

# 2. Find PDF documents
site:vnrvjiet.ac.in filetype:pdf

# 3. Find pages containing "admission" in the title
site:vnrvjiet.ac.in intitle:admission

# 4. Find URLs containing "admission"
site:vnrvjiet.ac.in inurl:admission

# 5. Find pages containing the exact word "contact"
site:vnrvjiet.ac.in intext:"contact"

# 6. Find syllabus PDFs
site:vnrvjiet.ac.in filetype:pdf intitle:syllabus

# 7. Find pages mentioning either syllabus or timetable
site:vnrvjiet.ac.in (syllabus OR timetable)

# 8. Find pages indexed after January 1, 2024
site:vnrvjiet.ac.in after:2024-01-01

# 9. Search for an exact phrase
site:vnrvjiet.ac.in "information technology"

# 10. Exclude results containing the term "www"
site:vnrvjiet.ac.in -www
```

## Part E: IP Geolocation of the Server

```bash
# 1. Resolve the domain name
nslookup vnrvjiet.ac.in

# 2. Obtain the IPv4 address directly
dig +short A vnrvjiet.ac.in

# 3. Test connectivity
ping -c 4 vnrvjiet.ac.in

# 4. Look up geolocation (replace with the actual IP)
curl https://ipinfo.io/YOUR_IP_ADDRESS

# 5. Identify the network owner and ASN
whois YOUR_IP_ADDRESS

# 6. Trace the network path (optional)
traceroute vnrvjiet.ac.in
```

If `dig` or `traceroute` is unavailable:

```bash
sudo apt update
sudo apt install dnsutils traceroute -y
```

**Web-based geolocation:**
- [IPLocation](https://www.iplocation.net)
- [IPinfo](https://ipinfo.io)

## Final Observation Table

| Technique | Tool Used | Target | Key Information Found |
|---|---|---|---|
| Whois | `whois` | `vnrvjiet.ac.in` | Registrar, registration dates, name servers |
| Netcraft | Netcraft Site Report | `vnrvjiet.ac.in` | Hosting provider, server technology, SSL/TLS |
| Wayback Machine | Internet Archive | `vnrvjiet.ac.in` | Historical website versions |
| Search Operators | Google | `vnrvjiet.ac.in` | Indexed pages, PDFs, and public information |
| IP Geolocation | `nslookup`, `dig`, `curl`, `whois` | Server IP address | Country, region, city, network owner, ASN |

## Result

Various passive information-gathering techniques were performed to examine publicly available domain registration details, hosting infrastructure, website history, indexed content, and approximate server location.

## Ethics Note

This lab focuses on passive reconnaissance using publicly available information. Perform reconnaissance only within an authorized scope. Do not use these techniques to profile individuals or organizations without permission, and do not send attack traffic to the target.
