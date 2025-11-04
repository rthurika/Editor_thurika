"""
Index Creator Module for Word Directory
Finds terms that occur more than 3 times
"""

import re


class IndexCreator:
    """Creates index of frequent terms"""

    def create_index(self, paragraphs):
        """
        Creates index of all terms that occur > 3 times

        Args:
            paragraphs: List of paragraphs

        Returns:
            Sorted dictionary {Term: [paragraph numbers]}
        """
        if len(paragraphs) == 0:
            return {}

        term_occurrences = {}

        for para_num, paragraph in enumerate(paragraphs, 1):
            terms = self.find_terms(paragraph)

            for term in terms:
                if term not in term_occurrences:
                    term_occurrences[term] = []

                if para_num not in term_occurrences[term]:
                    term_occurrences[term].append(para_num)

        filtered = self.filter_frequent(term_occurrences)
        return filtered

    def find_terms(self, text):
        """
        Finds all terms that start with capital letters

        Args:
            text: Text to search

        Returns:
            List of terms
        """
        pattern = r'\b[A-ZÄÖÜ][a-zäöüA-ZÄÖÜ]*\b'
        terms = re.findall(pattern, text)
        return terms

    def filter_frequent(self, term_dict):
        """
        Filters terms that occur more than 3 times

        Args:
            term_dict: Dictionary with all terms

        Returns:
            Filtered dictionary
        """
        filtered = {}

        for term, positions in term_dict.items():
            total_count = len(positions)
            if total_count > 3:
                filtered[term] = positions

        return dict(sorted(filtered.items()))

    def format_index(self, index_dict):
        """
        Formats index for output

        Args:
            index_dict: Index dictionary

        Returns:
            Formatted string
        """
        if len(index_dict) == 0:
            return "No terms found (must occur > 3 times)."

        lines = []
        for term, positions in index_dict.items():
            pos_string = ",".join(map(str, positions))
            lines.append(f"{term} {pos_string}")

        return "\n".join(lines)