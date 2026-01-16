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
        
        # Step 3: Ask for desired pitch shift and validate
        while True:
            try:
                # Ask for pitch shift (allows decimals and negatives)
                pitch_input = input("\nEnter the desired pitch shift (in semitones, e.g., +2 or -1): ")
                desired_pitch_shift = float(pitch_input)
                
                # If successful, exit the validation loop
                break
            except ValueError:
                # Triggers if the user enters non-numeric text
                print(f"'{pitch_input}' is not a valid number. Please enter a numeric pitch shift.")

        # Step 4: Musical Tempo Calculation
        # Result = Original Tempo * 2^(Semitones / 12)
        new_tempo = initial_tempo * (2 ** (desired_pitch_shift / 12))

        print(f"\n>>> RECOMMENDED PRO-TOOLS TEMPO: {new_tempo:.3f} BPM")
                

        # Step 5: Restart or Exit logic
        choice = input("\nPress Enter to run again, or 'z' to exit: ").strip().lower()
        if choice == 'z':
            print("Happy Vocal Layering!")
            break

if __name__ == "__main__":
    main()