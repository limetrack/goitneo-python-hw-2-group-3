def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Invalid value. Please enter correct information."
        except IndexError:
            return "Invalid number of arguments."
        except Exception as e:
            return f"Unexpected error: {e}"
    return inner

@input_error
def add_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Invalid number of arguments.")
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args) != 2:
        raise ValueError("Invalid number of arguments.")
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        raise KeyError("Contact not found.")

@input_error
def show_phone(args, contacts):
    if len(args) != 1:
        raise ValueError("Invalid number of arguments.")
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        raise KeyError("Contact not found.")

def show_all(contacts):
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def parse_input(user_input):
    parts = user_input.split()
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
