# Log_analyser
This is a tool to parse and analyse logs in and then generate a report on the findings.

To run this tool use the command "python3 log_analysis.py --file /path/to/syslog".

An example of results shows:
![image](https://github.com/user-attachments/assets/b4485e4a-bc81-4a1c-b9d5-58ecc40d27fc)

What This Script Does:

* Detect Failed Logins: It looks for lines matching a failed login pattern, though your current syslog doesn't seem to include such entries. This feature is kept in case other logs have this information (e.g., SSH login failures).
* Detect Time Synchronization Issues: It looks for lines like Timed out waiting for reply from ntp.ubuntu.com, which are in your provided logs, and reports them.
* Detect Service Restarts: It detects system services starting or restarting by matching words like "Starting" or "started."



