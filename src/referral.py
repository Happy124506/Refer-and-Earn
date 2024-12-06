import random
import string

def generate_referral_code(username):
    code = username[:3].upper() + ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    return code

# Example Usage
if __name__ == "__main__":
    print(generate_referral_code("Rahul"))  # Output: RAH7DFT3
