import numpy as np

# Step 1: Generate OTP
otp = np.random.randint(100000, 1000000)  # 6-digit OTP
print("OTP sent to user (for simulation):", otp)  # in real app, send via SMS/email

# Step 2: Ask user to input OTP
user_input = int(input("Enter the OTP: "))

# Step 3: Verify
if user_input == otp:
    print("OTP verified! Access granted.")
    # Simulate file access
    with open('sm.txt', "w") as f:
        f.write("You have accessed the secret file!")
    print("File accessed successfully!")
else:
    print("Incorrect OTP! Access denied.")
