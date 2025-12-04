def is_invalid_id_part2(product_id: int) -> bool:
    id_string = str(product_id)
    total_length = len(id_string)

    for pattern_length in range(1, total_length):
        
        if total_length % pattern_length == 0:
            
            pattern_segment = id_string[:pattern_length]
            
            number_of_repeats = total_length // pattern_length
            
            reconstructed_id = pattern_segment * number_of_repeats
            
            if reconstructed_id == id_string:
                return True
                
    return False

def gift_shop_part1(file_path: str) -> int:
    total_invalid_ids_sum_part1 = 0
    
    with open(file_path, 'r') as f:
        data_line = f.read().strip()
    
    ranges = data_line.split(',')
    
    for range_str in ranges:
        if not range_str.strip():
            continue
        
        start_str, end_str = range_str.split('-')
        start_id = int(start_str.strip())
        end_id = int(end_str.strip())
            
        for current_id in range(start_id, end_id + 1):

            id_str = str(current_id)
            n = len(id_str)
            
            if n % 2 == 0:
                half_length = n // 2
                first_half = id_str[:half_length]
                second_half = id_str[half_length:]

                if first_half == second_half:
                    total_invalid_ids_sum_part1 += current_id
                    
    return total_invalid_ids_sum_part1

def gift_shop_part2(file_path: str) -> int:
    total_sum_of_invalid_ids = 0
    
    with open(file_path, 'r') as file:
        data_line = file.read().strip()

    range_strings = data_line.split(',')
    
    for range_str in range_strings:
        if not range_str.strip():
            continue
        
        start_str, end_str = range_str.split('-')
        start_id = int(start_str.strip())
        end_id = int(end_str.strip())
            
        for current_id in range(start_id, end_id + 1):
            
            if is_invalid_id_part2(current_id):
                total_sum_of_invalid_ids += current_id
                
    return total_sum_of_invalid_ids

input_file = "input.txt"

final_sum_part1 = gift_shop_part1(input_file)
final_sum_part2 = gift_shop_part2(input_file)
    
print("\n****************************************")
print(f"* DAY 2 - GIFT SHOP RESULTS            *")
print("****************************************")
print(f"* Part 1 Sum of Invalid IDs: {final_sum_part1} *")
print(f"* Part 2 Sum of Invalid IDs: {final_sum_part2} *")
print("****************************************")