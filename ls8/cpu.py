"""CPU functionality."""

import sys

# Operation Codes = Op Codes
HLT = 0b00000001
PRN = 0b01000111
LDI = 0b10000010
PUSH = 0b01000101
POP = 0b01000110


# ALU
MUL = 0b10100010
ADD = 0b10100000
CMP = 0b10100111


class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        # Create 256 bytes of RAM

        self.ram = [0] * 256

        # Create 8 registers

        self.reg = [0] * 8

        # Set the program counter to 0

        self.pc = 0

        self.sp = 7

        self.fl = 0

        self.dispatchable = {
            MUL: self.mul,
            ADD: self.add,
            PRN: self.prn,
            LDI: self.ldi,
        }



    def load(self,filename):
        """Load a program into memory."""

        # For now, we've just hardcoded a program:

        """Load a program into memory."""

        address = 0
        program = []

        with open(filename) as f:
            for line in f:
                comment_split = line.split("#")
                maybe_binary_number = comment_split[0]

                try:
                    x = int(maybe_binary_number, 2)
                    program.append(x)
                except:
                    continue
        print(program)

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        elif op == "SUB":
            self.reg[reg_a] -= self.reg[reg_b]
        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    def ram_read(self, address):
        """
        Reads the value at the designated address of RAM
        """
        return self.ram[address]

    def ram_write(self, address, value):
        """
        Writes a value to RAM at the designate address
        """
        self.ram[address] = value

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()
    
    def mul(self, reg_a, reg_b):
        self.alu("MUL", reg_a, reg_b)  
        self.pc += 3 

    def add(self, reg_a, reg_b):
        self.alu("ADD", reg_a, reg_b)
        self.pc += 3

    def prn(self, reg_a, reg_b):
        print(self.reg[reg_a])
        self.pc += 2

    def ldi(self, reg_a, reg_b):
        self.reg[reg_a] = reg_b
        self.pc += 3

    def run(self):
        """Run the CPU."""

        running = True

        while running:
            ir = self.ram_read(self.pc)
            reg_a = self.ram_read(self.pc + 1)
            reg_b = self.ram_read(self.pc + 2)          
            if ir == HLT:
                running = False
            else:
                self.dispatchable[ir](reg_a, reg_b)
        self.trace()
