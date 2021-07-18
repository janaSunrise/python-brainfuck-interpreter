## Brainfuck interpreter in Python

A simple and easy to use brainfuck interpreter written in python.

### Usage:

#### As a CLI tool:

- `python interpreter.py <filename>.bf`

#### As a module in your code

```py
from interpreter import BrainFuck

# Instantiate the Brainfuck code evaluation object.
bf = BrainFuck()

# To execute code
bf.evaluate("Your brainfuck code here")

# To execute from file
bf.evaluate(file="<filename>")
```

### Brainfuck examples:

- Printing hello world!

```brainfuck
> ++ .                  | "H"
> + .                   | "e"
+++++ ++ .              | "l"
.                       | "l"
+++ .                   | "o"
> ++ .                  | " "
<< +++++ +++++ +++++ .  | "W"
> .                     | "o"
+++ .                   | "r"
----- - .               | "l"
----- --- .             | "d"
> + .                   | "!"
> .                     | "\n"
```

- Basic things

```
> | Increases memory pointer, or moves the pointer to the right 1 block.
< | Decreases memory pointer, or moves the pointer to the left 1 block.

+ | Increases value stored at the block pointed to by the memory pointer
- | Decreases value stored at the block pointed to by the memory pointer

[ | Like c while(cur_block_value != 0) loop.
] | If block currently pointed to's value is not zero, jump back to [

, | Like c getchar(). input 1 character.
. | Like c putchar(). print 1 character to the console
```

<div align="center">Made by Sunrit Jana with ❤️</div>
