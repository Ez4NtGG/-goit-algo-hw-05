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
    def change_contact(self, args):
        name, new_phone = args
        if name in self.contacts:
            self.contacts[name] = new_phone
            return "Contact updated."
        else:
            return "Contact not found."

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
        
        cmd = parts[0].lower()
        args = parts[1:]

        if cmd == "add":
            return self.add_contact(args)
        elif cmd == "change":
            return self.change_contact(args)
        elif cmd == "phone":
            return self.phone(args)
        elif cmd == "all":
            return self.show_all(args)
        else:
            return "Unknown command."


def main():
    bot = ContactBot()
    print("Welcome to the assistant bot!")
    while True:
        command = input("Enter a command: ")
        if command.lower() in ["exit", "close"]:
            print("Good bye!")
            break
        response = bot.process_command(command)
        print(response)


if __name__ == "__main__":
    main()