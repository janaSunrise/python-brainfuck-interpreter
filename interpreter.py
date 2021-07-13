import sys
import typing as t


class BrainFuck:
    @staticmethod
    def get_file_contents(filename: str) -> str:
        with open(filename, "r") as file:
            contents = file.read()

        return contents

    @staticmethod
    def remove_comments(string: str) -> str:
        return "".join(
            filter(
                lambda x: x in [".", ",", "[", "]", "<", ">", "+", "-"],
                string
            )
        )

    @staticmethod
    def match_parentheses(string: t.Union[str, list]) -> dict:
        # Initialize variables
        pmap, pstack, start = {}, [], None

        # Ensure the brackets are paired.
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

    @staticmethod
    def get_jump_pos(bracemap, pointer):
        return bracemap[pointer]

    def evaluate(self, code: str = None, filename: str = None) -> None:
        # Error handling
        if filename is None and code is None:
            raise ValueError(
                "Please enter code or filename to evaluate!"
            )

        # File or code handling
        if filename is not None:
            file_contents = self.get_file_contents(filename)
            code = self.remove_comments(list(file_contents))
        else:
            code = self.remove_comments(list(code))

        # Evaluation variables
        bracemap = self.match_parentheses(code)

        cells = [0]
        pointer, cell_pointer = 0, 0

        # Main eval loop
        while pointer < len(code):
            command = code[pointer]

            if cell_pointer == len(cells):
                cells.append(0)

            if command == ">":
                cell_pointer += 1

            if command == "<":
                cell_pointer = 0 if cell_pointer <= 0 else cell_pointer - 1

            if command == "+":
                cells[cell_pointer] = (
                    cells[cell_pointer] + 1 if cells[cell_pointer] < 255 else 0
                )

            if command == "-":
                cells[cell_pointer] = (
                    cells[cell_pointer] - 1 if cells[cell_pointer] > 0 else 255
                )

            if command == "[" and cells[cell_pointer] == 0:
                pointer = self.get_jump_pos(bracemap, pointer)

            if command == "]" and cells[cell_pointer] != 0:
                pointer = self.get_jump_pos(bracemap, pointer)

            if command == ".":
                sys.stdout.write(chr(cells[cell_pointer]))

            if command == ",":
                print("Input of a single character needed: ", end="")
                cells[pointer] = ord(input())

            pointer += 1


if __name__ == "__main__":
    # Args Handling
    if len(sys.argv) != 2:
        print("Usage: python interpreter.py <filename>.bf")
        sys.exit(1)

    # Initialize and evaluate
    bf = BrainFuck()
    bf.evaluate(filename=sys.argv[1])
