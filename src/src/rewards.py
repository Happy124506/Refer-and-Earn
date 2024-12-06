def calculate_rewards(referral_count):
    if referral_count >= 5:
        return "₹500 Cashback"
    elif referral_count >= 3:
        return "₹200 Cashback"
    else:
        return "Keep Referring to Earn Rewards!"

# Example Usage
if __name__ == "__main__":
    print(calculate_rewards(4))  # Output: ₹200 Cashback
