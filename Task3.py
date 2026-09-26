import math
import secrets
import string

def calculate_entropy(length: int, pool_size: int) -> float:
    """Calculates password entropy in bits: E = L * log2(R)."""
    if pool_size <= 0 or length <= 0:
        return 0.0
    return length * math.log2(pool_size)

def generate_password(length: int, include_digits: bool = True, include_symbols: bool = True) -> tuple[str, float]:
    """
    Generates a cryptographically secure random password and returns 
    the password along with its entropy value.
    """
    # 1. Build Character Pool using standard library string classifications
    char_pool = string.ascii_letters
    if include_digits:
        char_pool += string.digits
    if include_symbols:
        char_pool += string.punctuation

    # 2. Cryptographically Secure Selection Engine (O(N) memory allocation)
    # Using secrets.choice for cryptographic randomness + list join for linear speed
    password_chars = [secrets.choice(char_pool) for _ in range(length)]
    password = "".join(password_chars)

    # 3. Calculate Information Entropy
    entropy = calculate_entropy(length, len(char_pool))

    return password, entropy

def main():
    print("==================================================")
    print("  DecodeLabs - Enterprise Password Generator (P3) ")
    print("==================================================")
    print("NIST SP 800-63-4 Standard: 15+ characters recommended.\n")

    # Phase 1: Input & Environmental Validation
    while True:
        try:
            raw_input = input("Enter desired password length (e.g., 16): ").strip()
            length = int(raw_input)

            if length < 8:
                print("⚠️  Security Warning: Lengths below 8 characters are extremely vulnerable.")
                confirm = input("Are you sure you want to proceed? (y/n): ").strip().lower()
                if confirm != 'y':
                    continue
            break
        except ValueError:
            print("❌ Invalid input: Please enter a valid integer for length.\n")

    # Phase 2 & 3: Generation & Entropy Mathematical Provision
    password, entropy = generate_password(length)

    print("\n---------------- GENERATED CREDENTIAL ----------------")
    print(f"Password: {password}")
    print(f"Entropy : {entropy:.2f} bits")
    
    # Entropy Strength Classification
    if entropy < 50:
        print("Strength: WEAK 🔴 (Vulnerable to modern GPU brute-force)")
    elif entropy < 80:
        print("Strength: MODERATE 🟡 (Acceptable for standard user accounts)")
    else:
        print("Strength: STRONG 🟢 (Cryptographically resilient)")
    print("------------------------------------------------------\n")

if __name__ == "__main__":
    main()