"""
Paragraph Management for the Editor
Manages the list of text paragraphs
"""

import re


class ParagraphManager:
    """Manages all text paragraphs"""

    def __init__(self):
        """Initializes empty paragraph list"""
        self.paragraphs = []

    def add_paragraph(self, text, position=None):
        """
        Adds a paragraph.
        If position is given:
          - Only 1..len+1 allowed (no gaps like 500).
          - If position <= len: ask overwrite or shift down.
          - If position == len+1: append.
        """
        cleaned_text = self.validate_text(text)

        # No position -> append at end
        if position is None:
            self.paragraphs.append(cleaned_text)
            return True

        # Disallow gaps: only 1..len+1
        if position < 1 or position > len(self.paragraphs) + 1:
            return False

        # Existing slot -> ask user
        if position <= len(self.paragraphs):
            print(f"A paragraph already exists at position {position}:")
            print(f"→ {self.paragraphs[position - 1][:50]}")
            choice = input("Overwrite (o) or shift down (s)? [o/s] > ").strip().lower()
            if choice == "s":
                self.paragraphs.insert(position - 1, cleaned_text)
            else:
                self.paragraphs[position - 1] = cleaned_text
            return True

        # position == len+1 -> append
        self.paragraphs.append(cleaned_text)
        return True

    def delete_paragraph(self, position=None):
        """
        Deletes a paragraph

        Args:
            position: Position (1-based), None for last

        Returns:
            True on success, False on error
        """
        if len(self.paragraphs) == 0:
            return False

        if position is None:
            self.paragraphs.pop()
            return True

        if position < 1 or position > len(self.paragraphs):
            return False

        self.paragraphs.pop(position - 1)
        return True

    def replace_text(self, position, old_text, new_text):
        """
        Replaces text in a paragraph

        Args:
            position: Position (1-based), None for last
            old_text: Text to search for
            new_text: Replacement text

        Returns:
            True on success, False if not found
        """
        if position is None:
            position = len(self.paragraphs)

        if position < 1 or position > len(self.paragraphs):
            return False

        paragraph = self.paragraphs[position - 1]
        if old_text not in paragraph:
            return False

        new_paragraph = paragraph.replace(old_text, new_text)
        self.paragraphs[position - 1] = self.validate_text(new_paragraph)
        return True

    def get_paragraph(self, position):
        """
        Returns a paragraph

        Args:
            position: Position (1-based)

        Returns:
            Paragraph text or None
        """
        if position < 1 or position > len(self.paragraphs):
            return None
        return self.paragraphs[position - 1]

    def get_all_paragraphs(self):
        """
        Returns all paragraphs

        Returns:
            List of all paragraphs
        """
        return self.paragraphs.copy()

    def get_paragraph_count(self):
        """
        Returns number of paragraphs

        Returns:
            Number of paragraphs
        """
        return len(self.paragraphs)

    def validate_text(self, text):
        """
        Validates and cleans input text
        Allows: A-Z, a-z, Umlauts, 0-9 and .,:;-!?'()"%@+*[]{}/\&#$

        Args:
            text: Text to validate

        Returns:
            Cleaned text
        """
        allowed_chars = r'[A-Za-zäöüÄÖÜ0-9 .,:;\-!?\'\(\)"%@+*\[\]{}/\\&#$]'
        cleaned = ''.join(re.findall(allowed_chars, text))
        return cleaned

    def insert_dummy_text(self, position=None):
        """
        Inserts a dummy text

        Args:
            position: Position (1-based), None for end

        Returns:
            True on success
        """
        dummy = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
                 "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
                 "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.")
        return self.add_paragraph(dummy, position)