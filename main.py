class BytecodeInterpreter:
    def __init__(self, bytecode):
        self.bytecode = bytecode
        self.pc = 0
        self.registers = {}

    def execute(self):
        while self.pc < len(self.bytecode):
            opcode = self.bytecode[self.pc]
            self.pc += 1
            if opcode == 1:
                register = self.bytecode[self.pc]
                self.pc += 1
                value = self.bytecode[self.pc]
                self.pc += 1
                self.registers[register] = value
            elif opcode == 2:
                register1 = self.bytecode[self.pc]
                self.pc += 1
                register2 = self.bytecode[self.pc]
                self.pc += 1
                result = self.registers[register1] + self.registers[register2]
                self.registers[register1] = result
            elif opcode == 3:
                register1 = self.bytecode[self.pc]
                self.pc += 1
                register2 = self.bytecode[self.pc]
                self.pc += 1
                result = self.registers[register1] - self.registers[register2]
                self.registers[register1] = result
            elif opcode == 4:
                register1 = self.bytecode[self.pc]
                self.pc += 1
                register2 = self.bytecode[self.pc]
                self.pc += 1
                result = self.registers[register1] * self.registers[register2]
                self.registers[register1] = result
            elif opcode == 5:
                register1 = self.bytecode[self.pc]
                self.pc += 1
                register2 = self.bytecode[self.pc]
                self.pc += 1
                result = self.registers[register1] / self.registers[register2]
                self.registers[register1] = result
            elif opcode == 6:
                register = self.bytecode[self.pc]
                self.pc += 1
                print(self.registers[register])
            elif opcode == 7:
                register = self.bytecode[self.pc]
                self.pc += 1
                value = input()
                self.registers[register] = int(value)

bytecode = [1, 1, 10, 2, 1, 2, 3, 1, 2, 4, 1, 2, 5, 1, 2, 6, 1, 7, 1]
interpreter = BytecodeInterpreter(bytecode)
interpreter.execute()