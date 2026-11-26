# Nand2Tetris Hardware Implementations & Capstone Project

This repository contains Hardware Description Language (HDL) implementations for the [Nand2Tetris](https://www.nand2tetris.org/) course ("The Elements of Computing Systems" by Noam Nisan and Shimon Schocken), along with the complete Capstone Project modules.

**Student Roll No:** 2501420061  
**Personal Parameter:** $K = 61$  

---

## Repository Structure

```text
.
├── PROJECT 1/    # Elementary and multi-bit logic gates
├── PROJECT 2/    # Boolean arithmetic and ALU
├── PROJECT 3/    # Sequential logic and memory systems (Registers, RAM, PC)
├── PROJECT 5/    # Computer architecture (Memory, CPU, Computer)
└── Capstone/     # Capstone project modules (Parts A, B, and C)
    ├── PartA/    # Hardware architecture implementation & simulator verification
    ├── PartB/    # Hack Assembler in Python (with K mod 3 = 1 error handling)
    └── PartC/    # Box interactive program in Hack assembly (for K = 61)
```

---

## Project 1: Boolean Logic & Elementary Logic Gates

Project 01 builds elementary, multi-bit, and multi-way logic gates starting from the primitive **Nand** gate.

### Implemented Chips (`PROJECT 1/`)

| Chip Name | Description | Built From |
| :--- | :--- | :--- |
| `Not.hdl` | Bitwise NOT gate | `Nand` |
| `And.hdl` | Bitwise AND gate | `Nand` |
| `Or.hdl` | Bitwise OR gate | `Nand`, `Not` |
| `Xor.hdl` | Exclusive OR gate | `Nand`, `Or`, `And` |
| `Mux.hdl` | 2-to-1 Multiplexor | `Not`, `And`, `Or` |
| `DMux.hdl` | 1-to-2 Demultiplexor | `Not`, `And` |
| `Not16.hdl` | 16-bit NOT gate | `Not` |
| `And16.hdl` | 16-bit AND gate | `And` |
| `Or16.hdl` | 16-bit OR gate | `Or` |
| `Mux16.hdl` | 16-bit 2-to-1 Multiplexor | `Mux` |
| `Or8Way.hdl` | 8-input OR gate | `Or` |
| `Mux4Way16.hdl` | 4-way 16-bit Multiplexor | `Mux16` |
| `Mux8Way16.hdl` | 8-way 16-bit Multiplexor | `Mux4Way16` |
| `DMux4Way.hdl` | 1-to-4 Demultiplexor | `DMux` |
| `DMux8Way.hdl` | 1-to-8 Demultiplexor | `DMux4Way` |

---

## Project 2: Boolean Arithmetic

Project 02 builds arithmetic chips starting from basic adder components up to a full Arithmetic Logic Unit (ALU).

### Implemented Chips (`PROJECT 2/`)

| Chip Name | Description | Built From |
| :--- | :--- | :--- |
| `HalfAdder.hdl` | Computes the sum of 2 bits | `Xor`, `And` |
| `FullAdder.hdl` | Computes the sum of 3 bits | `HalfAdder`, `Or` |
| `Add16.hdl` | 16-bit Adder (adds two 16-bit numbers) | `HalfAdder`, `FullAdder` |
| `Inc16.hdl` | 16-bit Incrementer ($out = in + 1$) | `Add16` |
| `ALU.hdl` | 16-bit Arithmetic Logic Unit | `Mux16`, `Not16`, `Add16`, `And16`, `Or8Way` |

---

## Project 3: Sequential Logic & Memory Systems

Project 03 constructs sequential memory components, progressing from a 1-bit register to memory hierarchies (RAM8 to RAM16K) and a Program Counter (PC), built upon the primitive **Data Flip-Flop (DFF)**.

### Implemented Chips (`PROJECT 3/`)

| Chip Name | Description | Built From |
| :--- | :--- | :--- |
| `Bit.hdl` | 1-bit memory register | `DFF`, `Mux` |
| `Register.hdl` | 16-bit memory register | `Bit` |
| `RAM8.hdl` | 8-register 16-bit RAM ($8 \times 16\text{-bit}$) | `Register`, `DMux8Way`, `Mux8Way16` |
| `RAM64.hdl` | 64-register 16-bit RAM ($64 \times 16\text{-bit}$) | `RAM8`, `DMux8Way`, `Mux8Way16` |
| `RAM512.hdl` | 512-register 16-bit RAM ($512 \times 16\text{-bit}$) | `RAM64`, `DMux8Way`, `Mux8Way16` |
| `RAM4K.hdl` | 4096-register 16-bit RAM ($4096 \times 16\text{-bit}$) | `RAM512`, `DMux8Way`, `Mux8Way16` |
| `RAM16K.hdl` | 16384-register 16-bit RAM ($16384 \times 16\text{-bit}$) | `RAM4K`, `DMux8Way`, `Mux8Way16` |
| `PC.hdl` | 16-bit Program Counter (with reset, load, inc) | `Register`, `Inc16`, `Mux16` |

---

## Project 5: Computer Architecture

Project 05 brings together the processing unit, memory units, and peripheral addressing to build the complete Hack Computer platform.

### Implemented Chips (`PROJECT 5/`)

| Chip Name | Description | Built From |
| :--- | :--- | :--- |
| `Memory.hdl` | Complete Hack address space (RAM16K, Screen, Keyboard) | `RAM16K`, `Screen`, `Keyboard`, `DMux4Way`, `Mux4Way16` |
| `CPU.hdl` | Hack Central Processing Unit | `ALU`, `ARegister`, `DRegister`, `PC`, `Mux16` |
| `Computer.hdl` | Complete Hack Computer system | `CPU`, `Memory`, `ROM32K` |

---

## Capstone Project: Make the Computer Draw a Box

### Student Configuration
- **Roll No:** `2501420061`
- **$K$ (Last two digits):** `61`
- **$K \pmod 3$:** $61 \pmod 3 = 1$
- **$K \pmod 4$:** $61 \pmod 4 = 1$

### Part A: Computer Architecture & Hardware Verification (`Capstone/PartA/`)
- **`Memory.hdl`**, **`CPU.hdl`**, **`Computer.hdl`**: Complete Hack computer implementation.
- **`screenshot/`**: Official Hardware Simulator verification test screenshots for `ComputerAdd`, `ComputerMax`, `ComputerRect`, `CPU`, `CPU-External`, and `Memory`.

### Part B: Hack Assembler in Python (`Capstone/PartB/`)
- **`assembler.py`**: Two-pass assembler translating Hack assembly (`.asm`) into binary machine code (`.hack`).
  - Predefined symbols (`R0`-`R15`, `SP`, `LCL`, `ARG`, `THIS`, `THAT`, `SCREEN`, `KBD`).
  - Label resolution and variable address allocation starting at RAM 16.
  - **Extra Feature for $K \pmod 3 = 1$**: Robust error diagnostics with exact source line numbers (e.g. `Line 7: invalid instruction '<line>' (<reason>)`) without crashing.
- **Tests**: Validated on `Add.asm`, `Max.asm`, and error reporting verified on `invalid_test.asm`.

### Part C: Interactive Box Program (`Capstone/PartC/`)
- **`Box.asm`**: Written in Hack assembly for $K = 61$:
  - **Start Row:** Row $K = 61$ ($\text{address} = \text{SCREEN} + 32 \times 61 = 18336$).
  - **Height:** 20 rows tall (rows 61 to 80).
  - **Width:** $16 \times ((K \pmod 4) + 1) = 16 \times (1 + 1) = 32$ pixels wide (2 words from left edge).
  - **Interaction:** Checks `@KBD`. While any key is pressed, draws the black box. When the key is released, clears the box.
- **`Box.hack`**: Machine code assembled directly with our Part B `assembler.py`.

---

## How to Run & Test

### Running the Assembler (Part B)
```bash
python Capstone/PartB/assembler.py Capstone/PartB/Add.asm
python Capstone/PartB/assembler.py Capstone/PartC/Box.asm Capstone/PartC/Box.hack
```

### Running Hardware & CPU Emulators
1. Launch the **Nand2Tetris Hardware Simulator** to test HDL files with `.tst` scripts.
2. Launch the **Nand2Tetris CPU Emulator** or **Hardware Simulator** to load and run `Box.hack` / `Box.tst`.
