
with open('input_09.txt') as f:
    content = f.read()

test = '''7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3'''


def get_pts(text):
    points = []
    for line in text.split():
        pair = line.split(',')
        points.append((int(pair[0]), int(pair[1])))
    return points

def area(p1, p2):
    return (abs(p2[0]-p1[0]) +1 )*(abs(p2[1]-p1[1])+1)

def q1(pts):
    cur_best = 0
    for p1 in pts:
        for p2 in pts:
            p12_area = area(p1, p2)
            if p12_area > cur_best:
                cur_best = p12_area
    print(cur_best)

def no_pts_in_middle(pts, p1, p2):
    # edge is fine?
    for x, y in pts:
        between_x = (p1[0] > x and x > p2[0]) or (p1[0] < x and x < p2[0])
        if between_x:
            between_y = (p1[1] > y and y > p2[1]) or (p1[1] < y and y < p2[1])
            if between_y:
                return False
    return True

# still need to check points on border

def q2(pts):
    cur_best = 0
    for p1 in pts:
        for p2 in pts:
            p12_area = area(p1, p2)
            if p12_area > cur_best and no_pts_in_middle(pts, p1, p2):
                print(p1, p2)
                cur_best = p12_area
    print(cur_best)

pts = get_pts(test)
print(no_pts_in_middle(pts, (2,3), (7,1)))
q2(pts)
