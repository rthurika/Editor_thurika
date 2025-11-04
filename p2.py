"""
Main Program for Editor
Project 2 - Text Editor with Console Control
"""

from src.command_parser import CommandParser
from src.formatter import Formatter
from src.index_creator import IndexCreator
from src.paragraph_manager import ParagraphManager


class Editor:
    """Main class for Editor application"""

    def __init__(self):
        """Initializes editor with all components"""
        self.paragraph_manager = ParagraphManager()
        self.parser = CommandParser()
        self.formatter = Formatter()
        self.index_creator = IndexCreator()
        self.running = True

    def start(self):
        """Starts the editor main loop"""
        print("=== Editor started ===")
        print("Type 'EXIT' to quit")
        print()

        while self.running:
            try:
                user_input = input("> ")
                self.process_input(user_input)
            except KeyboardInterrupt:
                print("\nExiting program...")
                break
            except Exception as e:
                print(f"Error: {e}")

    def process_input(self, user_input):
        """
        Processes user input

        Args:
            user_input: Input string
        """
        command_dict = self.parser.parse_command(user_input)

        if not self.parser.is_valid(command_dict):
            print("Unknown command!")
            return

        command = command_dict["command"]

        if command == "ADD":
            self.execute_add(command_dict["position"])
        elif command == "DEL":
            self.execute_del(command_dict["position"])
        elif command == "DUMMY":
            self.execute_dummy(command_dict["position"])
        elif command == "EXIT":
            self.execute_exit()
        elif command == "FORMAT":
            self.execute_format(command_dict["parameters"])
        elif command == "INDEX":
            self.execute_index()
        elif command == "PRINT":
            self.execute_print()
        elif command == "REPLACE":
            self.execute_replace(command_dict["position"])

    def execute_add(self, position):
        """Executes ADD command (validate position BEFORE asking for text)."""
        # validate position first (no prompt if invalid)
        if position is not None:
            max_pos = self.paragraph_manager.get_paragraph_count() + 1
            if position < 1 or position > max_pos:
                print(f"Error adding paragraph. Position out of range (allowed: 1..{max_pos}).")
                return

        print("Enter text:")
        text = input()

        success = self.paragraph_manager.add_paragraph(text, position)

        if success:
            if position is None:
                print("Paragraph added.")
            else:
                print(f"Paragraph added at position {position}.")
        else:
            # (should not happen now, but keep a safe fallback)
            print("Error adding paragraph. Position out of range.")

    def execute_del(self, position):
        """Executes DEL command (validate BEFORE delete)."""
        total = self.paragraph_manager.get_paragraph_count()
        if total == 0:
            print("Error deleting paragraph. No paragraphs available.")
            return
        if position is not None and (position < 1 or position > total):
            print(f"Error deleting paragraph. Position out of range (allowed: 1..{total}).")
            return

        success = self.paragraph_manager.delete_paragraph(position)
        if success:
            print(f"Paragraph {position or total} deleted.")
        else:
            print("Error deleting paragraph.")

    def execute_dummy(self, position):
        """Executes DUMMY command (validate BEFORE insert)."""
        max_pos = self.paragraph_manager.get_paragraph_count() + 1
        if position is not None and (position < 1 or position > max_pos):
            print(f"Error inserting dummy text. Position out of range (allowed: 1..{max_pos}).")
            return

        success = self.paragraph_manager.insert_dummy_text(position)
        if success:
            print(f"Dummy text inserted at position {position or self.paragraph_manager.get_paragraph_count()}.")
        else:
            print("Error inserting dummy text.")

    def execute_exit(self):
        """Executes EXIT command"""
        print("Editor is closing.")
        self.running = False

    def execute_format(self, parameters):
        """Executes FORMAT command"""
        if parameters[0] == "RAW":
            self.formatter.set_format_raw()
            print("Format set to RAW.")
        elif parameters[0] == "FIX":
            self.formatter.set_format_fix(parameters[1])
            print(f"Format set to FIX with width {parameters[1]}.")

    def execute_index(self):
        """Executes INDEX command"""
        paragraphs = self.paragraph_manager.get_all_paragraphs()
        index = self.index_creator.create_index(paragraphs)
        output = self.index_creator.format_index(index)
        print(output)

    def execute_print(self):
        """Executes PRINT command"""
        paragraphs = self.paragraph_manager.get_all_paragraphs()
        output = self.formatter.format_output(paragraphs)
        print(output)

    def execute_replace(self, position):
        """Executes REPLACE command (validate BEFORE editing)."""
        total = self.paragraph_manager.get_paragraph_count()
        if total == 0:
            print("No paragraphs available.")
            return
        if position is None:
            position = total
        if position < 1 or position > total:
            print(f"Error replacing text. Position out of range (allowed: 1..{total}).")
            return

        print("Text to search for:")
        old_text = input()
        print("Replacement text:")
        new_text = input()

        success = self.paragraph_manager.replace_text(position, old_text, new_text)
        if success:
            print(f"Text replaced in paragraph {position}.")
        else:
            print("Text not found or replacement failed.")


def main():
    """Main function"""
    editor = Editor()
    editor.start()


if __name__ == "__main__":
    main()