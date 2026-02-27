import re   # Used for pattern matching (regular expressions)


# -------------------------------------------------
# Function to check password strength
# -------------------------------------------------
def check_password(password: str) -> str:
    # Check minimum length (at least 8 characters)
    length_ok = len(password) >= 8
    
    # Using Walrus Operator (:=) for modern assignment inside expression
    has_upper = (upper := re.search(r"[A-Z]", password))
    has_lower = (lower := re.search(r"[a-z]", password))
    has_digit = (digit := re.search(r"[0-9]", password))
    has_special = (special := re.search(r"[!@#$%^&*()_+]", password))
    
    # Count satisfied conditions (True = 1, False = 0)
    score = sum(bool(x) for x in [length_ok, upper, lower, digit, special])
    
    # Structural Pattern Matching (Python 3.10+)
    match score:
        case 5:
            return "🟢 Strong"
        case 3 | 4 if length_ok:
            return "🟡 Moderate"
        case _:
            return "🔴 Weak"


# -------------------------------------------------
# Main Program Starts Here
# -------------------------------------------------
if __name__ == "__main__":
    print("\n" + "=" * 40)    # Print "=" 40 times 
    print(f"{'PASSWORD COMPLEXITY CHECKER':^40}")   # "^40" means center the text in 40 spaces.
    print("=" * 40)
    
    user_password: str = input("Enter your password: ")
    
    result = check_password(user_password)
    
    print(f"\nPassword Strength: {result}")
    print("=" * 40 + "\n")