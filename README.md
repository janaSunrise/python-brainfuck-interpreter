## brainfuck-interpreter

A simple and easy to use brainfuck interpreter written in python.

### Usage:

#### As a CLI tool:

- `python interpreter.py <filename>.bf`

#### As a module in your code

```py
from interpreter import BrainFuck

bf = BrainFuck()
bf.eval("Code here")
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
> = increases memory pointer, or moves the pointer to the right 1 block.
< = decreases memory pointer, or moves the pointer to the left 1 block.
+ = increases value stored at the block pointed to by the memory pointer
- = decreases value stored at the block pointed to by the memory pointer
[ = like c while(cur_block_value != 0) loop.
] = if block currently pointed to's value is not zero, jump back to [
, = like c getchar(). input 1 character.
. = like c putchar(). print 1 character to the console
```
