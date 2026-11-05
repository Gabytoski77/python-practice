# Day 4 - Log triage with collections

failed_ips = ["10.0.0.5", "10.0.0.9", "10.0.0.5", "172.16.1.20", "10.0.0.5", "10.0.0.9"]
print(f"Total numbers of failed ips: {len(failed_ips)}")
print(f"First IP: {failed_ips[0]}")
print(f"Last IP: {failed_ips[-1]}")
failed_ips.append("192.168.50.7")
print(f"After new log entry: {len(failed_ips)}")
