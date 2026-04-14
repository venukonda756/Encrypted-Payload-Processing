# in_built_functions_in_python

raw_data = "   GhostAdmin | 7 | failed_login  "
clean_playload=raw_data.strip()
parts=clean_playload.split(" | ")
print(parts)

username=parts[0]
sector_id=parts[1]
status=parts[2]

if username.isalnum():
    print(f"ALERT user {username} {status} in sector {sector_id}")
else:
    print("LOCKDOWN INITIALIZED: Invalid characters detected.")
