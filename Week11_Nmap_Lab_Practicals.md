# WEEK 11: Nmap Lab Practicals

**Target IP used in all commands:** `scanme.nmap.org`

Run these commands in the Kali Linux terminal only if you are authorized
to scan this target.

## A) Detect Service, Version, and OS Using Nmap

### 1. Detect the operating system

``` bash
nmap -O scanme.nmap.org
```

### 2. Detect services and versions

``` bash
nmap -sV 1scanme.nmap.org
```

### 3. Detect services, versions, and operating system

``` bash
nmap -sV -O scanme.nmap.org
```

### 4. Scan specific ports

``` bash
nmap -p 21,22,80,443 scanme.nmap.org
```

## B) Scanning Using Nmap Scripts

### 5. Run default Nmap scripts

``` bash
nmap -sC scanme.nmap.org
```

### 6. Run default scripts and detect service versions

``` bash
nmap -sC -sV scanme.nmap.org
```

### 7. Run vulnerability-checking scripts

``` bash
nmap --script vuln scanme.nmap.org
```

### 8. Run the HTTP title script on ports 80 and 443

``` bash
nmap --script http-title -p 80,443 scanme.nmap.org
```

### 9. List available Nmap scripts

``` bash
ls /usr/share/nmap/scripts/
```

### 10. Display Nmap help

``` bash
nmap -h
```

## Quick Revision

  -----------------------------------------------------------------------
  Option / Command                    Purpose
  ----------------------------------- -----------------------------------
  `-O`                                Detect operating system

  `-sV`                               Detect service versions

  `-sC`                               Run default NSE scripts

  `--script vuln`                     Run vulnerability-checking scripts

  `-p`                                Specify ports

  `-A`                                Enable OS detection, version
                                      detection, default scripts, and
                                      traceroute
  -----------------------------------------------------------------------

## Four Main Commands to Memorize

``` bash
nmap -O scanme.nmap.org
nmap -sV scanme.nmap.org
nmap -sC scanme.nmap.org
nmap --script vuln scanme.nmap.org
```
