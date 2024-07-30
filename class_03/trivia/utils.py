def get_int_input_in_range(
    min_value: int, max_value: int, prompt: str = "Please select an option: "
):
    bad_input_msg = f"Bad input. Please provide a number in range [{min_value}, {max_value}]"
    
    while True:
        raw_input = input(prompt)
        if not raw_input.isdigit():
            print(bad_input_msg)
            continue
        input_number = int(raw_input)

        if input_number < min_value or input_number > max_value:
            print(bad_input_msg)
            continue

        return input_number


def clean_empty_keys_from_dict(mapping: dict[str, list]):
    keys = list(mapping.keys())

    for key in keys:
        if len(mapping[key]) == 0:
            del mapping[key]