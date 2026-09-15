# Nand2Tetris Hardware Implementations

This repository contains Hardware Description Language (HDL) implementations for the [Nand2Tetris](https://www.nand2tetris.org/) course ("The Elements of Computing Systems" by Noam Nisan and Shimon Schocken).

## Repository Structure

```text
.
├── PROJECT 1/    # Elementary and multi-bit logic gates
└── PROJECT 2/    # Boolean arithmetic and adders
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

Project 02 builds arithmetic chips starting from basic adder components up to multi-bit adders.

### Implemented Chips (`PROJECT 2/`)

| Chip Name | Description | Built From |
| :--- | :--- | :--- |
| `HalfAdder.hdl` | Computes the sum of 2 bits | `Xor`, `And` |
| `FullAdder.hdl` | Computes the sum of 3 bits | `HalfAdder`, `Or` |
| `Add16.hdl` | 16-bit Adder (adds two 16-bit numbers) | `HalfAdder`, `FullAdder` |

---

## How to Test

You can test any of these HDL implementations using the **Nand2Tetris Hardware Simulator**:

1. Download the [Nand2Tetris Software Suite](https://www.nand2tetris.org/software).
2. Launch `HardwareSimulator.bat` (Windows) or `HardwareSimulator.sh` (Mac/Linux).
3. Load any `.hdl` file from `PROJECT 1/` or `PROJECT 2/` along with its corresponding `.tst` test script.
4. Run the test script and verify that the output matches the `.cmp` file.
