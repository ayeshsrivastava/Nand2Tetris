// Box.asm for Roll No: 2501420061 (K=61)
// Box starts at row 61 (address 18336)
// Width: 32 pixels (2 words)
// Height: 20 rows

(MAIN)
@KBD
D=M
@SET_BLACK
D;JNE      // If any key is pressed, jump to SET_BLACK

// If no key, fill = 0 (white)
@0
D=A
@fill
M=D
@DRAW
0;JMP

(SET_BLACK)
// If key pressed, fill = -1 (black)
@1
D=-A
@fill
M=D

(DRAW)
// Set starting address (Row 61 = 16384 + 32*61 = 18336)
@18336
D=A
@ptr
M=D

// Set row counter to 20
@20
D=A
@row_count
M=D

(DRAW_ROW)
// Draw two words (32 pixels wide)
@fill
D=M
@ptr
A=M
M=D        // Write first word (pixels 0-15)

@ptr
A=M+1
M=D        // Write second word (pixels 16-31)

// Move pointer to the next row (+32)
@32
D=A
@ptr
M=M+D

// Decrement row counter
@row_count
M=M-1
D=M
@DRAW_ROW
D;JGT      // If row_count > 0, draw next row

@MAIN
0;JMP
