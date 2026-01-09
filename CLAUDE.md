# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`lang-end-pj` is a collection of small practice projects to help developers consolidate their knowledge of a new programming language through hands-on implementation.

The goal is to provide complete, functional projects that cover core programming concepts—data structures, file I/O, string manipulation, sorting, error handling, etc.—so developers can practice implementing the same functionality in different languages.

## Project Structure

Projects are organized by **project name**, with each project containing multiple language implementations:

```
lang-end-pj/
├── projects/
│   ├── student-manager/        # Student Information Management System
│   │   ├── README.md
│   │   ├── python/
│   │   │   └── demo.py
│   │   ├── go/              (planned)
│   │   └── typescript/      (planned)
│   ├── todo-list/           (planned)
│   └── notes-app/           (planned)
├── README.md
├── CLAUDE.md
└── LICENSE
```

### Student Information Management System

Located at `projects/student-manager/`

**Architecture (Python implementation):**
- Single-file procedural design with function-based organization
- Data stored as stringified dictionaries in text file
- Main loop with menu-driven UI (`main()` → `menu()` → function dispatch)

**Key functions:**
- `main()` — Entry point, menu loop with input validation
- `insert()` — Add student records
- `search()` — Query by ID or name
- `delete()` — Remove student by ID
- `modify()` — Update student info
- `mysort()` — Sort by subject (english/python/java/total) with asc/desc
- `show()` — Display all records
- `total()` — Count records
- `backup()` — Create timestamped backup before destructive operations
- `save()` / `save2()` — Persist records to file (legacy versions)

**Data format:**
Each line in the data file is a Python dictionary string:
```
{'id': '1001', 'name': '张三', 'english': 85, 'python': 90, 'java': 78}
```

Read with `eval()` or `dict(eval(item))` to convert back to dictionary.

## Running Projects

Each project has its own README with specific instructions. Example:

```bash
# Student Manager (Python)
cd projects/student-manager/python
python demo.py
```

## Adding New Implementations

### Adding a new language to an existing project

1. Create the language directory: `projects/<project-name>/<language>/`
2. Implement the same functionality as the reference implementation
3. Create a `data/` subdirectory for any data files
4. Update the project's README with the new implementation

### Adding a new project

1. Create project directory: `projects/<project-name>/`
2. Create a README.md describing:
   - Project overview
   - Key concepts covered
   - Main features
   - How to run each language implementation
3. Create language subdirectories (python/, go/, typescript/, etc.)
4. Each language implementation should maintain its data in a `data/` subdirectory

**Naming conventions:**
- Project directories: kebab-case (e.g., `todo-list`, `notes-app`)
- Source files: Follow language conventions (snake_case for Python, PascalCase for Go, etc.)

## Data Files

Each language implementation stores its data in its own `data/` subdirectory:
- `projects/student-manager/python/data/`
- `projects/todo-list/go/data/`
- etc.

Data directories are gitignored to avoid committing user data.

## License

Apache License 2.0
