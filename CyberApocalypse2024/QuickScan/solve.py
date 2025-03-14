from capstone import *
from elftools.elf.elffile import ELFFile
from pwn import *

# Get the address of the start function
def get_start_address(ELF):

    with open('f', 'rb') as mem_file:
        elf_file = ELFFile(mem_file)
        # Assuming the architecture is x86-64
        start_address = elf_file.header.e_entry
    return start_address

# Get the image base of the ELF file
def get_image_base(ELF):
    with open('f', 'rb') as mem_file:
        elf_file = ELFFile(mem_file)
        program_headers = elf_file.iter_segments()
        # Find the first LOAD segment and get its virtual address (VADDR)
        for segment in program_headers:
            if segment.header.p_type == 'PT_LOAD':
                return segment.header.p_vaddr
    
        return None


# Load the ELF file and disassemble its code section
def disassemble_elf(ELF):
    open('f', 'wb').write(ELF)
    start_address = get_start_address(ELF)
    base_address = get_image_base(ELF)
    elf_data = ELF[(start_address - base_address):]
    address = 0
    md = Cs(CS_ARCH_X86, CS_MODE_64)
    ecx_value = 0
    for i in md.disasm(elf_data, start_address - base_address):
        # Extract immediate values loaded into registers
        if i.mnemonic == 'lea' and 'rsi' in i.op_str:
            # Extract immediate value loaded into rsi
            offset = int(i.op_str.split()[3][2:-1],16)
            address = i.size + i.address + (offset if i.op_str.split()[2] == '+' else -offset)
        elif i.mnemonic == 'mov' and 'ecx' in i.op_str:
            # Extract immediate value loaded into ecx
            ecx_value = i.op_str.split(',')[1].strip()
        
    return ELF[address:address + 0x18].hex()

if __name__ == "__main__":
    # Replace with the path to your ELF file
    r = remote('94.237.57.88', 34598)
    for i in range(129):
        r.recvuntil("ELF:  ")
        data = r.recvline().rstrip()
        ELF = base64.b64decode(data)
        r.recvuntil("Bytes? ")
        answer = disassemble_elf(ELF)
        r.sendline(answer)

    r.interactive()
