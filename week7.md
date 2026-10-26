# Basic Kali Linux Commands --- Step by Step

Run commands in the Kali Linux terminal. Commands that change system
settings or install software may require `sudo`.

## 1. Basic navigation and files

### Show the current directory

``` bash
pwd
```

### List files and folders

``` bash
ls
```

### List files, including hidden files, with details

``` bash
ls -la
```

### Change directory

``` bash
cd Documents
```

### Go to the home directory

``` bash
cd ~
```

### Go up one directory

``` bash
cd ..
```

### Create a directory

``` bash
mkdir practice
```

### Create an empty file

``` bash
touch notes.txt
```

### Display a file's contents

``` bash
cat notes.txt
```

### Copy a file

``` bash
cp notes.txt notes-copy.txt
```

### Rename or move a file

``` bash
mv notes.txt new-notes.txt
```

### Delete a file

``` bash
rm new-notes.txt
```

### Delete an empty directory

``` bash
rmdir practice
```

## 2. System information

### Display the current username

``` bash
whoami
```

### Display the computer name

``` bash
hostname
```

### Display Linux and kernel information

``` bash
uname -a
```

### Display operating-system details

``` bash
cat /etc/os-release
```

### Display date and time

``` bash
date
```

### Show command history

``` bash
history
```

### Clear the terminal screen

``` bash
clear
```

## 3. Network commands

### Display IP addresses

``` bash
ip addr
```

### Display network interfaces

``` bash
ip link
```

### Display the routing table and default gateway

``` bash
ip route
```

### Test connectivity to a host

``` bash
ping -c 4 8.8.8.8
```

### Test DNS name resolution

``` bash
nslookup example.com
```

### Alternative DNS lookup

``` bash
dig example.com
```

### Display the path to a host

``` bash
traceroute example.com
```

### Display listening ports and connections

``` bash
ss -tuln
```

### Display the ARP/neighbour table

``` bash
ip neigh
```

### Display network interface details (if installed)

``` bash
ip -s link
```

## 4. Package management

### Update package lists

``` bash
sudo apt update
```

### Upgrade installed packages

``` bash
sudo apt full-upgrade
```

### Install a package

``` bash
sudo apt install package-name
```

### Remove a package

``` bash
sudo apt remove package-name
```

### Search for a package

``` bash
apt search package-name
```

## 5. Processes and performance

### Show running processes

``` bash
ps aux
```

### View processes interactively

``` bash
top
```

### Show memory usage

``` bash
free -h
```

### Show disk space

``` bash
df -h
```

### Show directory sizes

``` bash
du -sh *
```

## 6. Users and permissions

### Display file permissions

``` bash
ls -l
```

### Change file permissions

``` bash
chmod 644 notes.txt
```

### Run a command with administrator privileges

``` bash
sudo command
```

### Show user and group IDs

``` bash
id
```

## 7. Text and command-line utilities

### Search for text in a file

``` bash
grep "word" notes.txt
```

### Display the first 10 lines

``` bash
head notes.txt
```

### Display the last 10 lines

``` bash
tail notes.txt
```

### Follow new lines added to a log

``` bash
tail -f /var/log/syslog
```

### Find a file by name in the current directory tree

``` bash
find . -name "notes.txt"
```

### Show a command's manual

``` bash
man ls
```

### Show help for a command

``` bash
ls --help
```

## 8. Download and transfer utilities

### Fetch a webpage's response headers

``` bash
curl -I https://example.com
```

### Download a file from a trusted URL

``` bash
wget https://example.com/file.txt
```

## 9. Security and network inspection (authorized systems only)

### Show Nmap version

``` bash
nmap --version
```

### Scan your own machine for open TCP ports

``` bash
nmap 127.0.0.1
```

### Detect services on an authorized host

``` bash
nmap -sV 192.168.1.10
```

### Run default Nmap scripts against an authorized host

``` bash
nmap -sC 192.168.1.10
```

Replace `192.168.1.10` with a host you own or have explicit permission
to test. Do not scan networks or devices without authorization.

## 10. Helpful shortcuts

-   `Tab` --- autocomplete commands and paths.
-   `↑` / `↓` --- move through command history.
-   `Ctrl + C` --- stop the current command.
-   `Ctrl + L` --- clear the terminal view.
-   `command1 && command2` --- run the second command only if the first
    succeeds.
-   `command1 ; command2` --- run both commands in sequence.

## Notes

-   Replace example names such as `example.com`, `package-name`, and
    `192.168.1.10` with appropriate values.
-   If a command is missing, install its package using
    `sudo apt install package-name` where available.
-   Some commands may behave differently depending on the Kali Linux
    version, network configuration, and permissions.
