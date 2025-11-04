"""
Command Parser Module for the Editor
Processes user input and extracts commands
"""


class CommandParser:
    """Parses and validates user commands"""

    def __init__(self):
        """Initializes parser with valid commands"""
        self.valid_commands = [
            "ADD", "DEL", "DUMMY", "EXIT", "FORMAT",
            "INDEX", "PRINT", "REPLACE"
        ]

    def parse_command(self, input_str):
        """
        Parses user input

        Args:
            input_str: Input string

        Returns:
            Dictionary with command, parameters, position or None
        """
        parts = input_str.strip().split()

        if len(parts) == 0:
            return None

        command = parts[0].upper()

        if command == "FORMAT":
            return self.parse_format_command(parts)

        if command not in self.valid_commands:
            return None

        position = None
        if len(parts) > 1:
            position = self.parse_position(parts[1])
            # If a position token is present but invalid -> reject command
            if position is None and command in ("ADD", "DEL", "DUMMY", "REPLACE"):
                return None

        return {
            "command": command,
            "position": position,
            "parameters": parts[1:] if len(parts) > 1 else []
        }

    def parse_format_command(self, parts):
        """
        Parses FORMAT command

        Args:
            parts: List of command parts

        Returns:
            Command dictionary or None
        """
        if len(parts) < 2:
            return None

        format_type = parts[1].upper()

        if format_type == "RAW":
            return {
                "command": "FORMAT",
                "parameters": ["RAW"],
                "position": None
            }

        if format_type == "FIX":
            if len(parts) < 3:
                return None

            width = self.parse_number(parts[2])
            if width is None or width <= 0:
                return None

            return {
                "command": "FORMAT",
                "parameters": ["FIX", width],
                "position": None
            }

        return None

    def parse_position(self, text):
        """
        Parses position like 3 or [3].
        Returns int or None if invalid.
        """
        import re
        s = text.strip()
        m = re.match(r'^\[?(\d+)\]?$', s)  # accepts "3" or "[3]"
        return int(m.group(1)) if m else None

    def parse_number(self, text):
        """
        Parses numeric value

        Args:
            text: String with number

        Returns:
            Number as int or None
        """
        try:
            number = int(text)
            return number
        except ValueError:
            return None

    def is_valid(self, command_dict):
        """
        Checks if command is valid

        Args:
            command_dict: Parsed command

        Returns:
            True if valid
        """
        return command_dict is not None