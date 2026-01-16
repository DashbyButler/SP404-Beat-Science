def print_splash():
    """Prints an ASCII drum machine splash screen."""
    # Use raw string (r"") to handle backslashes correctly in 2026
    drum_machine = r"""
    ___________________________________
    | [ Beat Science Calculator ]     |
    |_________________________________|
    | [O] [O] [O] [O] |  [120.000 BPM]|
    | [O] [O] [O] [O] |  [+0.0 SEMI ] |
    |_________________|_______________|
    | [PAD 1] [PAD 2] [PAD 3] [PAD 4] |
    | [PAD 5] [PAD 6] [PAD 7] [PAD 8] |
    |_________________________________|
    """
    print(drum_machine)
    print("Welcome to the Beat Science Calculator.")



def main():
    print_splash()
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