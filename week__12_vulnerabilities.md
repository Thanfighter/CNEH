# WEEK 12: Finding Website Security Vulnerabilities

**Practical Experiment**

## 1. Aim

To identify potential security weaknesses in a website using Mozilla HTTP Observatory by analyzing its HTTP security headers and configuration.

## 2. Tool Required

- Mozilla HTTP Observatory
- Internet connection
- Web browser

**Website:** https://developer.mozilla.org/en-US/observatory

## 3. Introduction

Mozilla HTTP Observatory is an online website security assessment tool that analyzes HTTP security headers and related website configurations.

It evaluates the security configuration of a website and provides a security score, grade, and recommendations for improving its security.

## 4. Procedure

1. Open a web browser.
2. Visit https://developer.mozilla.org/en-US/observatory.
3. Enter the domain name of the website you want to test.
4. Start the security scan.
5. Wait for the scan to complete.
6. Observe the security score and grade.
7. Check the test results for failed checks and warnings.
8. Review the recommendations provided by the tool.
9. Record the results and capture screenshots.

**Note:** Test only websites that you own or have permission to assess.

## 5. Security Checks

The tool examines various HTTP security headers and configurations.

| Security Header | Purpose |
|---|---|
| Content-Security-Policy (CSP) | Helps prevent cross-site scripting attacks. |
| Strict-Transport-Security (HSTS) | Enforces secure HTTPS connections. |
| X-Content-Type-Options | Prevents MIME-type sniffing. |
| Referrer-Policy | Controls referrer information shared with other websites. |
| Permissions-Policy | Controls access to browser features. |
| Secure Cookie Settings | Helps protect cookies from unauthorized access and transmission. |

## 6. Observation

Record the results obtained after scanning the website.

| Observation | Result |
|---|---|
| Website Name | |
| Date of Scan | |
| Security Score | |
| Security Grade | |
| Failed Checks | |
| Warnings | |
| Recommended Improvements | |

## 7. Screenshots for Lab Record

Capture the following screenshots:

1. Mozilla HTTP Observatory homepage.
2. Website domain entered for scanning.
3. Security scan results showing the score and grade.
4. Detailed security checks and recommendations.

## 8. Precautions

1. Enter the correct website domain.
2. Test only authorized websites.
3. Review all failed checks and warnings carefully.
4. A high security score does not guarantee complete website security.
5. The tool checks specific security configurations and is not a complete vulnerability scanner.

## 9. Result

The website was successfully assessed using Mozilla HTTP Observatory. Its HTTP security headers and related configurations were analyzed, and the tool provided a security score, grade, and recommendations for improving website security.

## Reference

- Mozilla HTTP Observatory: https://developer.mozilla.org/en-US/observatory
