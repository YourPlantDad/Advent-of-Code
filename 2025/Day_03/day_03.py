def calculateTotalJoltagesPart1(file_path: str) -> int:
    total_max_joltage = 0
    
    with open(file_path, 'r') as input_file:
        for bank_index, battery_bank in enumerate(input_file):
            cleaned_bank = battery_bank.strip()
            current_bank_max = 0
            
            for i in range(len(cleaned_bank) - 1):
                tens_digit = cleaned_bank[i]
                
                for j in range(i + 1, len(cleaned_bank)):
                    units_digit = cleaned_bank[j]
                    
                    joltage_value = int(tens_digit + units_digit)
                    
                    if joltage_value > current_bank_max:
                        current_bank_max = joltage_value
            
            total_max_joltage += current_bank_max
            
    print(f"Part 1 - Total Maximum Joltage: {total_max_joltage}")
    return total_max_joltage

def calculateTotalJoltagesPart2(file_path: str) -> int:
    total_output_joltage = 0
    target_length = 12
    
    with open(file_path, 'r') as input_file:
        for bank_index, battery_bank in enumerate(input_file):
            cleaned_bank = battery_bank.strip()
            
            if len(cleaned_bank) < target_length:
                continue

            current_result_str = ""
            search_start_index = 0
            
            for digits_collected in range(target_length):
                digits_needed_after = (target_length - 1) - digits_collected
                search_end_index = len(cleaned_bank) - digits_needed_after
                
                search_zone = cleaned_bank[search_start_index : search_end_index]
                
                max_digit = max(search_zone)
                relative_index = search_zone.index(max_digit)
                
                current_result_str += max_digit
                search_start_index = search_start_index + relative_index + 1
            
            bank_joltage = int(current_result_str)
            total_output_joltage += bank_joltage

    print(f"Part 2 - Total Output Joltage:  {total_output_joltage}")
    return total_output_joltage

# --- Execution Block ---

battery_bank_input = "input.txt"

print("--- Calculating Part 1 ---")
calculateTotalJoltagesPart1(battery_bank_input)

print("\n--- Calculating Part 2 ---")
calculateTotalJoltagesPart2(battery_bank_input)