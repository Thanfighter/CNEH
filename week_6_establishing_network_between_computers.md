# WEEK 6: Establishing a Network Between Computers

**Experiment:** Establishing a direct network connection between two computers using an Ethernet cable.

## 1. Aim

To establish a network connection between two computers using an Ethernet cable, configure static IP addresses, and verify communication using the `ping` command.

## 2. Requirements

1. Two computers (PC1 and PC2).
2. An Ethernet cable (RJ45).
3. Windows operating system on both computers.
4. Ethernet network interface cards (NICs) on both computers.

## 3. Network Topology

The two computers are connected directly using an Ethernet cable.

```text
+----------------------+         Ethernet cable         +----------------------+
|         PC1          |---------------------------------|         PC2          |
| IP: 192.168.20.1     |                                 | IP: 192.168.20.2     |
| Mask: 255.255.255.0  |                                 | Mask: 255.255.255.0  |
+----------------------+                                 +----------------------+
```

Both computers belong to the same IPv4 subnet (`192.168.20.0/24`).

## 4. Procedure

### Step 1: Connect the computers

1. Connect PC1 and PC2 using the Ethernet cable.
2. Check that the Ethernet connection is detected on both computers. The Ethernet adapter should show a connected status.
3. Open **Command Prompt** on both computers.

### Step 2: Check the current network configuration

Run the following command on both computers:

```cmd
ipconfig
```

This command displays the IP address, subnet mask, and default gateway for the network adapters.

For this experiment, static IPv4 addresses will be assigned manually to the Ethernet adapters.

### Step 3: Assign static IP addresses

Use the following configuration:

| Configuration | PC1 | PC2 |
|---|---|---|
| IPv4 address | `192.168.20.1` | `192.168.20.2` |
| Subnet mask | `255.255.255.0` | `255.255.255.0` |
| Default gateway | Leave blank | Leave blank |
| Preferred DNS server | Leave blank | Leave blank |

**Steps to configure the IP address:**

1. Open **Control Panel**.
2. Select **Network and Internet**.
3. Open **Network and Sharing Center**.
4. Click **Change adapter settings**.
5. Right-click the **Ethernet** adapter and select **Properties**.
6. Select **Internet Protocol Version 4 (TCP/IPv4)** and click **Properties**.
7. Select **Use the following IP address**.
8. Enter the IP address and subnet mask specified for that computer in the table above.
9. Leave the default gateway and DNS fields blank.
10. Click **OK**, then **Close**.

Repeat these steps on the other computer, using its assigned IP address.

> **Important:** Configure the physical Ethernet adapter used for the cable connection. Do not change the settings for Wi-Fi, VPN, VirtualBox, or other virtual network adapters.

### Step 4: Verify the IP configuration

On PC1, run:

```cmd
ipconfig
```

Expected Ethernet adapter details:

```text
IPv4 Address . . . . . . . . . . : 192.168.20.1
Subnet Mask  . . . . . . . . . . : 255.255.255.0
```

On PC2, run:

```cmd
ipconfig
```

Expected Ethernet adapter details:

```text
IPv4 Address . . . . . . . . . . : 192.168.20.2
Subnet Mask  . . . . . . . . . . : 255.255.255.0
```

### Step 5: Test connectivity using PING

The `ping` command tests whether one computer can communicate with another over an IP network. It sends ICMP Echo Request packets and waits for replies.

**From PC1, ping PC2:**

```cmd
ping 192.168.20.2
```

Sample successful output:

```text
Pinging 192.168.20.2 with 32 bytes of data:
Reply from 192.168.20.2: bytes=32 time=1ms TTL=128
Reply from 192.168.20.2: bytes=32 time=1ms TTL=128
Reply from 192.168.20.2: bytes=32 time=1ms TTL=128
Reply from 192.168.20.2: bytes=32 time=1ms TTL=128

Ping statistics for 192.168.20.2:
    Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
```

**From PC2, ping PC1:**

```cmd
ping 192.168.20.1
```

A successful test should report four packets sent, four received, and zero lost (0% packet loss).

If both tests succeed, the computers can communicate with each other over the Ethernet connection.

### Step 6: Check the ARP table

Run the following command on both computers:

```cmd
arp -a
```

The Address Resolution Protocol (ARP) table displays IP-to-MAC address mappings learned by the computer. After a successful ping, PC1 should normally show an entry for `192.168.20.2`, and PC2 should normally show an entry for `192.168.20.1`.

### Step 7: Check the MAC address

Run:

```cmd
getmac
```

This command displays the MAC addresses of the network adapters. Identify the entry corresponding to the Ethernet adapter used in the experiment.

## 5. Commands Used in the Experiment

| Command | Purpose |
|---|---|
| `ipconfig` | Displays IP configuration. |
| `ipconfig /all` | Displays detailed network configuration, including physical addresses and adapter details. |
| `ping IP-address` | Tests network connectivity with the specified IP address. |
| `arp -a` | Displays the ARP table containing IP-to-MAC address mappings. |
| `getmac` | Displays the MAC addresses of network adapters. |
| `hostname` | Displays the computer's host name. |
| `tracert IP-address` | Traces the route taken by packets to the destination. For two computers on the same local subnet, intermediate routers are generally not involved. |

## 6. Troubleshooting

If the ping test fails, check the following:

1. Confirm that the Ethernet cable is properly connected and that both Ethernet adapters show a connected status.
2. Verify that PC1 and PC2 have the correct IP addresses and the same subnet mask.
3. Make sure the IP addresses are configured on the physical Ethernet adapters, not on Wi-Fi or virtual adapters.
4. Check whether Windows Firewall is blocking ICMP Echo Requests. The relevant inbound rule may need to be enabled for the active network profile, subject to the computer's security policy.
5. Run `ipconfig` again to confirm that the settings have been applied correctly.

## 7. Result

A direct network connection was established between two computers using an Ethernet cable. Static IP addresses `192.168.20.1` and `192.168.20.2` were assigned with the subnet mask `255.255.255.0`. Communication between the computers was verified using the `ping` command. Successful communication is indicated by four packets received and 0% packet loss in both directions.
