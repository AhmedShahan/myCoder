import argparse
from generator import generate_code

def main():
    parser = argparse.ArgumentParser(description="LangChain Code Generator")
    parser.add_argument("--file", type=str, help="Input file with code prompt")
    parser.add_argument("--output", type=str, help="Output file to save result", default=None)
    parser.add_argument("--append", action="store_true", help="Append to original file")

    args = parser.parse_args()

    with open(args.file, "r") as f:
        prompt = f.read()

    result = generate_code(prompt)

    if args.output:
        with open(args.output, "w") as f:
            f.write(result)
    elif args.append:
        with open(args.file, "a") as f:
            f.write("\n\n# Generated Code:\n")
            f.write(result)
    else:
        print("\n===== Generated Code =====\n")
        print(result)

if __name__ == "__main__":
    main()
