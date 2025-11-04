# Project 2: Editor

## Project Description
A simple text-processing application with console-based input and output.  
The program allows managing text paragraphs with various formatting options.

## Team Members
- **[rajkuthu]** – Scrum Master  
- **[pannasan]** – Product Owner  
- **[krishabi]** – Developer  
- **[gunasja1]** – Developer  

## Folder Structure
```
P2_Editor/
├── README.md
├── p2.py                    # Main program
├── src/
│   ├── paragraph_manager.py # Paragraph management
│   ├── command_parser.py    # Command processing
│   ├── formatter.py         # Text formatting
│   └── index_creator.py     # Index functionality
├── tests/
│   ├── testcases.md
│   ├── test_concept.md
└── docs/
    ├── sprint_protocols.md
    └── documentation.md
```

## Installation & Start
```bash
python p2.py
```

## Commands

### ADD [n]
Adds a new paragraph at position **n** (optional, otherwise at the end).  
If the position already exists, the user can choose to **overwrite** or **shift down**.
```bash
ADD
ADD 2
```

### DEL [n]
Deletes the paragraph at position **n** (optional, otherwise the last paragraph).
```bash
DEL
DEL 3
```

### DUMMY [n]
Inserts a dummy (placeholder) text at position **n** (optional, otherwise at the end).
```bash
DUMMY
DUMMY 1
```

### EXIT
Terminates the program.

### FORMAT RAW
Sets the output format to *RAW* (plain output) with paragraph numbers.

**Example:**
```bash
> FORMAT RAW
Format set to RAW.
> PRINT
<1>: This is the first paragraph
<2>: This is the second paragraph
<3>: This is the third paragraph
```

### FORMAT FIX <b>
Sets the output format to *FIXED COLUMN WIDTH* (width = b).

**Line Break Rules:**
- Break only after spaces  
- The space after a line break does not count toward line length  
- Words longer than the column width are split  
- If no space is found within the limit, break at the maximum width  

**Example with FORMAT FIX 20:**
```bash
> FORMAT FIX 20
Format set to FIX with width 20.
> PRINT
Virtute praecedunt,
quod fere cotidianis
proeliis cum
Germanis
contendunt, septentr
ionesimmensoslongusw
ordos
ionesimmensoslongusw
s.
```

### INDEX
Outputs all terms that appear more than three times and begin with a capital letter.
```bash
INDEX
```

### PRINT
Displays the text using the currently selected format.
```bash
PRINT
```

### REPLACE [n]
Replaces text in paragraph **n** (optional, otherwise the last paragraph).
```bash
REPLACE
REPLACE 2
```

## Functionality Components

### 1. Paragraph Management (`paragraph_manager.py`)
- Store and manage paragraphs  
- Add, delete, and retrieve paragraphs  
- Validate and clean input  

### 2. Command Parser (`command_parser.py`)
- Parse user input  
- Recognize commands and handle errors  
- Extract command parameters  

### 3. Formatter (`formatter.py`)
- RAW format: display with paragraph numbers  
- FIX format: display with fixed column width  
- Implement text wrapping rules  

### 4. Index Creator (`index_creator.py`)
- Generate a word index  
- Count occurrences (case-sensitive for capitalized words)  
- Display terms appearing more than three times  

## Testing
All tests are located in the `tests/` folder:
- Unit tests for individual modules  
- Integration tests for command execution  
- Formatting test cases  

Run all tests:
```bash
python -m pytest tests/
```

## Clean Code Principles
- Each function performs one specific task  
- Clear and descriptive names for variables and functions  
- No code duplication  
- Consistent abstraction levels  
- Detailed docstrings  
- Use of control flags in main loop  

## Documentation
See the `docs/` folder for:
- Sprint protocols  
- Detailed project documentation  

## Git Workflow
- Frequent commits with meaningful messages  
- Feature branches for new functions  
- Code reviews before merging  
- Equal contribution from all team members  
