# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

`lang-end-pj` is a collection of small practice projects to help developers consolidate their knowledge of a new programming language through hands-on implementation.

The goal is to provide complete, functional projects that cover core programming concepts—data structures, file I/O, string manipulation, sorting, error handling, etc.—so developers can practice implementing the same functionality in different languages.

## Project Structure

Currently contains one reference implementation:

- `demo.py` — Student Information Management System (Python)

### Student Information Management System (`demo.py`)

A console-based application demonstrating CRUD operations with file persistence.

**Architecture:**
- Single-file procedural design with function-based organization
- Data stored as stringified dictionaries in text file (`学生信息/student.txt`)
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
Each line in `学生信息/student.txt` is a Python dictionary string:
```
{'id': '1001', 'name': '张三', 'english': 85, 'python': 90, 'java': 78}
```

Read with `eval()` or `dict(eval(item))` to convert back to dictionary.

## Running the Project

```bash
python demo.py
```

## Adding New Language Implementations

When adding a new language implementation:

1. **Keep the same functionality** — All CRUD operations, sorting, backup, etc.
2. **Follow existing project naming** — Use descriptive filenames like `student_manager.go`, `student_manager.rs`
3. **Document language-specific patterns** — If the implementation uses idiomatic patterns specific to that language
4. **Test core functionality** — Ensure insert, search, delete, modify, sort all work

Suggested future project types (from README.md):
- Data management (CRUD operations)
- Algorithm implementation (sorting, searching)
- Utilities (file processing, text analysis)
- Simple games (guess number, tic-tac-toe)

## License

Apache License 2.0
