# Projekt 2: Editor

## Projektbeschreibung
Eine einfache Textverarbeitung mit Ein- und Ausgabe über die Konsole. Die Anwendung ermöglicht das Verwalten von Textabsätzen mit verschiedenen Formatierungsoptionen.

## Teammitglieder
- [Name 1] - ScrumMaster
- [Name 2] - Product Owner
- [Name 3] - Entwickler
- [Name 4] - Entwickler

## Ordnerstruktur
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
│   ├── test_paragraph.py
│   ├── test_formatter.py
│   └── test_index.py
└── docs/
    ├── sprint_protocols.md
    ├── test_concept.md
    └── documentation.md
```

## Installation & Start
```bash
python p2.py
```

## Befehle

### ADD [n]
Fügt einen neuen Absatz an Position n ein (optional, sonst am Ende)
```
ADD
ADD 2
```

### DEL [n]
Löscht den Absatz an Position n (optional, sonst letzter Absatz)
```
DEL
DEL 3
```

### DUMMY [n]
Fügt einen Blindtext an Position n ein
```
DUMMY
DUMMY 1
```

### EXIT
Beendet das Programm

### FORMAT RAW
Setzt Ausgabeformat auf Rohformat mit Absatznummern

**Beispiel:**
```
> FORMAT RAW
Format auf RAW gesetzt.
> PRINT
<1>: Dies ist der erste Absatz
<2>: Dies ist der zweite Absatz
<3>: Dies ist der dritte Absatz
```

### FORMAT FIX <b>
Setzt Ausgabeformat mit fester Spaltenbreite b

**Umbruch-Regeln:**
- Umbruch nur nach Leerzeichen
- Leerzeichen nach dem umgebrochen wird zählt nicht zur Zeilenlänge
- Wörter länger als Spaltenbreite werden getrennt
- Keine Umbruchstelle innerhalb Spaltenbreite = Umbruch nach Spaltenbreite

**Beispiel mit FORMAT FIX 20:**
```
> FORMAT FIX 20
Format auf FIX mit Breite 20 gesetzt.
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

**Weitere Beispiele:**
```
FORMAT FIX 30
FORMAT FIX 50
FORMAT FIX 80
```

### INDEX
Gibt Index aller Begriffe aus, die öfter als 3x vorkommen
```
INDEX
```

### PRINT
Gibt Text im aktuellen Format aus
```
PRINT
```

### REPLACE [n]
Ersetzt Text im Absatz n
```
REPLACE
REPLACE 2
```

## Functionality Components

### 1. Paragraph Management (paragraph_manager.py)
- Store and manage paragraphs
- Add, delete and retrieve paragraphs
- Input validation

### 2. Command Parser (command_parser.py)
- Parse user input
- Command recognition and error handling
- Parameter extraction

### 3. Formatter (formatter.py)
- RAW format: Output with paragraph numbers
- FIX format: Output with fixed column width
- Text wrapping according to rules

### 4. Index Creator (index_creator.py)
- Create word directory
- Count terms (capital letters)
- Output of occurrences

## Testing
Tests are located in the `tests/` folder:
- Unit tests for individual modules
- Integration tests for command execution
- Test cases for formatting

Run all tests:
```bash
python -m pytest tests/
```

## Clean Code Principles
- Functions are short and fulfill only one task
- Descriptive variable and function names
- No code duplication
- Consistent abstraction levels
- Comprehensive docstrings

## Documentation
See `docs/` folder for:
- Sprint protocols
- Test concept
- Detailed documentation

## Used Constructs
- Only PROG1 and PROG2 modules
- No external libraries
- Standard Python functionality

## Git Workflow
- Regular commits with meaningful messages
- Feature branches for new functions
- Code reviews before merge
- All team members contribute code

## Known Limitations
- No file input/output
- Console-based interaction only
- Input validation restricted to defined characters