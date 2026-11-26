# Nand2Tetris Hardware Implementations

This repository contains Hardware Description Language (HDL) implementations for the [Nand2Tetris](https://www.nand2tetris.org/) course ("The Elements of Computing Systems" by Noam Nisan and Shimon Schocken), along with the Capstone project modules.

## Repository Structure

```text
.
├── PROJECT 1/    # Elementary and multi-bit logic gates
├── PROJECT 2/    # Boolean arithmetic and ALU
├── PROJECT 3/    # Sequential logic and memory systems (Registers, RAM, PC)
├── PROJECT 5/    # Computer architecture (Memory, CPU, Computer)
└── Capstone/     # Capstone modules
    ├── PartA/    # Hardware architecture implementation & simulator verification
    ├── PartB/    # Assembler & machine language
    └── PartC/    # Software application / OS level
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

## Capstone Project

The Capstone organizes the comprehensive computer architecture implementation:

### Part A: Complete Architecture & Hardware Verification (`Capstone/PartA/`)
- **`Memory.hdl`**: Address decoding for data memory, screen, and keyboard mapping.
- **`CPU.hdl`**: Execution unit for Hack instructions, decoding, arithmetic operations, and conditional jumps.
- **`Computer.hdl`**: Top-level integration of CPU, Memory, and Instruction ROM.
- **`screenshot/`**: Verification outputs and test execution proof across test scripts (`ComputerAdd`, `ComputerMax`, `ComputerRect`, `CPU`, `CPU-External`, `Memory`).

### Part B & Part C (`Capstone/PartB/`, `Capstone/PartC/`)
- Scaffolded modules for assembler, software translation, and application execution.

---

## How to Test

You can test any of these HDL implementations using the **Nand2Tetris Hardware Simulator**:

1. Download the [Nand2Tetris Software Suite](https://www.nand2tetris.org/software).
2. Launch `HardwareSimulator.bat` (Windows) or `HardwareSimulator.sh` (Mac/Linux).
3. Load any `.hdl` file from the respective project folder along with its corresponding `.tst` test script.
4. Run the test script and verify that the output matches the `.cmp` file.
