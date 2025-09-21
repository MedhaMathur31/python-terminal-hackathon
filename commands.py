import os
from utils import format_output

def handle_command(cmd):
    cmd = cmd.strip()
    if cmd == "ls":
        return format_output("\n".join(os.listdir(".")))
    
    elif cmd.startswith("echo "):
        return format_output(cmd[5:])
    
    elif cmd.startswith("cat "):
        try:
            with open(cmd[4:], "r") as f:
                return format_output(f.read())
        except FileNotFoundError:
            return format_output("File not found", success=False)
    
    elif cmd.startswith("rm "):
        try:
            os.remove(cmd[3:])
            return format_output(f"Deleted {cmd[3:]}")
        except FileNotFoundError:
            return format_output("File not found", success=False)
    
    elif cmd.startswith("mkdir "):
        folder = cmd[6:]
        try:
            os.mkdir(folder)
            return format_output(f"Folder '{folder}' created")
        except FileExistsError:
            return format_output(f"Folder '{folder}' already exists", success=False)
        except Exception as e:
            return format_output(f"Error: {str(e)}", success=False)
    
    elif cmd == "pwd":
        return format_output(os.getcwd())
    
    elif cmd.startswith("cd "):
        folder = cmd[3:]
        try:
            os.chdir(folder)
            return format_output(f"Changed directory to {folder}")
        except FileNotFoundError:
            return format_output("Directory not found", success=False)
    
    elif cmd == "history":
        from utils import show_history
        return format_output(show_history())
    
    else:
        return format_output(f"Unknown command: {cmd}", success=False)
