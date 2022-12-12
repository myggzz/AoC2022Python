file_name = "input.txt"
with open(file_name, 'r') as f:
    data = f.read().split('\n')

def is_close(h, t):
    h_x, h_y, t_x, t_y = h[0], h[1], t[0], t[1]

    if abs(h_x - t_x) > 1 or abs(h_y - t_y) > 1:
        return False
    return True

knots = [[0, 0] for i in range(10)]

steps_arr = []

for com in data:
    direction, steps = com.split(' ')[0], int(com.split(' ')[1])
    for step in range(steps):
        if direction == 'R': knots[0][0] += 1
        elif direction == 'L': knots[0][0] -= 1
        elif direction == 'U': knots[0][1] -= 1
        elif direction == 'D': knots[0][1] += 1

        for i in range(1, len(knots)):
            H_X, H_Y, T_X, T_Y = knots[i-1][0], knots[i-1][1], knots[i][0], knots[i][1]
            H, T = knots[i-1], knots[i]

            if not is_close(H, T):
                h_x, h_y, t_x, t_y = H[0], H[1], T[0], T[1]
                # Same row
                if h_y == t_y:
                    if h_x > t_x:
                        T[0] += 1
                    else:
                        T[0] -= 1

                # Either 2 steps above or below
                elif abs(h_y - t_y) > 1 and h_x == t_x:
                    if h_y > t_y:
                        T[1] += 1
                    else:
                        T[1] -= 1
                # Diagonal
                elif (abs(h_y - t_y ) > 1 and h_x - t_x != 0) or (abs(h_x - t_x) > 1 and h_y - t_y != 0):
                    if h_y > t_y and h_x > t_x:
                        T[0] += 1
                        T[1] += 1
                    elif h_y > t_y and h_x < t_x:
                        T[0] -= 1
                        T[1] += 1
                    elif h_y < t_y and h_x > t_x:
                        T[0] += 1
                        T[1] -= 1
                    elif h_y < t_y and h_x < t_x:
                        T[0] -= 1
                        T[1] -= 1
            position_number = (T[0], T[1])
            if i == len(knots) - 1 and position_number not in steps_arr:
                steps_arr.append(position_number)


print(len(steps_arr))
