# First, read all the throws from the user and store them in a list.
throws = []
# There are 3 frames in a game.
for frame in range(1, 4):

    if frame < 3:
        ball1 = int(input())
        throws.append(ball1)
        if ball1 < 10:
            ball2 = int(input())
            throws.append(ball2)
    else:
        ball1 = int(input())
        throws.append(ball1)

        ball2 = int(input())
        throws.append(ball2)
        if ball1 == 10 or (ball1 + ball2) == 10:
            ball3 = int(input())
            throws.append(ball3)

total_score = 0
throw_index = 0
for frame in range(1, 4):
    if throws[throw_index] == 10:
        total_score += 10 + throws[throw_index + 1] + throws[throw_index + 2]
        throw_index += 1
    elif throws[throw_index] + throws[throw_index + 1] == 10:
        total_score += 10 + throws[throw_index + 2]
        throw_index += 2
    else:
        total_score += throws[throw_index] + throws[throw_index + 1]
        throw_index += 2

print(total_score)
