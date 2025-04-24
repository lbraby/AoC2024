from aoc.utils import parsing

import math

input_parser = parsing.split_lines

# LITERAL OPERANDS:
#   the value is the operand itself
# COMBO OPERANDS:
#   0-3: literal values 0-3
#   4: value of register A
#   5: value of register B
#   6: value of register C

combo_operands = [0, 1, 2, 3, 0, 0, 0]
instruction_list = []
output = []
pointer = 0

def parse_input(input_data: list[str]):
    global combo_operands, instruction_list

    combo_operands[4] = int(input_data[0].split(":")[1])
    combo_operands[5] = int(input_data[1].split(":")[1])
    combo_operands[6] = int(input_data[2].split(":")[1])

    instruction_list = [int(num) for num in input_data[4].split(":")[1].split(",")]
    

def perform_instruction():
    global combo_operands, instruction_list, output, pointer

    instruction = instruction_list[pointer]
    operand = instruction_list[pointer+1]

    if instruction == 0:
        combo_operands[4] = combo_operands[4] // (2**combo_operands[operand])
    elif instruction == 1:
        combo_operands[5] = operand ^ combo_operands[5]
    elif instruction == 2:
        combo_operands[5] = combo_operands[operand] % 8
    elif instruction == 3:
        if combo_operands[4] != 0:
            pointer = operand
            return
    elif instruction == 4:
        combo_operands[5] = combo_operands[5] ^ combo_operands[6]
    elif instruction == 5:
        output.append(str(combo_operands[operand] % 8))
    elif instruction == 6:
        combo_operands[5] = combo_operands[4] // (2**combo_operands[operand])
    elif instruction == 7:
        combo_operands[6] = combo_operands[4] // (2**combo_operands[operand])

    pointer += 2

def part1(input_data):
    parse_input(input_data)

    while pointer < len(instruction_list) - 1:
        perform_instruction()

    return ",".join(output)

def compute(program: list[int], a: int, b: int = 0, c: int = 0) -> list[int]:
    def combo(val: int) -> int:
        assert val != 7, "Invalid combo value"
        if val <= 3:
            return val
        reg_map = {4: a, 5: b, 6: c}
        return reg_map[val]

    output = []
    ip = 0
    while ip < len(program) - 1:
        opcode = program[ip]
        operand = program[ip + 1]
        match opcode:
            case 0: # adv
                a = a >> combo(operand)
            case 1: # bxl
                b = b ^ operand
            case 2: # bst
                b = combo(operand) % 8
            case 3: # jnz
                if a != 0:
                    ip = operand
                    continue
            case 4: # bxc
                b = b ^ c
            case 5: # out
                output.append(combo(operand) % 8)
            case 6: # bdv
                b = a >> combo(operand)
            case 7: # cdv
                c = a >> combo(operand)
        ip += 2

    return output

def part2(input_data):
    program = [int(num) for num in input_data[4].split(":")[1].split(",")]
    
    candidates = [0]
    for l in range(len(program)):
        next_candidates = []
        for val in candidates:
            for i in range(8):
                target = (val << 3) + i # shift A left by 3 since only operation performed on A in script is shift right 3
                if compute(program, target) == program[-l - 1 :]:
                    next_candidates.append(target)
        candidates = next_candidates

    print(min(candidates))
