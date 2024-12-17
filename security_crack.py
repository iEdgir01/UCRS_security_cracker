# Dice pairs mapping
DICE_PAIRS = {1: 6, 2: 5, 3: 4, 6: 1, 5: 2, 4: 3}

def get_dice_inverse():
    print("Enter a dice number (1-6), and I'll provide its inverse:")
    while True:
        try:
            dice = int(input("Enter dice number: ").strip())
            if dice in DICE_PAIRS:
                print(f"The inverse of {dice} is {DICE_PAIRS[dice]}\n")
                return
            else:
                print("Invalid input. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid number (1-6).")

def get_icons():
    print("\nEnter each icon's attributes in one line using the format '(#EYES)(HEAD DIRECTION - L/M/R)(#LEGS)' (e.g., '1L4' or '2M3').")
    print("Type all three icons, pressing Enter after each. Then press Enter on an empty line to finish.")
    
    icons = []
    for i in range(1, 4):
        while True:
            input_str = input(f"Icon {i}: ").strip().upper()
            if input_str == "":
                print("Invalid format. Please enter the icon as 'eyes-direction-legs' (e.g., '1L4').")
                continue
            if len(input_str) != 3:
                print("Invalid format. Please enter the icon as 'eyes-direction-legs' (e.g., '1L4').")
                continue
            try:
                eyes = int(input_str[0])  # Number of eyes
                direction = input_str[1]  # Head direction (L, M, R)
                legs = int(input_str[2])  # Number of legs
                if direction not in "LMR":
                    raise ValueError
                icons.append((eyes, direction, legs, i))  # Append icon with its index
                break  # Break after valid icon
            except (IndexError, ValueError):
                print("Invalid format. Please enter the icon as 'eyes-direction-legs' (e.g., '1L4').")
    
    return icons

def sort_icons(icons):
    # Sorting rules
    return sorted(
        icons,
        key=lambda icon: (
            icon[0],  # Number of eyes (low to high)
            {"L": 0, "M": 1, "R": 2}[icon[1]],  # Head direction (L < M < R)
            icon[2]   # Number of legs (low to high)
        )
    )

def main():
    try:
        while True:
            # Step 1: Get dice inverse
            get_dice_inverse()

            # Step 2: Get icons
            icons = get_icons()

            # Step 3: Sort icons
            sorted_icons = sort_icons(icons)

            # Step 4: Output the sequence
            sequence = [icon[3] for icon in sorted_icons]  # Extract the original icon numbers
            print(f"\nThe correct sequence is: {', '.join(map(str, sequence))}")

    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Exiting...")

if __name__ == "__main__":
    main()