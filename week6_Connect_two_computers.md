# WEEK 6: Establishing a Network Between Computers

**Practical Experiment**

## 1. Aim

To establish a network connection between two computers using a direct Ethernet cable, configure static IP addresses, and verify communication using the `ping` command.

## 2. Requirements

1. Two computers (PC1 and PC2).
2. Ethernet cable (RJ45).
3. Windows operating system.
4. Network Interface Cards (NICs).

## 3. Procedure

### Step 1: Connect Both Computers

1. Connect PC1 and PC2 using a direct Ethernet cable.
2. Disconnect Wi-Fi on both computers to avoid network interference.
3. Open Command Prompt on both computers.

### Step 2: Assign Static IP Addresses

Configure the following IP addresses on the respective computers.

**PC1 Configuration**

- IP Address: `192.168.20.1`
- Subnet Mask: `255.255.255.0`
- Default Gateway: Leave blank
- DNS Server: Leave blank

**PC2 Configuration**

- IP Address: `192.168.20.2`
- Subnet Mask: `255.255.255.0`
- Default Gateway: Leave blank
- DNS Server: Leave blank

**Configuration Steps:**

1. Open Settings → Network & Internet → Ethernet.
2. Under IP Assignment, click **Edit**.
3. Select **Manual**.
4. Enable **IPv4**.
5. Enter the respective IP address and subnet mask.
6. Leave Default Gateway and DNS fields blank.
7. Click **Save**.

### Step 3: Verify IP Configuration

Open Command Prompt on both computers and execute:

```cmd
ipconfig
```

**Expected Output on PC1:**

```text
IPv4 Address: 192.168.20.1
Subnet Mask: 255.255.255.0
```

**Expected Output on PC2:**

```text
IPv4 Address: 192.168.20.2
Subnet Mask: 255.255.255.0
```

### Step 4: Configure Windows Firewall

On both computers, open Command Prompt as Administrator and execute:

```cmd
netsh advfirewall firewall add rule name="Lab ICMPv4 Echo" protocol=icmpv4:8,any dir=in action=allow
```

**Expected Output:**

```text
Ok.
```

This command allows incoming ICMPv4 Echo Requests, which are required for successful ping communication.

### Step 5: Test Network Connectivity

**From PC1, execute:**

```cmd
ping 192.168.20.2
```

**From PC2, execute:**

```cmd
ping 192.168.20.1
```

**Expected Result:**

```text
Packets: Sent = 4, Received = 4, Lost = 0 (0% loss)
```

Successful replies indicate that both computers can communicate over the Ethernet connection.

## 4. Additional Networking Commands

Execute the following commands on both computers.

| Command | Purpose |
|---|---|
| `ipconfig` | Displays IP address configuration. |
| `ipconfig /all` | Displays detailed network configuration. |
| `ping <IP>` | Tests network connectivity. |
| `arp -a` | Displays IP-to-MAC address mappings. |
| `hostname` | Displays the computer name. |
| `getmac` | Displays the MAC address. |
| `tracert <IP>` | Traces the network route to a destination. |
| `netstat -an` | Displays network connections and listening ports. |

## 5. Screenshots for Lab Record

Capture the following four screenshots as proof of successful execution:

1. PC1 IP configuration using `ipconfig`.
2. PC2 IP configuration using `ipconfig`.
3. Successful ping from PC1 to PC2.
4. Successful ping from PC2 to PC1.

## 6. Important Note: Previous Wi-Fi Experiment

In the earlier Wi-Fi experiment, the following IP addresses were used:

| Device | IP Address |
|---|---|
| PC1 | `192.168.0.102` |
| PC2 | `192.168.0.103` |
| Router | `192.168.0.1` |

Both computers could successfully ping the router but could not communicate directly with each other.

This issue may have been caused by **Wireless Client Isolation (AP Isolation)** configured on the router.

The Wi-Fi experiment and the direct Ethernet experiment are separate tests. Do not mix their IP addresses or configurations.

## 7. Result

A direct Ethernet network was established between two computers by assigning static IP addresses. Network connectivity was successfully verified using the `ping` command.

**Troubleshooting note:** The firewall command should be executed on both PCs, and the Ethernet adapter must show a connected link. If ping fails, check the Ethernet connection, IP configuration, and firewall rule before concluding that the experiment failed.
