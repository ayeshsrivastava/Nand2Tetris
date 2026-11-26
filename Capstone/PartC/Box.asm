// Box.asm - Nand2Tetris Capstone Project (Part C)
// Student Roll Number: 2501420061
// Personal Number: K = 61
//
// Calculation:
// - Start Row = K = 61
// - Height = 20 rows (rows 61 through 80)
// - Width = 16 * ((K mod 4) + 1) = 16 * ((61 mod 4) + 1) = 16 * 2 = 32 pixels
// - Words per row = 32 pixels / 16 pixels per word = 2 words (from left edge)
// - Screen base address = 16384 (SCREEN)
// - Row 61 start address = SCREEN + 32 * 61 = 16384 + 1952 = 18336
//
// Behavior:
// While any key is pressed, draws a black box (32 pixels wide, 20 rows high, starting at row 61).
// When the key is released, clears the box (turns white).

(MAIN_LOOP)
    // Check keyboard input
    @KBD
    D=M

    // If key is pressed (KBD != 0), jump to KEY_PRESSED
    @KEY_PRESSED
    D;JNE

    // If key is released (KBD == 0), set color to 0 (white)
    @color
    M=0
    @DRAW_BOX
    0;JMP

(KEY_PRESSED)
    // Set color to -1 (black: all 1s in 16-bit 2's complement)
    @color
    M=-1

(DRAW_BOX)
    // Initialize rows_left = 20
    @20
    D=A
    @rows_left
    M=D

    // Initialize current_row = SCREEN + 32 * 61 = SCREEN + 1952 = 18336
    @SCREEN
    D=A
    @1952
    D=D+A
    @current_row
    M=D

(ROW_LOOP)
    // If rows_left == 0, finished drawing all 20 rows; check keyboard again
    @rows_left
    D=M
    @MAIN_LOOP
    D;JEQ

    // Load color into D
    @color
    D=M

    // Write word 0 of current row (pixels 0 to 15)
    @current_row
    A=M
    M=D

    // Write word 1 of current row (pixels 16 to 31)
    @current_row
    A=M+1
    M=D

    // Advance to next row: current_row = current_row + 32
    @32
    D=A
    @current_row
    M=D+M

    // Decrement rows_left
    @rows_left
    M=M-1

    // Continue to next row
    @ROW_LOOP
    0;JMP
