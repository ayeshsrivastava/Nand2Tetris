# Nand2Tetris - Project 1: Boolean Logic & Elementary Logic Gates

This repository contains Hardware Description Language (HDL) implementations for **Project 01** of the [Nand2Tetris](https://www.nand2tetris.org/) course ("The Elements of Computing Systems" by Noam Nisan and Shimon Schocken).

## Overview

The goal of Project 01 is to build basic Boolean logic gates starting from the primitive **Nand** gate. Using elementary gates, higher-level multi-bit and multi-way logic gates are constructed step-by-step.

## Implemented Chips

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

## How to Test

You can test these HDL implementations using the **Nand2Tetris Hardware Simulator**:

1. Download the [Nand2Tetris Software Suite](https://www.nand2tetris.org/software).
2. Launch `HardwareSimulator.bat` (Windows) or `HardwareSimulator.sh` (Mac/Linux).
3. Load any `.hdl` file along with its corresponding `.tst` test script.
4. Run the script and verify that the test output matches the `.cmp` file.
