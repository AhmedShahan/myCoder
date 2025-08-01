import argparse
import time
import os
from generator import generate_code

def simulate_typing_to_file(code: str, filename: str, delay: float = 0.03):
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, 'w') as f:
        f.write("# === LangCoder Output ===\n\n")
        f.flush()
        for line in code.split('\n'):
            for char in line:
                f.write(char)
                f.flush()
                time.sleep(delay)
            f.write('\n')
            f.flush()
            time.sleep(delay * 10)  # longer pause between lines

def main():
    parser = argparse.ArgumentParser(description="LangChain Live Code Writer")
    parser.add_argument('--file', type=str, default='generated/main.py', help='New file to create and write')
    args = parser.parse_args()
    target_file = args.file

    print(f"🤖 LangCoder Live CLI — Writing to: {target_file}")
    print("Type your coding task (e.g., 'create a FastAPI endpoint'). Type 'exit' to quit.\n")

    while True:
        try:
            task = input("> ").strip()
            if task.lower() in {"exit", "quit"}:
                break
            if not task:
                continue

            print("⏳ Generating code...\n")
            code = generate_code(task)

            print(f"✍️ Writing code to {target_file}...\n")
            simulate_typing_to_file(code, target_file)

            print(f"✅ Done! Code written to {target_file}\n")
        except KeyboardInterrupt:
            print("\n👋 Exiting LangCoder.")
            break
        except Exception as e:
            print(f"❌ Error: {e}\n")

if __name__ == "__main__":
    main()
