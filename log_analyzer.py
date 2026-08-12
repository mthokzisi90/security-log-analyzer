from collections import Counter

LOG_FILE = "sample_auth.log"


def analyze_log(filename):
    failed_logins = []
    successful_logins = []

    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split()

            if len(parts) < 4:
                continue

            timestamp = f"{parts[0]} {parts[1]}"
            event = parts[2]
            user = parts[3].split("=")[1]
            ip_address = parts[4].split("=")[1]

            if event == "FAILED_LOGIN":
                failed_logins.append((timestamp, user, ip_address))

            elif event == "SUCCESS_LOGIN":
                successful_logins.append((timestamp, user, ip_address))

    return failed_logins, successful_logins


failed, successful = analyze_log(LOG_FILE)

print("=== Security Log Analysis ===")
print(f"Total failed logins: {len(failed)}")
print(f"Total successful logins: {len(successful)}")

print("\nFailed login attempts:")

for timestamp, user, ip in failed:
    print(f"{timestamp} | User: {user} | IP: {ip}")

ip_counts = Counter(ip for _, _, ip in failed)

print("\nPotentially suspicious IP addresses:")

for ip, count in ip_counts.items():
    if count >= 3:
        print(f"{ip} - {count} failed login attempts")
