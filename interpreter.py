import sys


class BrainFuck:
    def __init__(self, filename: str = None) -> None:
        if not filename:
            self.file_contents = filename
        else:
            self.file_contents = self.get_file_contents(filename)

    @staticmethod
    def get_file_contents(filename: str) -> str:
        with open(filename, "r") as file:
            contents = file.read()

        return contents


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python interpreter.py <filename>.bf")
        sys.exit(1)

    bf = BrainFuck(sys.argv[1])
    print(bf.eval())
