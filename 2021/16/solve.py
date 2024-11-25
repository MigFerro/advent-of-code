#!/bin/bash
import sys

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

f = read_input()

alpha_to_hex = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
    }


bb = ''
for c in f:
    bb += alpha_to_hex[c]
# print(bb)

def get_next_packet(i):
    packet = {}
    ver = int(bb[i:i+3], 2)
    packet['version'] = ver
    i += 3
    id = int(bb[i:i+3], 2)
    packet['id'] = id
    i += 3
    if id == 4: #literal
        packet['type'] = 'literal'
        flag = True 
        l = 0
        curr = ''
        while flag:
            group = bb[i:i+5]
            curr += group[1:]
            i += 5
            if group[0] == '0':
                flag = False
        packet['val'] = int(curr, 2)
    else: #operator
        packet['type'] = 'operator'
        packet['sub'] = []
        lID = bb[i]
        i += 1
        if lID == '0': #15 bit length
            l = bb[i:i+15]
            i += 15
            ll = int(l, 2) + i
            while i < ll:
                i, p = get_next_packet(i)
                packet['sub'].append(p)
                
        elif lID == '1': #11 bit length
            l = bb[i:i+11]
            i += 11
            npacks = int(l, 2)
            for _ in range(npacks):
                i, p = get_next_packet(i)
                packet['sub'].append(p)
        else:
            assert False

    return i, packet


packets = []
i = 0
while i < len(bb):
    if len(bb) - i < 8:
        break
    i, packet = get_next_packet(i)
    packets.append(packet)

def get_version_sum(packet):
    res = packet['version']
    if 'sub' not in packet.keys():
        return res

    for p in packet['sub']:
        res += get_version_sum(p) 

    return res

def get_value(packet):
    if 'sub' not in packet.keys():
        return packet['val']
    if packet['id'] == 0:
        s = 0
        for p in packet['sub']:
            s += get_value(p)
        return s
    elif packet['id'] == 1:
        s = 1
        for p in packet['sub']:
            s *= get_value(p)
        return s
    elif packet['id'] == 2:
        min = float('inf')
        for p in packet['sub']:
            v = get_value(p)
            if v < min:
                min = v
        assert min != float('inf')
        return min
    elif packet['id'] == 3:
        max = 0
        for p in packet['sub']:
            v = get_value(p)
            if v > max:
                max = v
        return max
    elif packet['id'] == 5:
        if get_value(packet['sub'][0]) > get_value(packet['sub'][1]):
            return 1
        return 0
    elif packet['id'] == 6:
        if get_value(packet['sub'][0]) < get_value(packet['sub'][1]):
            return 1
        return 0
    elif packet['id'] == 7:
        if get_value(packet['sub'][0]) == get_value(packet['sub'][1]):
            return 1
        return 0
    assert False


res = 0
for p in packets:
    res += get_version_sum(p)

print(res)
print(get_value(packets[0]))

