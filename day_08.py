
import numpy as np

with open('input_08.txt') as f:
    content = f.read()

test = '''162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689'''

def calc_distances(boxes):
    dists = np.zeros((len(boxes), len(boxes)))
    for i, box1 in enumerate(boxes):
        for j, box2 in enumerate(boxes):
            if dists[j, i] != 0:
                dists[i, j] = dists[j, i]
            else:
                dists[i, j] = np.linalg.norm(box1-box2)
            if dists[i,j] == 0:
                dists[i, j] = np.inf
    return dists



def connect_boxes(links, boxes, dists):
    circuits = [] #[[i] for i in range(len(boxes))]
    for _ in range(links):
        # finds next shortest link
        ind = np.unravel_index(np.argmin(dists, axis=None), dists.shape)
        if type(ind) != tuple:
            print(ind)
        # print(boxes[ind[0]], boxes[ind[1]])
        # print(ind)
        # check if any of the boxes b are in an existing circuit c
        circuit_idx = -1
        to_delete = -1
        for i, c in enumerate(circuits):
            if circuit_idx == -1:
                if ind[0] in c:
                    circuit_idx = i
                    circuits[i].add(ind[1])
                elif ind[1] in c:
                    circuit_idx = i
                    circuits[i].add(ind[0])
            else: # connect the two circuits
                if ind[0] in c or ind[1] in c:
                    circuits[i] = c.union(circuits[circuit_idx])
                    to_delete = circuit_idx
        if to_delete >= 0:
            circuits.pop(to_delete)
        
        # if not, add new circuit with one of the indices
        if circuit_idx == -1:
            circuits.append({ind[0], ind[1]})
        
        # change dist between the two as inf
        dists[ind[0], ind[1]] = dists[ind[1], ind[0]] = np.inf
        
        #print([[i  for i in c] for c in circuits])
    return circuits

def q1(circuits):
    lengths = sorted([len(c) for c in circuits], reverse=True)
    print(lengths[0] * lengths[1] * lengths[2])
    
lines = content.split()
boxes = np.array([[int(i) for i in line.split(',')] for line in lines])
dists = calc_distances(boxes)
print('finished distances')
circuits = connect_boxes(1000, boxes, dists)

q1(circuits)
