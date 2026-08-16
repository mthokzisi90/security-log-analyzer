# 🔎 Security Log Analyzer

## 📌 Overview

This project is a beginner-friendly Python security log analyzer that examines a fictional authentication log and identifies repeated failed login attempts.

The project was created as part of my cybersecurity learning journey to practice **Python, log analysis, and security investigation concepts**.

## 🎯 Project Objectives

The program is designed to:

* Read an authentication log
* Identify successful login events
* Identify failed login events
* Count failed login attempts
* Group failed attempts by IP address
* Highlight IP addresses with repeated failed login attempts

## 🐍 Technologies Used

* Python 3
* Python `collections` module
* File handling
* Lists
* Loops
* Functions
* Conditional statements
* String manipulation

## 📂 Project Structure

```text
security-log-analyzer
│
├── README.md
├── sample_auth.log
└── log_analyzer.py
```
## ▶️ How to Run

### Requirements

- Python 3.x
- No external Python packages are required.

### Steps

1. Clone the repository:

```bash
git clone https://github.com/mthokzisi90/security-log-analyzer.git
### `sample_auth.log`

A fictional authentication log created specifically for this educational project.

### `log_analyzer.py`

The Python program that reads the log, processes authentication events, counts failed attempts, and identifies potentially suspicious IP addresses.

## 🔐 How the Analysis Works

The program reads each line of the log and extracts:

* Timestamp
* Event type
* Username
* IP address

It separates events into:

* `FAILED_LOGIN`
* `SUCCESS_LOGIN`

It then counts failed login attempts associated with each IP address.

The program currently flags an IP address when it has **three or more failed login attempts**.

## 💻 Example Analysis

The analyzer was tested against the fictional `sample_auth.log` file.

The program identified repeated failed login attempts associated with:

**IP address:** `192.168.1.10`

The IP address was flagged because it reached the threshold of three or more failed login attempts.

This demonstrates how Python can be used to automatically identify authentication patterns that may require further investigation.

## 🔎 Analysis Finding

After running the Python analyzer against the fictional authentication log, the program identified repeated failed login attempts associated with:

**IP address:** `192.168.1.10`

The IP address generated multiple failed authentication attempts and was therefore flagged by the program for further investigation.

### Analyst Interpretation

The repeated failed attempts may indicate:

* Incorrect or forgotten credentials
* A user experiencing authentication problems
* Automated login attempts
* Password-guessing activity
* A possible brute-force attempt

However, the activity should **not** automatically be classified as malicious based only on these log entries.

A real security analyst would investigate additional information, such as:

* Whether the IP address belongs to an authorized user
* The affected account
* The time pattern of the attempts
* Other events occurring around the same time
* Network and system logs
* Whether successful authentication occurred after the failed attempts

## 🛡️ Security Concepts Demonstrated

This project demonstrates practical understanding of:

- Authentication monitoring
- Failed login detection
- Security log analysis
- IP address analysis
- Suspicious activity identification
- Evidence-based investigation
- Python automation
- Security monitoring

### Conclusion

The analysis successfully demonstrated how Python can be used to process authentication logs and identify patterns that may require further security investigation.

This project strengthened my practical understanding of **log analysis, authentication monitoring, Python automation, and security investigation**.


---

**Author:** Mthokozisi Khulu
**GitHub:** [@mthokzisi90](https://github.com/mthokzisi90)

⭐ Part of my ongoing journey into IT Support and Cybersecurity.


