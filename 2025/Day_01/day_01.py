def getDialMovements(file):
    DIAL_RANGE = 100 
    current_dial_position = 50
    landed_on_zero = 0
    
    with open(file, 'r') as f: 
        print(f"Startposition {current_dial_position}\n")
        
        for line in f:

            cleaned_line = line.strip()

            if cleaned_line:
                direction_char = cleaned_line[0]
                steps_str = cleaned_line[1:]

                steps = int(steps_str)

                amount = 0
                
                if direction_char == 'L':
                    amount = -steps
                elif direction_char == 'R':
                    amount = steps 
                    
                new_position_raw = current_dial_position + amount
                
                current_dial_position = new_position_raw % DIAL_RANGE
                
                if current_dial_position == 0:
                    landed_on_zero += 1

                print(f"File text: {cleaned_line:<4} | Dial turn amount: {amount:>+3} | New dial position: {current_dial_position}")
                    
    return current_dial_position, landed_on_zero

eindpositie, zero_passes = getDialMovements("input.txt")
print(f"\nThe dial has landed on zero exactly {zero_passes} times.\n")