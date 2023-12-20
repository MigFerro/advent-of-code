#!/bin/bash
import sys
from collections import deque
from math import lcm

def read_input():
    input_file_code = sys.argv[-1]
    if input_file_code == 't':
        return open('test_input.txt', 'r').read().strip()
    else: 
        return open('input.txt', 'r').read().strip()

def parse_input():
    f = read_input()
    s = f.split("\n")

    nodes = {}

    for line in s:
        node, links = line.split(" -> ")
        node_type = node[0]
        name = node[1:]
        links = links.split(", ")
        nodes[name] = {'type': node_type, 'links': links, 'state': False if node_type == '%' else True}

    get_conv_inputs(nodes)

    return nodes


def get_state(nodes):
    state = []
    for k in nodes.keys():
        state.append((k, nodes[k]['state']))
    return tuple(state)

def get_conv_inputs(nodes):
    conv_nodes = [k for k in nodes.keys() if nodes[k]['type'] == '&']
    for ck in conv_nodes:
        inputs = {}
        for k in nodes.keys():
            if ck in nodes[k]['links']:
                inputs[k] = False

        nodes[ck]['inputs'] = inputs

def get_conv_state(conv_name, nodes):
    for v in nodes[conv_name]['inputs'].values():
        if not v:
            return True
    return False



def part1():
    nodes = parse_input()
    n = 0
    sent = {0: 0, 1:0}

    while n < 1000:
        
        # button -low -> boradcaster
        n += 1
        sent[0] += 1
        to_process = deque()

        for l in nodes['roadcaster']['links']:
            to_process.append((l,0,'roadcaster'))
        
        while to_process:
            node, sig, sender = to_process.popleft()
            t = nodes[node]['type']
            links = nodes[node]['links']
            st = nodes[node]['state']
            sent[sig] += 1

            if t == '%':
                if sig:
                    continue
                else:
                    st = not st
                    nodes[node]['state'] = st

            elif t == '&':
                nodes[node]['inputs'][sender] = sig
                st = get_conv_state(node, nodes)
                nodes[node]['state'] = st

            for l in links:
                if l in nodes:
                    to_process.append((l,st,node))
                else:
                    sent[st] += 1
                
    print(sent[0] * sent[1])

def part2():
    nodes = parse_input()
    n = 0

    (rxf,) = [k for k in nodes.keys() if 'rx' in nodes[k]['links']]
    cycle_lengths = {}
    seen = {name: 0 for name in nodes[rxf]['inputs']}

    while True:

        # button -low -> boradcaster
        n += 1
        to_process = deque()

        for l in nodes['roadcaster']['links']:
            to_process.append((l,0,'roadcaster'))
        
        while to_process:
            node, sig, sender = to_process.popleft()
            t = nodes[node]['type']
            links = nodes[node]['links']
            st = nodes[node]['state']

            if t == '%':
                if sig:
                    continue
                else:
                    st = not st
                    nodes[node]['state'] = st

            elif t == '&':
                nodes[node]['inputs'][sender] = sig
                st = get_conv_state(node, nodes)
                nodes[node]['state'] = st
                if node == rxf and sig:
                    seen[sender] += 1

                    if sender not in cycle_lengths:
                        cycle_lengths[sender]= n
                    else:
                        assert n == seen[sender] * cycle_lengths[sender]

                    if all(seen.values()):
                        ans = 1
                        for x in cycle_lengths.values():
                            ans = lcm(ans,x)
                        print(ans)
                        exit(0)

            for l in links:
                if l in nodes:
                    to_process.append((l,st,node))
                
part1()
part2()
