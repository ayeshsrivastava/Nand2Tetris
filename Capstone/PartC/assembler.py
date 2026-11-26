#!/usr/bin/env python3
"""
Hack Assembler for Nand2Tetris Capstone Project (Part B)
Student Roll No: 2501420061  (K = 61, K mod 3 = 1)

Extra Feature (K mod 3 = 1):
  For any erroneous line in the assembly source, print a clear message with the
  exact line number (e.g. "Line 7: invalid instruction '...' (reason)") instead of crashing.
"""

import sys
import re
import os

PREDEFINED_SYMBOLS = {
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,
    "SCREEN": 16384,
    "KBD": 24576,
    **{f"R{i}": i for i in range(16)}
}

COMP_TABLE = {
    # a = 0 (operations on D and A)
    "0": "0101010",
    "1": "0111111",
    "-1": "0111010",
    "D": "0001100",
    "A": "0110000",
    "!D": "0001101",
    "!A": "0110001",
    "-D": "0001111",
    "-A": "0110011",
    "D+1": "0011111",
    "A+1": "0110111",
    "D-1": "0001110",
    "A-1": "0110010",
    "D+A": "0000010",
    "D-A": "0010011",
    "A-D": "0000111",
    "D&A": "0000000",
    "D|A": "0010101",
    # a = 1 (operations on D and M)
    "M": "1110000",
    "!M": "1110001",
    "-M": "1110011",
    "M+1": "1110111",
    "M-1": "1110010",
    "D+M": "1000010",
    "D-M": "1010011",
    "M-D": "1000111",
    "D&M": "1000000",
    "D|M": "1010101"
}

DEST_TABLE = {
    "": "000",
    "M": "001",
    "D": "010",
    "MD": "011",
    "DM": "011",
    "A": "100",
    "AM": "101",
    "AD": "110",
    "AMD": "111",
    "ADM": "111"
}

JUMP_TABLE = {
    "": "000",
    "JGT": "001",
    "JEQ": "010",
    "JGE": "011",
    "JLT": "100",
    "JNE": "101",
    "JLE": "110",
    "JMP": "111"
}

VALID_SYMBOL_REGEX = re.compile(r"^[a-zA-Z_.$:][a-zA-Z0-9_.$:]*$")

