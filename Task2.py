def main():
    # State Initialization (Outside the loop to preserve cumulative total)
    total_spent = 0.0

    print("========================================")
    print("   DecodeLabs - Expense Tracker (P2)    ")
    print("========================================")
    print("Enter expenses one by one.")
    print("Type 'quit' or 'exit' when you are finished.\n")

    while True:
        # Step 1: Input & Sentinel Check
        user_input = input("Enter expense amount: ").strip()

        # Sentinel Kill Switch
        if user_input.lower() in ['quit', 'exit']:
            print("\nShutting down continuous audit loop...")
            break

        # Step 2: Defensive Validation & Computation
        try:
            expense = float(user_input)

            if expense < 0:
                print("⚠️ Invalid entry: Expense amount cannot be negative.\n")
                continue

            # State update (Accumulator)
            total_spent += expense
            print(f"✓ Added: ${expense:.2f} | Running Total: ${total_spent:.2f}\n")

        except ValueError:
            print("❌ Invalid input: Please enter a valid number or type 'quit' to exit.\n")

    # Step 3: Final Output Stream
    print("========================================")
    print(f"FINAL TOTAL SPENT: ${total_spent:.2f}")
    print("========================================")

if __name__ == "__main__":
    main()