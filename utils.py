import os

# ANSI escape codes for colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# Format output with color based on success or error
def format_output(output, success=True):
    if success:
        return f"{GREEN}{output}{RESET}"
    else:
        return f"{RED}{output}{RESET}"

# Generate a prompt showing current directory
def get_prompt():
    cwd = os.getcwd()
    return f"{YELLOW}pyterm {cwd}>{RESET} "

# Optional: keep command history (last n commands)
command_history = []

def add_to_history(cmd, max_len=10):
    command_history.append(cmd)
    if len(command_history) > max_len:
        command_history.pop(0)

def show_history():
    if not command_history:
        return "No commands executed yet."
    return "\n".join(command_history)