class HackAssembler:
    def __init__(self):
        self.symbol_table = dict(PREDEFINED_SYMBOLS)
        self.next_variable_address = 16
        self.errors = []

    def clean_line(self, line):
        """Remove comments and leading/trailing whitespace."""
        comment_idx = line.find("//")
        if comment_idx != -1:
            line = line[:comment_idx]
        return line.strip()

    def first_pass(self, raw_lines):
        """
        First reading:
        - Strip whitespace and comments.
        - Record label pseudo-commands (LABEL) with the next instruction's ROM address.
        """
        rom_address = 0
        cleaned_instructions = []

        for line_num, raw_line in enumerate(raw_lines, start=1):
            cleaned = self.clean_line(raw_line)
            if not cleaned:
                continue

            if cleaned.startswith("(") and cleaned.endswith(")"):
                label = cleaned[1:-1].strip()
                if not label or not VALID_SYMBOL_REGEX.match(label):
                    self.errors.append(f"Line {line_num}: invalid instruction '{cleaned}' (malformed label name)")
                elif label in self.symbol_table and label not in PREDEFINED_SYMBOLS:
                    # Note: label redefinition is handled gracefully
                    self.symbol_table[label] = rom_address
                else:
                    self.symbol_table[label] = rom_address
            else:
                cleaned_instructions.append((line_num, cleaned))
                rom_address += 1

        return cleaned_instructions

    def translate_a_instruction(self, line_num, line):
        """Translate @value or @symbol to 16-bit binary."""
        symbol = line[1:].strip()
        if not symbol:
            self.errors.append(f"Line {line_num}: invalid instruction '{line}' (empty address in A-instruction)")
            return None

        # Numeric constant
        if symbol.isdigit():
            val = int(symbol)
            if val < 0 or val > 32767:
                self.errors.append(f"Line {line_num}: invalid instruction '{line}' (constant {val} exceeds 15-bit address range [0, 32767])")
                return None
            return f"0{val:015b}"

        # Symbol (variable or predefined/label)
        if not VALID_SYMBOL_REGEX.match(symbol):
            self.errors.append(f"Line {line_num}: invalid instruction '{line}' (invalid symbol name '{symbol}')")
            return None

        if symbol not in self.symbol_table:
            self.symbol_table[symbol] = self.next_variable_address
            self.next_variable_address += 1

        val = self.symbol_table[symbol]
        return f"0{val:015b}"

    def translate_c_instruction(self, line_num, line):
        """Translate dest=comp;jump into 16-bit binary."""
        dest = ""
        comp = ""
        jump = ""
        rest = line

        # Parse dest
        if "=" in rest:
            dest, rest = rest.split("=", 1)
            dest = dest.strip()

        # Parse jump
        if ";" in rest:
            comp, jump = rest.split(";", 1)
            comp = comp.strip()
            jump = jump.strip()
        else:
            comp = rest.strip()

        # Validate comp
        if comp not in COMP_TABLE:
            self.errors.append(f"Line {line_num}: invalid instruction '{line}' (invalid computation expression '{comp}')")
            return None

        # Validate dest
        if dest not in DEST_TABLE:
            self.errors.append(f"Line {line_num}: invalid instruction '{line}' (invalid destination register '{dest}')")
            return None

        # Validate jump
        if jump not in JUMP_TABLE:
            self.errors.append(f"Line {line_num}: invalid instruction '{line}' (invalid jump condition '{jump}')")
            return None

        comp_bits = COMP_TABLE[comp]
        dest_bits = DEST_TABLE[dest]
        jump_bits = JUMP_TABLE[jump]

        return f"111{comp_bits}{dest_bits}{jump_bits}"

    def assemble(self, source_text):
        """
        Assemble Hack assembly source text into binary machine instructions.
        Returns list of 16-bit binary strings or None if errors occurred.
        """
        self.errors = []
        raw_lines = source_text.splitlines()

        # Pass 1: Symbol resolution for labels
        cleaned_instructions = self.first_pass(raw_lines)

        # Pass 2: Binary code generation
        binary_lines = []
        for line_num, instruction in cleaned_instructions:
            if instruction.startswith("@"):
                bin_code = self.translate_a_instruction(line_num, instruction)
            else:
                bin_code = self.translate_c_instruction(line_num, instruction)

            if bin_code is not None:
                binary_lines.append(bin_code)

        if self.errors:
            return None
        return binary_lines

    def assemble_file(self, input_path, output_path=None):
        """Assemble an .asm file to .hack."""
        if not os.path.exists(input_path):
            print(f"Error: input file '{input_path}' not found.", file=sys.stderr)
            return False

        with open(input_path, "r", encoding="utf-8") as f:
            source = f.read()

        binary_lines = self.assemble(source)

        if self.errors:
            print(f"Assembly failed with {len(self.errors)} error(s) in {input_path}:", file=sys.stderr)
            for err in self.errors:
                print(f"  {err}", file=sys.stderr)
            return False

        if output_path is None:
            base, _ = os.path.splitext(input_path)
            output_path = base + ".hack"

        with open(output_path, "w", encoding="utf-8", newline="\n") as f:
            for b_line in binary_lines:
                f.write(b_line + "\n")

        print(f"Successfully assembled '{input_path}' -> '{output_path}' ({len(binary_lines)} instructions).")
        return True


def main():
    if len(sys.argv) < 2:
        print("Usage: python assembler.py <file.asm> [<file.hack>]")
        sys.exit(1)

    asm_file = sys.argv[1]
    hack_file = sys.argv[2] if len(sys.argv) > 2 else None

    assembler = HackAssembler()
    success = assembler.assemble_file(asm_file, hack_file)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
