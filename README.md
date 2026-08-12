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

## 🔎 Example Finding

The sample log contains repeated failed login attempts from:

```text
192.168.1.10
```

The program identifies this IP address as potentially suspicious because it generates multiple failed authentication attempts.

This does **not** automatically mean that the activity is malicious. In a real security investigation, an analyst would examine additional information and context before determining whether the activity represents an attack.

## 🛡️ Cybersecurity Relevance

Authentication logs can provide useful information when investigating suspicious activity.

Repeated failed login attempts may indicate situations such as:

* Incorrect passwords
* User account problems
* Forgotten credentials
* Automated login attempts
* Password-guessing activity
* Brute-force attempts

Security analysts should investigate the surrounding context before making a conclusion.

## 📚 What I Learned

Through this project, I practiced:

* Reading files with Python
* Processing information line by line
* Splitting strings into useful data
* Using lists to store information
* Creating and using functions
* Using conditional statements
* Counting repeated events
* Identifying potentially suspicious patterns
* Connecting Python programming with cybersecurity analysis

## 🚀 Future Improvements

I plan to improve this project by adding:

* Detection of repeated failed attempts within a specific time period
* Username-based analysis
* More detailed event classification
* Automatic security alerts
* CSV report generation
* Visualization of authentication activity
* Detection of additional suspicious patterns

## ⚠️ Security Note

The log file included in this repository contains **fictional data created for educational purposes**.

No real authentication logs, credentials, passwords, or sensitive information are included.

---

**Author:** Mthokozisi Khulu
**GitHub:** [@mthokozisi90](https://github.com/mthokozisi90)

⭐ Part of my ongoing journey into IT Support and Cybersecurity.

