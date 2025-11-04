"""
Formatter Module for Text Output
Supports RAW and FIX format
"""


class Formatter:
    """Formats paragraphs for output"""

    def __init__(self):
        """Initializes formatter with RAW format"""
        self.format_type = "RAW"
        self.column_width = 0

    def set_format_raw(self):
        """Sets format to RAW"""
        self.format_type = "RAW"

    def set_format_fix(self, width):
        """
        Sets format to FIX with column width

        Args:
            width: Column width
        """
        self.format_type = "FIX"
        self.column_width = width

    def format_output(self, paragraphs):
        """
        Formats all paragraphs for output

        Args:
            paragraphs: List of paragraphs

        Returns:
            Formatted text as string
        """
        if self.format_type == "RAW":
            return self.format_raw(paragraphs)
        else:
            return self.format_fix(paragraphs)

    def format_raw(self, paragraphs):
        """
        Formats in RAW format with paragraph numbers

        Args:
            paragraphs: List of paragraphs

        Returns:
            Formatted text
        """
        if len(paragraphs) == 0:
            return "No paragraphs available."

        lines = []
        for i, paragraph in enumerate(paragraphs, 1):
            lines.append(f"<{i}>: {paragraph}")
        return "\n".join(lines)

    def format_fix(self, paragraphs):
        """
        Formats with fixed column width

        Args:
            paragraphs: List of paragraphs

        Returns:
            Formatted text
        """
        if len(paragraphs) == 0:
            return "No paragraphs available."

        all_lines = []
        for paragraph in paragraphs:
            lines = self.wrap_text(paragraph, self.column_width)
            all_lines.extend(lines)
            all_lines.append("")

        return "\n".join(all_lines)

    def wrap_text(self, text, width):
        """
        Wraps text according to rules

        Args:
            text: Text to wrap
            width: Maximum line width

        Returns:
            List of lines
        """
        lines = []
        words = text.split()
        current_line = ""

        for word in words:
            if len(word) <= width:
                if len(current_line) == 0:
                    current_line = word
                elif len(current_line) + 1 + len(word) <= width:
                    current_line += " " + word
                else:
                    lines.append(current_line)
                    current_line = word
            else:
                if current_line:
                    lines.append(current_line)
                    current_line = ""

                lines.extend(self.split_long_word(word, width))

        if current_line:
            lines.append(current_line)

        return lines

    def split_long_word(self, word, width):
        """
        Splits a word that is too long

        Args:
            word: Word to split
            width: Maximum length

        Returns:
            List of word parts
        """
        parts = []
        while len(word) > width:
            parts.append(word[:width])
            word = word[width:]
        if word:
            parts.append(word)
        return parts