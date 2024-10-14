import re
import argparse


def parse_logs(file_path):
    logs = []
    with open(file_path, 'r') as file:
        for line in file:
            logs.append(line.strip())
    return logs

def detect_failed_logins(logs):
    failed_logins = []
    pattern = re.compile(r'Failed password for .* from (\d+\.\d+\.\d+\.\d+)')

    for log in logs:
        match = pattern.search(log)
        if match:
            failed_logins.append(log)

    return failed_logins

def detect_time_sync_issues(logs):
    time_sync_issues = []
    pattern = re.compile(r'Timed out waiting for reply from .* \(ntp\.ubuntu\.com\)')

    for log in logs:
        match = pattern.search(log)
        if match:
            time_sync_issues.append(log)

    return time_sync_issues

def detect_service_restarts(logs):
    restarts = []
    pattern = re.compile(r'started|Starting')

    for log in logs:
        match = pattern.search(log, re.IGNORECASE)
        if match:
            restarts.append(log)

    return restarts

def analyse_logs(file_path):
    logs = parse_logs(file_path)

    failed_logins = detect_failed_logins(logs)
    if failed_logins:
        print("Failed login attempts detected:")
        for log in failed_logins:
            print(log)
    else:
        print("No failed login attempts detected.")

    time_sync_issues = detect_time_sync_issues(logs)
    if time_sync_issues:
        print("\nTime synchronization issues detected:")
        for log in time_sync_issues:
            print(log)
    else:
        print("No time synchronization issues detected.")

    service_restarts = detect_service_restarts(logs)
    if service_restarts:
        print("\nService restarts or system events detected:")
        for log in service_restarts:
            print(log)
    else:
        print("No service restarts detected.")

def main():
    parser = argparse.ArgumentParser(description="Log Analysis Tool")
    parser.add_argument("-f", "--file", required=True, help="Path to the log file")
    
    # Parse arguments
    args = parser.parse_args()

    # Run the analysis
    analyse_logs(args.file)

if __name__ == "__main__":
    main()
