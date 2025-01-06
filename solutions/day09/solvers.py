from aoc.utils import parsing

input_parser = parsing.split_lines

def part1(input_data):
    disk = []
    open_blocks = []
    occupied_blocks = []

    isFile = True
    id = 0
    for size in map(int, input_data[0]):
        if isFile and size:
            disk += [id]*size
            occupied_blocks.append((len(disk) - size, len(disk)-1, id)) # QUEUE: (start_index, end_index, id)
            id += 1
        elif size:
            disk += ["."]*size
            open_blocks.append((len(disk) - size, len(disk)-1)) # STACK: (start_index, end_index)
        isFile = not isFile

    while open_blocks and open_blocks[0][0] < occupied_blocks[-1][0]:
        block = open_blocks.pop(0) 
        file = occupied_blocks.pop()

        if block[1]-block[0] == file[1]-file[0]: # perfect fit
            disk[block[0]:block[1]+1] = [file[2]]*(file[1]-file[0]+1) # write
            disk[file[0]:file[1]+1] = ["."]*(file[1]-file[0]+1) # clear
        elif block[1]-block[0] > file[1]-file[0]: # memory gap larger than file
            disk[block[0]:block[0]+file[1]-file[0]+1] = [file[2]]*(file[1]-file[0]+1) # write
            disk[file[0]:file[1]+1] = ["."]*(file[1]-file[0]+1) # clear
            open_blocks.insert(0, (block[0]+file[1]-file[0]+1, block[1])) # push to open blocks queue
        else: # memory gap smaller than file
            disk[block[0]:block[1]+1] = [file[2]]*(block[1]-block[0]+1) # write
            disk[file[1]-(block[1]-block[0]):file[1]+1] = ["."]*(block[1]-block[0]+1) # clear
            occupied_blocks.append((file[0], file[1]-(block[1]-block[0])-1, file[2]))
    
    checksum = 0
    for i in range(len(disk)):
        if disk[i] == ".":
            return checksum
        checksum += i*disk[i]

def part2(input_data):
    disk = []
    open_blocks = []
    occupied_blocks = []

    isFile = True
    id = 0
    for size in map(int, input_data[0]):
        if isFile and size:
            disk += [id]*size
            occupied_blocks.append((len(disk) - size, len(disk)-1, id)) # QUEUE: (start_index, end_index, id)
            id += 1
        elif size:
            disk += ["."]*size
            open_blocks.append((len(disk) - size, len(disk)-1)) # STACK: (start_index, end_index)
        isFile = not isFile

    while occupied_blocks and open_blocks[0][0] < occupied_blocks[-1][0]:
        file = occupied_blocks.pop()

        for i in range(len(open_blocks)):
            block = open_blocks[i]
            if block[0] > file[0]: break

            if block[1]-block[0] == file[1]-file[0]: # perfect fit
                disk[block[0]:block[1]+1] = [file[2]]*(file[1]-file[0]+1) # write
                disk[file[0]:file[1]+1] = ["."]*(file[1]-file[0]+1) # clear
                open_blocks.pop(i)
                break
            elif block[1]-block[0] > file[1]-file[0]: # memory gap larger than file
                disk[block[0]:block[0]+file[1]-file[0]+1] = [file[2]]*(file[1]-file[0]+1) # write
                disk[file[0]:file[1]+1] = ["."]*(file[1]-file[0]+1) # clear
                open_blocks[i] = ((block[0]+file[1]-file[0]+1, block[1])) # push to open blocks queue
                break
        
    checksum = 0
    for i in range(len(disk)):
        if disk[i] == ".": continue
        checksum += i*disk[i]

    return checksum