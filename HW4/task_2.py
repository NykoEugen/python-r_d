sample_text = input("Input some text or args: ")
match sample_text:
    case s if s.isnumeric():
        print("It's integer")
    case s if len(sample_text) > 0:
        print("It's string")
    case s if len(sample_text) <= 0:
        print("Empty")
