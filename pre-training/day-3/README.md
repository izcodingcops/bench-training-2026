# Task Tracker

A command-line task tracker built with Python. Tasks are saved to `tasks.json`.

## Usage
```bash
# Add a task
python tasks.py add "Fix login bug"

# List all tasks
python tasks.py list

# Filter by status
python tasks.py list --filter todo
python tasks.py list --filter done

# Mark a task as done
python tasks.py done 2

# Delete a task
python tasks.py delete 3
```

## Why a class instead of just functions?

I used classes instead so i don't have to reload the file on every operation. In every terminal call , i simply used the instance of task manager instead of reloading the file on every operation