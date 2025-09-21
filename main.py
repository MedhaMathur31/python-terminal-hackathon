from commands import handle_command
from utils import get_prompt, add_to_history

def main():
    print("🔹 Welcome to PyTerminal v1.1")
    print("Type 'exit' or 'quit' to exit.\n")

    while True:
        try:
            cmd = input(get_prompt()).strip()
            if cmd.lower() in ["exit", "quit"]:
                print("Exiting PyTerminal... Goodbye! 👋")
                break
            add_to_history(cmd)
            print(handle_command(cmd))
        except KeyboardInterrupt:
            print("\nUse 'exit' or 'quit' to quit.")
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
