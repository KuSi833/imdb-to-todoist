VALID_TRUE = ["y", "yes"]
VALID_FALSE = ["n", "no"]


def parse_bool(message: str, default_value=True) -> bool:
    print(message)
    valid_true, valid_false = VALID_TRUE, VALID_FALSE
    if default_value is True:
        example_input = "[y]/n"
        valid_true.append("")
    else:
        example_input = "y/[n]"
        valid_false.append("")

    while True:
        ans = input(f"{example_input}: ").lower()
        if ans in valid_true:
            return True
        elif ans in valid_false:
            return False
        else:
            print("Invalid entry, try again.")
