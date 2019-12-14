# BFIL
BrainFuck intermediate language
an assembler like language to help create simple Brainfuck code
The interpreter keeps track of the pointers position and handles moving the pointer from place to place automaticly, so "gt 1" will in BF add the instructions required to get to cell 1. it also handles printing predefined strings, it uses an inefficient but simple method of presetting a value and changing it by an amount to print out every character of the string. the interpreter also handles 'memory' or the ability to designate a chunk of memory to act as longer term memory.

to do:
    -add a function system {semi implemented}

has simple commands :
 gt {address} - goto position
  inc          - increment value
  dec          - decrement value
  add {aexpr}  - add aexpr
  sub {aexpr}  - subtract aexpr
  mvf {aexpr}  - move pointer forward by aexpr
  mvb {aexpr}  - move pointer backward by aexpr
  in           - input
  out          - output

and has more high-level commands for more niche things:
  mem   wa,ms  - define working area(wa) and memory start(ms) for the interpreter
  stm  address - store given cell in defined memory are using working area to preserve the cell's value
  ldm  address - loads from given address to current cell preserving the value in memory
  prnt char    - set's cells value to character code and tells it to print
  lprnt str    - uses an initial set to the first chars value and changes value over time whilst printing
  move address - moves a cell value destructivly
  rmove dist   - moves a cell forward a given distance
  
 ===============================example================================
 given input (
 add 4
 mvf 2
 add 3
 mvb 2
 loop
    dec
    mvf 2
    loop
        dec
        mvb 1
        inc
        mvf 2
        inc
        mvb 1
    end
    mvf 1
    loop
        dec
        mvb 1
        inc
        mvf 1
    end
    mvb 3
end
)
will give
++++>>+++<<[->>[-<+>>+<]>[-<+>]<<<]
