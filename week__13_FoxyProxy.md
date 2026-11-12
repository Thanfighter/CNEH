# WEEK 13: Intercepting Web Traffic Using Burp Suite and FoxyProxy

**Practical Experiment**

## 1. Aim

To intercept and analyze HTTP/HTTPS web traffic using Burp Suite by configuring FoxyProxy in Mozilla Firefox.

## 2. Tools Required

1. Mozilla Firefox browser.
2. FoxyProxy Standard extension.
3. Burp Suite.
4. Internet connection.

## 3. Introduction

Burp Suite is a web application security testing tool used to intercept, inspect, and analyze HTTP/HTTPS requests and responses between a browser and a web server.

FoxyProxy is a browser extension that allows users to configure and switch between proxy servers easily.

In this experiment, Firefox is configured to route its web traffic through Burp Suite using a local proxy address.

## 4. Procedure

### Step 1: Install FoxyProxy

1. Open Mozilla Firefox.
2. Visit the Firefox Add-ons website.
3. Search for **FoxyProxy Standard**.
4. Click Add to Firefox.
5. Complete the installation.

### Step 2: Configure FoxyProxy

1. Click the FoxyProxy icon in Firefox.
2. Open its options or proxy settings.
3. Add a new proxy configuration.
4. Enter the following details:

| Field | Value |
|---|---|
| Title | Burp Suite |
| Hostname | `127.0.0.1` |
| Port | `8080` |

5. Click Save.

### Step 3: Configure Burp Suite

1. Open Burp Suite.
2. Navigate to Settings → Proxy.
3. Find the Proxy Listeners section.
4. Select the existing proxy listener and click Edit.
5. Change the specific address to:

   `127.0.0.1`

6. Keep the port as `8080`.
7. Click OK.

### Step 4: Connect Firefox to Burp Suite

1. Return to Mozilla Firefox.
2. Click the FoxyProxy icon.
3. Select the **Burp Suite** proxy configuration.
4. Firefox will now route its web traffic through Burp Suite.

### Step 5: Enable Interception

1. Open Burp Suite.
2. Navigate to Proxy → Intercept.
3. Switch on interception by clicking **Intercept is off**.
4. It should now display **Intercept is on**.

### Step 6: Intercept Web Traffic

1. Open Firefox with the Burp Suite proxy enabled.
2. Visit Google or another website.
3. Observe the HTTP/HTTPS requests appearing in Burp Suite.
4. Inspect the intercepted requests and responses.
5. Use Forward to allow an intercepted request to continue to the destination server.

**Note:** HTTPS traffic inspection requires Burp Suite's CA certificate to be installed and trusted in Firefox. Without it, HTTPS connections may show certificate warnings or fail to load.

## 5. Observation

| Parameter | Configuration |
|---|---|
| Browser | Mozilla Firefox |
| Proxy Extension | FoxyProxy Standard |
| Proxy Tool | Burp Suite |
| Proxy Host | `127.0.0.1` |
| Proxy Port | `8080` |
| Interception Status | Enabled |

## 6. Screenshots for Lab Record

Capture the following screenshots:

1. FoxyProxy Standard installed in Firefox.
2. FoxyProxy configuration showing hostname and port.
3. Burp Suite proxy listener configuration.
4. Burp Suite showing interception enabled.
5. Intercepted HTTP/HTTPS traffic in Burp Suite.

## 7. Precautions

1. Verify that Burp Suite is running before enabling the proxy in Firefox.
2. Ensure that the hostname and port are configured correctly.
3. Use only websites and applications you own or have permission to test.
4. Do not intercept or inspect other people's private traffic.
5. Disable the proxy in FoxyProxy after completing the experiment.
6. Use Burp Suite's CA certificate only in a controlled lab environment.

## 8. Result

Successfully configured FoxyProxy in Mozilla Firefox and connected it to Burp Suite using the local proxy address `127.0.0.1:8080`. Web traffic was successfully intercepted and inspected using Burp Suite.

## Reference

- Burp Suite: https://portswigger.net/burp
- FoxyProxy: https://getfoxyproxy.org/
