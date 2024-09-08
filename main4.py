#ЗАВДАННЯ 4
#ДОРОБЛЕНИЙ БОТ З НОМЕРАМИ ТА ІНШИМ

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Please provide all necessary arguments."
        except KeyError:
            return "Contact not found."
        except Exception as e:
            return f"An unexpected error occurred: {e}"

    return inner


class ContactBot:
    def __init__(self):
        self.contacts = {}

    @input_error
    def add_contact(self, args):
        name, phone = args
        self.contacts[name] = phone
        return "Contact added."

    @input_error
    def phone(self, args):
        name = args[0]
        return f"{name}: {self.contacts[name]}"

    @input_error
    def show_all(self, args):
        if not self.contacts:
            return "No contacts available."
        return '\n'.join([f"{name}: {phone}" for name, phone in self.contacts.items()])

    def process_command(self, command):
        parts = command.split()
        if not parts:
            return "Enter a command."
        
        command = parts[0]
        args = parts[1:]

        if command == "add":
            return self.add_contact(args)
        elif command == "phone":
            return self.phone(args)
        elif command == "all":
            return self.show_all(args)
        else:
            return "Unknown command."

def main():
    bot = ContactBot()
    while True:
        command = input("Enter a command: ")
        response = bot.process_command(command)
        print(response)

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) < 2:
        return "Invalid command. Please provide a name and a phone number."
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    if len(args) < 2:
        return "Invalid command. Please provide a name and a new phone number."
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(args, contacts):
    if len(args) < 1:
        return "Invalid command. Please provide a name."
    name = args[0]
    return contacts.get(name, "Contact not found.")

def show_all(contacts):
    if not contacts:
        return "No contacts found."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

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

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Please provide all necessary arguments."
        except KeyError:
            return "Contact not found."
        except Exception as e:
            return f"An unexpected error occurred: {e}"

    return inner



if __name__ == "__main__":
    main()