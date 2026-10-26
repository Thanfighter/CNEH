# WEEK 5: Configuring an FTP Server for File Sharing

## Aim

To configure an FTP server using IIS on Windows and test file download
and upload from an FTP client.

## Requirements

-   Windows with Internet Information Services (IIS)
-   Administrator access
-   Two devices on the same network, or a suitable local lab setup
-   A test file named `text1.txt`

## Step 1: Enable IIS FTP Server

1.  Press `Windows + R`.

2.  Type:

    ``` text
    optionalfeatures
    ```

3.  Press **Enter**.

4.  Expand **Internet Information Services**.

5.  Expand **FTP Server**.

6.  Enable:

    -   **FTP Service**
    -   **FTP Extensibility**

7.  Expand **Web Management Tools** and enable **IIS Management
    Console** if it is not already enabled.

8.  Click **OK** and wait for installation to finish.

## Step 2: Create the Shared Folder

1.  Open File Explorer.

2.  Create this folder:

    ``` text
    C:\FTP\Shared
    ```

3.  Create a test file inside it:

    ``` text
    C:\FTP\Shared\text1.txt
    ```

To create the file from Command Prompt, run:

``` cmd
mkdir C:\FTP\Shared
echo FTP test file > C:\FTP\Shared\text1.txt
```

## Step 3: Open IIS Manager

1.  Press `Windows + R`.

2.  Type:

    ``` text
    inetmgr
    ```

3.  Press **Enter**.

## Step 4: Create the FTP Site

1.  In IIS Manager, expand the computer name.
2.  Right-click **Sites**.
3.  Select **Add FTP Site**.
4.  Enter:
    -   **FTP site name:** `MyFTP`
    -   **Physical path:** `C:\FTP\Shared`
5.  Click **Next**.

## Step 5: Configure Binding and SSL

Set the following options:

-   **IP Address:** All Unassigned
-   **Port:** `21`
-   **Start FTP site automatically:** Enabled
-   **SSL:** No SSL (for the isolated lab only)

Click **Next**.

> **Security note:** FTP without SSL sends credentials and data without
> encryption. Use this configuration only in an isolated lab. For real
> networks, configure secure FTP such as FTPS or SFTP as appropriate.

## Step 6: Configure Authentication and Authorization

For the anonymous-access lab configuration:

-   **Authentication:** Anonymous
-   **Authorization:** Anonymous users
-   **Permissions:** Read and Write

Click **Finish**.

## Step 7: Set Folder Permissions

1.  Open `C:\FTP`.

2.  Right-click the `Shared` folder and select **Properties**.

3.  Open the **Security** tab.

4.  Click **Edit** → **Add**.

5.  Enter:

    ``` text
    IUSR
    ```

6.  Click **Check Names** → **OK**.

7.  Select `IUSR` and allow the permissions required for the lab:

    -   Read
    -   Write
    -   Modify

8.  Click **Apply** → **OK**.

## Step 8: Find the Server IP Address

Open Command Prompt and run:

``` cmd
ipconfig
```

Find the IPv4 address of the network adapter connected to the lab
network.

Example address from the lab handout:

``` text
10.100.2.57
```

The corresponding FTP address is:

``` text
ftp://10.100.2.57
```

> Replace `10.100.2.57` with the actual IPv4 address of your FTP server.

## Step 9: Connect to the FTP Server

Open Command Prompt on the client computer and run:

``` cmd
ftp 10.100.2.57
```

At the prompts, enter:

``` text
Username: anonymous
Password: [press Enter if anonymous login permits a blank password]
```

Successful login typically displays:

``` text
230 User logged in.
ftp>
```

## Step 10: Test Read Permission (Download)

At the `ftp>` prompt, run each command:

``` text
dir
get text1.txt
bye
```

Expected result: - `dir` lists `text1.txt`. - `get text1.txt` downloads
the file. - A successful transfer may display `226 Transfer complete.`

## Step 11: Test Write Permission (Upload)

On the client computer, open a separate Command Prompt and create a test
file:

``` cmd
echo FTP Write Test > upload.txt
```

Connect to the FTP server:

``` cmd
ftp 10.100.2.57
```

At the FTP prompts, enter the anonymous login details if requested. Then
run:

``` text
put upload.txt
dir
bye
```

Expected result: - `put upload.txt` uploads the file. - A successful
transfer may display `226 Transfer complete.` - `dir` should list both
`text1.txt` and `upload.txt`.

## Quick Command Revision

### On the Windows FTP server

``` cmd
optionalfeatures
inetmgr
ipconfig
```

### On the FTP client

``` cmd
ftp 10.100.2.57
```

### At the `ftp>` prompt

``` text
dir
get text1.txt
put upload.txt
bye
```

## Troubleshooting

-   **Cannot connect:** Confirm the FTP site is started, the IP address
    is correct, and Windows Firewall permits FTP traffic.
-   **Login fails:** Check the IIS authentication and authorization
    settings.
-   **Download fails:** Check folder read permissions and confirm
    `text1.txt` exists in `C:\FTP\Shared`.
-   **Upload fails:** Check IIS write authorization and the Windows
    folder permissions for the FTP account.
-   **Connection works but listing or transfer hangs:** FTP may require
    appropriate passive-mode settings and firewall rules for the FTP
    data connection.

## Result

The IIS FTP site is configured, and FTP client commands are used to test
listing files, downloading `text1.txt`, and uploading `upload.txt`.
