import pandas as pd

df = pd.read_csv("logins.csv")

print("=== LOGIN SECURITY REPORT ===\n")
print("Total logins:", len(df))
print("\nStatus breakdown:")
print(df["status"].value_counts())

print("\nFailed logins by IP (potential attackers):")
print(df[df["status"] == "failed"]["ip"].value_counts())

print("\nMost targeted usernames:")
print(df[df["status"] == "failed"]["username"].value_counts())