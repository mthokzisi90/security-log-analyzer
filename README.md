# 🔎 Security Log Analyzer

## 📌 Overview

This project is a beginner-friendly Python security log analyzer that examines a fictional authentication log and identifies repeated failed login attempts.

The project was created as part of my cybersecurity learning journey to practice **Python, log analysis, authentication monitoring, and security investigation concepts**.

## 🎯 Project Objectives

The program is designed to:

- Read an authentication log
- Identify successful login events
- Identify failed login events
- Count failed login attempts
- Group failed attempts by IP address
- Identify IP addresses with repeated failed login attempts
- Flag potentially suspicious authentication activity for further investigation

## 🐍 Technologies Used

- Python 3
- Python `collections` module
- File handling
- Lists
- Loops
- Functions
- Conditional statements
- String manipulation

## 📂 Project Structure

```text
security-log-analyzer
│
├── README.md
├── sample_auth.log
├── log_analyzer.py
├── log analyzer screenshot.png
├── log analyzer screenshot 2.png
└── log analyzer screenshot 3.png
```

## ▶️ How to Run

### Requirements

- Python 3.x
- No external Python packages are required.

### Steps

1. Clone the repository:

```bash
git clone https://github.com/mthokzisi90/security-log-analyzer.git
```

2. Navigate into the project directory:

```bash
cd security-log-analyzer
```

3. Run the analyzer:

```bash
python log_analyzer.py
```

The program will process the `sample_auth.log` file and display the authentication analysis results.

## 📄 Project Files

### `sample_auth.log`

A fictional authentication log created specifically for this educational project.

The log contains authentication events that can be analyzed for repeated failed login attempts.

### `log_analyzer.py`

The Python program that reads the authentication log, processes authentication events, counts failed attempts, and identifies potentially suspicious IP addresses.

## 🔐 How the Analysis Works

The program reads each line of the authentication log and extracts information such as:

- Timestamp
- Event type
- Username
- IP address

It separates authentication events into:

- `FAILED_LOGIN`
- `SUCCESS_LOGIN`

The program then counts failed login attempts associated with each IP address.

## 🚨 Detection Threshold

The current detection rule flags an IP address when it has **three or more failed login attempts**.

This threshold is used for demonstration purposes and does not represent a production security detection rule.

In a real security environment, detection thresholds would depend on factors such as:

- User behavior
- Authentication policies
- Time intervals
- Geographic location
- Account sensitivity
- Previous security incidents
- Other security telemetry

## 💻 Example Analysis

The analyzer was tested against the fictional `sample_auth.log` file.

The program identified repeated failed login attempts associated with:

**IP address:** `192.168.1.10`

The IP address was flagged because it reached the configured threshold of three or more failed login attempts.

This demonstrates how Python can be used to automatically identify authentication patterns that may require further investigation.

## 🔎 Security Finding

The analysis identified multiple failed authentication attempts originating from:

**`192.168.1.10`**

The repeated authentication failures caused the IP address to be flagged by the analyzer.

### Analyst Interpretation

The activity could have several possible explanations, including:

- Incorrect or forgotten credentials
- A user experiencing authentication problems
- Automated login attempts
- Password-guessing activity
- A possible brute-force attempt

However, the activity should **not automatically be classified as malicious** based only on these log entries.

A real security analyst would investigate additional information, including:

- Whether the IP address belongs to an authorized user
- The affected account
- The timing and frequency of the attempts
- Whether successful authentication occurred afterward
- Other events occurring around the same time
- Network and system logs
- Additional security monitoring data

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
- Basic incident investigation

## 📸 Project Screenshots

### Security Log Analyzer Output

![Security Log Analyzer Output](log%20analyzer%20screenshot.png)

### Log Analysis Results

![Log Analysis Results](log%20analyzer%20screenshot%202.png)

### Additional Analysis

![Additional Analysis](log%20analyzer%20screenshot%203.png)

## 🚀 Future Improvements

Possible improvements for future versions include:

- Add command-line arguments for different log files
- Detect failed login attempts within a specific time window
- Export analysis results to CSV
- Add username-based analysis
- Detect successful logins following multiple failures
- Add severity levels
- Generate automated security reports
- Integrate the analyzer with larger security datasets
- Add unit tests
- Improve error handling

## 🎓 Learning Outcome

This project strengthened my practical understanding of **Python programming, authentication monitoring, security log analysis, suspicious activity detection, and evidence-based security investigation**.

It also provided hands-on experience applying cybersecurity concepts to a practical log-analysis scenario.

## 👤 Author

**Mthokozisi Khulu**

GitHub: [@mthokzisi90](https://github.com/mthokzisi90)

⭐ Part of my ongoing journey into **IT Support and Cybersecurity**.
