import re

# The exact regex pattern from the model answer
EMAIL_PATTERN = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+'

def find_emails(text):
    # Scans the entire text and returns a list of all matching emails
    return re.findall(EMAIL_PATTERN, text)

def is_valid_email(candidate):
    # Checks if the entire string matches the email pattern
    if re.fullmatch(EMAIL_PATTERN, candidate):
        return True
    else:
        return False

# --- Part 1: Finding emails in a block of text ---
sample_text = """
Hello, please send the reports to admin@school.edu and copy 
teacher.name@department-123.com. 
Invalid ones like just-a-name or missing@domain won't work.
"""

print("--- Extracting Emails ---")
extracted = find_emails(sample_text)
print(f"Found {len(extracted)} email(s):")
for email in extracted:
    print(f"- {email}")

# --- Part 2: Validating individual email addresses ---
print("\n--- Validating Test Cases ---")

# A mix of valid, invalid, and tricky test cases
test_cases = [
    "student_2023@university.edu",  # Valid
    "broken-email.com",             # Invalid (no @)
    "@missing-local.org",           # Invalid (no local part)
    "numbers@12345.com"             # Valid (tricky number domain)
]

for test in test_cases:
    if is_valid_email(test):
        print(f"VALID   -> {test}")
    else:
        print(f"INVALID -> {test}")
