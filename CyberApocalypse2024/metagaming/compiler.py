from sys import stdin

program = []

def py_from_opcode(instr):
    match int(instr[0]):
        case 0:
            return f"regs[{instr[1]}] = flag[{instr[2]}]\n"
        case 1: 
            return f"regs[{instr[1]}] = BitVecVal({instr[2]}, 32) * 1\n"
        case 2:
            return f"regs[{instr[1]}] ^= {instr[2]}\n"
        case 3:
            return f"regs[{instr[1]}] ^= regs[{instr[2]}]\n"
        case 4:
            return f"regs[{instr[1]}] |= {instr[2]}\n"
        case 5:
            return f"regs[{instr[1]}] |= regs[{instr[2]}]\n"
        case 6:
            return f"regs[{instr[1]}] &= {instr[2]}\n"
        case 7:
            return f"regs[{instr[1]}] &= regs[{instr[2]}]\n"
        case 8: 
            return f"regs[{instr[1]}] += {instr[2]}\n"
        case 9:
            return f"regs[{instr[1]}] += regs[{instr[2]}]\n"
        case 10:
            return f"regs[{instr[1]}] -= {instr[2]}\n"
        case 11:
            return f"regs[{instr[1]}] -= regs[{instr[2]}]\n"
        case 12:
            return f"regs[{instr[1]}] *= {instr[2]}\n"
        case 13:
            return f"regs[{instr[1]}] *= regs[{instr[2]}]\n"
        case 14:
            return f""
        case 15:
            return f""
        case 16:
            return f"regs[{instr[1]}] = rotr(regs[{instr[1]}], {instr[2]})\n"
        case 17:
            return f"regs[{instr[1]}] = rotr(regs[{instr[1]}], regs[{instr[2]}])\n"
        case 18:
            return f"regs[{instr[1]}] = rotl(regs[{instr[1]}], {instr[2]})\n"
        case 19:
            return f"regs[{instr[1]}] = rotl(regs[{instr[1]}], regs[{instr[2]}])\n"
        case 20: 
            return f"regs[{instr[1]}] = regs[{instr[1]}] = regs[{instr[2]}]\n"
        case 21:
            return f"regs[{instr[1]}] = regs[{instr[1]}] = BitVecVal(0, 32) * 0 \n"
        case 22:
            return f"regs[{instr[1]}] = LShR(regs[{instr[1]}], {instr[2]})\n"
        case 23:
            return f"regs[{instr[1]}] = LShR(regs[{instr[1]}], regs[{instr[2]}])\n"
        case 24:
            return f"regs[{instr[1]}] <<= {instr[2]}\n"
        case 25:
            return f"regs[{instr[1]}] <<= regs[{instr[2]}]\n"
        case _:
            return 0



for line in stdin:
    program.append(line.split())

with output as open("output.py", 'w'):
    for instruction in program:
        output.write(py_from_opcode(instruction))

