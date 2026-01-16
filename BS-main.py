def main():
    # Application remains active until user chooses to exit
    while True:
        # Step 2: Ask for initial tempo and validate
        while True:
            try:
                # Ask for tempo (allows decimals)
                tempo_input = input("\nEnter the initial tempo (BPM): ")
                initial_tempo = float(tempo_input)
                
                # Ensure tempo is a positive value
                if initial_tempo <= 0:
                    print("Tempo must be a positive number. Please try again.")
                    continue
                
                # If successful, exit the validation loop
                break
            except ValueError:
                # Triggers if the user enters non-numeric text
                print(f"'{tempo_input}' is not a valid number. Please enter a numeric BPM.")

        # For now, just confirming the input
        print(f"Starting calculation with: {initial_tempo} BPM")

        # Step 5: Restart or Exit logic
        choice = input("\nPress Enter to run again, or 'z' to exit: ").strip().lower()
        if choice == 'z':
            print("Exiting Beat Science Calculator. Goodbye!")
            break

if __name__ == "__main__":
    main()