# WEEK 4: Basic Networking Commands

Run these commands one by one in **Windows Command Prompt (CMD)**.

## 1. Display IP address, subnet mask, default gateway, and DNS server

``` cmd
ipconfig /all
```

## 2. Check communication with the local router

``` cmd
ping 10.100.0.1
```

## 3. Check whether the EduPrime server is reachable

``` cmd
ping automation.vnrvjiet.ac.in
```

## 4. Find the IP address of vnrvjiet.ac.in

``` cmd
nslookup vnrvjiet.ac.in
```

## 5. Display the path to vnrvjiet.ac.in

``` cmd
tracert vnrvjiet.ac.in
```

## 6. Display TCP and UDP connections

``` cmd
netstat -ano
```

## 7. Check whether TCP port 8080 is in use

``` cmd
netstat -ano | findstr :8080
```

## 8. Display MAC addresses of network adapters

``` cmd
getmac
```

## 9. Display the Windows routing table

``` cmd
route print
```

## 10. Display IP-to-MAC address mappings

``` cmd
arp -a
```

## 11. Display the computer's host name

``` cmd
hostname
```

## 12. Check whether the default gateway is reachable

``` cmd
ping 10.100.0.1
```
