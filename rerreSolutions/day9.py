file_name = "input.txt"
with open(file_name, 'r') as f:
    data = f.read().split('\n')

def is_close(h, t):
    h_x, h_y, t_x, t_y = h[0], h[1], t[0], t[1]

    if abs(h_x - t_x) > 1 or abs(h_y - t_y) > 1:
        return False
    return True

H = [0, 4]
T = [0, 4]
steps_arr = []

for com in data:
    direction, steps = com.split(' ')[0], int(com.split(' ')[1])
    for step in range(steps):
        H_X, H_Y, T_X, T_Y = H[0], H[1], T[0], T[1]
        if direction == 'R': H[0] += 1
        elif direction == 'L': H[0] -= 1
        elif direction == 'U': H[1] -= 1
        elif direction == 'D': H[1] += 1

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
        if position_number not in steps_arr:
            steps_arr.append(position_number)


print(len(steps_arr))
