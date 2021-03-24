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

    @staticmethod
    def cleanup(string: str) -> str:
        return "".join(filter(lambda x: x in ['.', ',', '[', ']', '<', '>', '+', '-'], string))

    @staticmethod
    def match_parentheses(string: str) -> dict:
        pmap, pstack, start = {}, [], None

        for i, c in enumerate(string):
            if c == "[":
                pstack.append(i)
            elif c == "]":
                if len(pstack) == 0:
                    raise ValueError("An error occured!")

                start = pstack.pop()

            pmap[start] = i
            pmap[i] = start

        if len(pstack) > 0:
            raise ValueError("Unpaired brackets error!")

        return pmap

    def evaluate(self, code: str = None) -> None:
        if self.file_contents is None and code is None:
            raise ValueError("Please enter code or filename [When initializing] to evaluate!")

        if self.file_contents is not None:
            code = self.cleanup(list(self.file_contents))
        else:
            code = self.cleanup(list(code))

        bracemap = self.match_parentheses(code)

        cells = [0]
        pointer = 0
        cell_pointer = 0

        while pointer < len(code):
            command = code[pointer]

            if cell_pointer == len(cells):
                cells.append(0)

            if command == ">":
                cell_pointer += 1

            if command == "<":
                cell_pointer = 0 if cell_pointer <= 0 else cell_pointer - 1

            if command == "+":
                cells[cell_pointer] = cells[cell_pointer] + 1 if cells[cell_pointer] < 255 else 0

            if command == "-":
                cells[cell_pointer] = cells[cell_pointer] - 1 if cells[cell_pointer] > 0 else 255

            if command == "[" and cells[cell_pointer] == 0:
                pointer = bracemap[pointer]

            if command == "]" and cells[cell_pointer] != 0:
                pointer = bracemap[pointer]

            if command == ".":
                sys.stdout.write(chr(cells[cell_pointer]))

            if command == ",":
                print("Input of a single character needed.")
                cells[pointer] = ord(input())
            
            pointer += 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python interpreter.py <filename>.bf")
        sys.exit(1)

    bf = BrainFuck(sys.argv[1])
    bf.evaluate()
